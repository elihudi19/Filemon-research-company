from django.db import migrations, models
from django.utils.text import slugify


def cleanup_partial_state(apps, schema_editor):
    """
    Usafishaji wa kinga: ikiwa jaribio la awali la migration hii lilishindwa
    likaacha mabaki ya column/index ya 'slug' kwenye PostgreSQL (kwa mfano kwa
    sababu ya connection pooling isiyohifadhi transaction), tunaifuta kwanza
    kabla ya kuiongeza upya. Ni salama kuendesha hata kama hakuna mabaki
    (IF EXISTS), na haiathiri SQLite (dev pekee).
    """
    if schema_editor.connection.vendor == "postgresql":
        with schema_editor.connection.cursor() as cursor:
            cursor.execute("ALTER TABLE services_service DROP COLUMN IF EXISTS slug CASCADE;")


def reverse_cleanup_noop(apps, schema_editor):
    pass


def populate_slugs(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    used_slugs = set()
    for service in Service.objects.all():
        base_slug = slugify(service.title_en) or f"service-{service.pk}"
        slug = base_slug
        counter = 2
        while slug in used_slugs or Service.objects.filter(slug=slug).exclude(pk=service.pk).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        used_slugs.add(slug)
        service.slug = slug
        service.save(update_fields=["slug"])


def reverse_noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0002_seed_rcti_services"),
    ]

    operations = [
        migrations.RunPython(cleanup_partial_state, reverse_cleanup_noop),
        migrations.AddField(
            model_name="service",
            name="slug",
            field=models.SlugField(max_length=255, blank=True, null=True, unique=False),
        ),
        migrations.RunPython(populate_slugs, reverse_noop),
        migrations.AlterField(
            model_name="service",
            name="slug",
            field=models.SlugField(max_length=255, blank=True, unique=True),
        ),
    ]
