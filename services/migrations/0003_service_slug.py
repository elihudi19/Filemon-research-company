from django.db import migrations, models
from django.utils.text import slugify


def cleanup_partial_state(apps, schema_editor):
    """
    Usafishaji wa kinga: PostgreSQL ya Render inatumia connection pooling
    ambayo wakati mwingine inavuruga mpangilio wa transaction ya migration,
    ikiacha index/column za 'slug' nusu-nusu kutoka jaribio lililoshindwa
    awali. Tunatafuta na kufuta INDEX YOYOTE yenye jina linaloanza na
    'services_service_slug' (bila kubashiri jina kamili lenye hash), kisha
    tunafuta column yenyewe. Salama kuendesha hata kama hakuna mabaki.
    """
    if schema_editor.connection.vendor == "postgresql":
        with schema_editor.connection.cursor() as cursor:
            cursor.execute(
                """
                DO $$
                DECLARE r RECORD;
                BEGIN
                    FOR r IN
                        SELECT indexname FROM pg_indexes
                        WHERE tablename = 'services_service'
                        AND indexname LIKE 'services_service_slug%%'
                    LOOP
                        EXECUTE 'DROP INDEX IF EXISTS ' || quote_ident(r.indexname) || ' CASCADE';
                    END LOOP;
                END $$;
                """
            )
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

    atomic = False

    dependencies = [
        ("services", "0002_seed_rcti_services"),
    ]

    operations = [
        migrations.RunPython(cleanup_partial_state, reverse_cleanup_noop),
        migrations.AddField(
            model_name="service",
            name="slug",
            field=models.SlugField(max_length=255, blank=True, null=True, unique=False, db_index=False),
        ),
        migrations.RunPython(populate_slugs, reverse_noop),
        migrations.AlterField(
            model_name="service",
            name="slug",
            field=models.SlugField(max_length=255, blank=True, unique=True),
        ),
    ]
