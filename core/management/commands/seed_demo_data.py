from django.core.management.base import BaseCommand

from core.models import ClientTestimonial, CoreValue, ImpactStat, TeamMember
from sectors.models import Sector
from services.models import Service


class Command(BaseCommand):
    help = "Inaongeza data za mfano (seed data) ili tovuti isionekane tupu baada ya deployment."

    def handle(self, *args, **options):
        if Sector.objects.exists():
            self.stdout.write(self.style.WARNING("Data tayari ipo. Hakuna kilichoongezwa."))
            return

        sectors = [
            ("Socio-Economic Research", "Tafiti za Kijamii na Uchumi",
             "socio-economic-research", "bar-chart-2"),
            ("Market & Consumer Insights", "Tafiti za Masoko na Wateja",
             "market-consumer-insights", "shopping-bag"),
            ("Health & Public Policy", "Tafiti za Afya na Sera za Umma",
             "health-public-policy", "activity"),
            ("Agriculture & Environmental Studies", "Tafiti za Kilimo na Mazingira",
             "agriculture-environmental-studies", "sun"),
            ("Data Science & Monitoring and Evaluation", "Sayansi ya Data na M&E",
             "data-science-me", "cpu"),
        ]
        for i, (name_en, name_sw, slug, icon) in enumerate(sectors):
            Sector.objects.create(
                name_en=name_en, name_sw=name_sw, slug=slug, icon=icon, order=i,
                summary_en=f"Utafiti wa kina katika eneo la {name_en}, ukitumia mbinu za kisasa za uchambuzi wa data.",
                summary_sw=f"Utafiti wa kina katika eneo la {name_sw}, ukitumia mbinu za kisasa za uchambuzi wa data.",
            )

        services = [
            ("Quantitative Data Collection", "Ukusanyaji wa Data za Takwimu"),
            ("Qualitative Insights", "Uchambuzi wa Kimaelezo"),
            ("Advanced Analytics & Visualization", "Uchambuzi wa Hali ya Juu"),
            ("Impact Evaluation & M&E", "Tathmini ya Miradi"),
        ]
        for i, (title_en, title_sw) in enumerate(services):
            Service.objects.create(
                title_en=title_en, title_sw=title_sw, order=i,
                description_en=f"{title_en} kwa viwango vya kimataifa, vinavyokidhi mahitaji ya wateja wa taasisi.",
                description_sw=f"{title_sw} kwa viwango vya kimataifa, vinavyokidhi mahitaji ya wateja wa taasisi.",
            )

        stats = [
            ("100+", "Projects Completed", "Miradi Iliyokamilika"),
            ("50+", "Enterprise Clients", "Wateja wa Taasisi"),
            ("5", "Sector Specialties", "Sekta za Utaalamu"),
            ("15+", "Countries Reached", "Nchi Zilizofikiwa"),
        ]
        for i, (number, label_en, label_sw) in enumerate(stats):
            ImpactStat.objects.create(number=number, label_en=label_en, label_sw=label_sw, order=i)

        values = [
            ("Accuracy", "Usahihi"),
            ("Integrity", "Uadilifu"),
            ("Innovation", "Ubunifu"),
        ]
        for i, (title_en, title_sw) in enumerate(values):
            CoreValue.objects.create(
                title_en=title_en, title_sw=title_sw, order=i,
                description_en=f"Tunazingatia {title_en.lower()} katika kila hatua ya utafiti wetu.",
                description_sw=f"Tunazingatia {title_sw.lower()} katika kila hatua ya utafiti wetu.",
            )

        TeamMember.objects.create(
            full_name="Mkurugenzi Mtendaji (Weka Jina Halisi)",
            role_en="Chief Executive Officer",
            role_sw="Mkurugenzi Mtendaji",
            bio_en="Ongeza wasifu halisi wa uongozi wako hapa kupitia Admin Panel.",
            order=0,
        )

        ClientTestimonial.objects.create(
            client_name="Jina la Mteja (Mfano)",
            client_organization="Taasisi ya Mfano",
            quote_en="Ushuhuda wa mteja utaonekana hapa - ongeza kupitia Admin Panel.",
            quote_sw="Ushuhuda wa mteja utaonekana hapa - ongeza kupitia Admin Panel.",
            order=0,
        )

        self.stdout.write(self.style.SUCCESS("Data za mfano zimeongezwa kikamilifu!"))
