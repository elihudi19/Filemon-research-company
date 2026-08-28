from django.db import migrations, models
from django.utils.text import slugify


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
        migrations.AddField(
            model_name="service",
            name="slug",
            field=models.SlugField(blank=True, null=True, unique=False),
        ),
        migrations.RunPython(populate_slugs, reverse_noop),
        migrations.AlterField(
            model_name="service",
            name="slug",
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
