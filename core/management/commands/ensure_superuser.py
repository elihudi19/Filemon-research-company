import os

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = (
        "Inaunda au kusasisha akaunti ya Lead Admin (superuser) kwa kutumia "
        "username/password kutoka Environment Variables (DJANGO_SUPERUSER_USERNAME, "
        "DJANGO_SUPERUSER_EMAIL, DJANGO_SUPERUSER_PASSWORD). Salama kuendesha kila "
        "deploy - haifanyi chochote endapo variables hazijawekwa."
    )

    def handle(self, *args, **options):
        username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

        if not username or not password:
            self.stdout.write(
                self.style.WARNING(
                    "DJANGO_SUPERUSER_USERNAME/PASSWORD hazijawekwa - hakuna admin "
                    "iliyoundwa. Hii ni sawa kama tayari una admin mwingine."
                )
            )
            return

        user, created = User.objects.get_or_create(
            username=username,
            defaults={"email": email, "is_staff": True, "is_superuser": True},
        )
        user.email = email
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()

        if created:
            self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' imeundwa kikamilifu."))
        else:
            self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' tayari ipo - password imesasishwa."))
