from django.db import migrations


CONTENT_EDITOR_GROUP = "Content Editor"

FULL_ACCESS_MODELS = [
    ("insights", "publication"),
    ("insights", "article"),
    ("careers", "jobposting"),
    ("core", "clienttestimonial"),
    ("core", "impactstat"),
]

VIEW_AND_CHANGE_MODELS = [
    ("proposals", "proposalrequest"),
    ("careers", "jobapplication"),
]


def create_content_editor_group(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Permission = apps.get_model("auth", "Permission")
    ContentType = apps.get_model("contenttypes", "ContentType")

    def get_or_create_perms(app_label, model_name, actions):
        ct, _ = ContentType.objects.get_or_create(app_label=app_label, model=model_name)
        perms = []
        for action in actions:
            codename = f"{action}_{model_name}"
            perm, _ = Permission.objects.get_or_create(
                content_type=ct,
                codename=codename,
                defaults={"name": f"Can {action} {model_name}"},
            )
            perms.append(perm)
        return perms

    group, _ = Group.objects.get_or_create(name=CONTENT_EDITOR_GROUP)

    permission_ids = []
    for app_label, model_name in FULL_ACCESS_MODELS:
        permission_ids += [p.id for p in get_or_create_perms(app_label, model_name, ["add", "change", "view"])]

    for app_label, model_name in VIEW_AND_CHANGE_MODELS:
        permission_ids += [p.id for p in get_or_create_perms(app_label, model_name, ["view", "change"])]

    group.permissions.set(permission_ids)


def remove_content_editor_group(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Group.objects.filter(name=CONTENT_EDITOR_GROUP).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
        ("insights", "0001_initial"),
        ("careers", "0001_initial"),
        ("proposals", "0001_initial"),
        ("contenttypes", "0002_remove_content_type_name"),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.RunPython(create_content_editor_group, remove_content_editor_group),
    ]
