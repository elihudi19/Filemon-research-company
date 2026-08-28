from django.db import migrations


SECTORS_DATA = [
    {
        "icon": "book-open",
        "slug": "education",
        "name_en": "Education",
        "name_sw": "Elimu",
        "summary_en": (
            "We provide research, technology, and policy support across the "
            "education sector.\n\n"
            "* Educational Research & Assessment\n"
            "* Academic Performance Analytics\n"
            "* EdTech & Digital Learning\n"
            "* Educational Policy & Governance"
        ),
        "summary_sw": (
            "Tunatoa huduma za utafiti, teknolojia, na ushauri wa sera katika "
            "sekta ya elimu.\n\n"
            "* Utafiti na Tathmini ya Viwango vya Elimu\n"
            "* Uchambuzi wa Matokeo na Utendaji wa Wanafunzi\n"
            "* Teknolojia katika Elimu\n"
            "* Sera za Elimu na Usimamizi wa Shule"
        ),
    },
    {
        "icon": "trending-up",
        "slug": "socio-economic-development",
        "name_en": "Socio-Economic Development",
        "name_sw": "Uchumi na Maendeleo ya Jamii",
        "summary_en": (
            "We support institutions working on economic policy, community "
            "development, and inclusive growth.\n\n"
            "* Economic Policy & Data Analysis\n"
            "* Community Development & Social Impact\n"
            "* Poverty & Welfare Studies\n"
            "* Inclusive Finance & Markets"
        ),
        "summary_sw": (
            "Tunasaidia taasisi zinazofanya kazi katika sera za kiuchumi, "
            "maendeleo ya jamii, na ukuaji jumuishi.\n\n"
            "* Uchambuzi wa Sera za Kiuchumi\n"
            "* Maendeleo ya Jamii na Uwezeshaji\n"
            "* Tafiti za Umaskini na Ustawi wa Jamii\n"
            "* Fedha na Biashara"
        ),
    },
    {
        "icon": "sun",
        "slug": "agriculture-environment-sustainability",
        "name_en": "Agriculture, Environment & Sustainability",
        "name_sw": "Kilimo, Maliasili na Mazingira",
        "summary_en": (
            "We work with institutions on climate-resilient agriculture, "
            "natural resource management, and food systems.\n\n"
            "* Climate-Smart Agriculture\n"
            "* Environmental & Resource Management\n"
            "* Food Security & Agricultural Analytics\n"
            "* GIS & Spatial Mapping"
        ),
        "summary_sw": (
            "Tunafanya kazi na taasisi katika kilimo hifadhi, usimamizi wa "
            "maliasili, na mifumo ya chakula.\n\n"
            "* Kilimo Hifadhi na Mabadiliko ya Tabianchi\n"
            "* Usimamizi wa Maliasili na Mazingira\n"
            "* Uchanganuzi wa Mifumo ya Chakula\n"
            "* Mifumo ya Taarifa za Jiografia na Mipango Ardhini"
        ),
    },
    {
        "icon": "cpu",
        "slug": "data-science-monitoring-evaluation",
        "name_en": "Data Science, Monitoring & Evaluation",
        "name_sw": "Sayansi ya Data, Ufuatiliaji na Tathmini",
        "summary_en": (
            "We help organizations build data systems and M&E frameworks that "
            "turn information into action.\n\n"
            "* Data Engineering, Wrangling & Analytics\n"
            "* Monitoring & Evaluation Frameworks\n"
            "* Survey Design & Mobile Data Collection\n"
            "* Machine Learning & Predictive Modeling"
        ),
        "summary_sw": (
            "Tunasaidia mashirika kujenga mifumo ya data na M&E inayobadili "
            "taarifa kuwa hatua za utekelezaji.\n\n"
            "* Usimamizi na Uchambuzi wa Data\n"
            "* Uundaji wa Mifumo ya M&E\n"
            "* Muundo wa Tafiti na Ukusanyaji wa Data\n"
            "* Akili Bandia na Mifumo ya Kutabiri"
        ),
    },
]


def replace_sectors(apps, schema_editor):
    Sector = apps.get_model("sectors", "Sector")
    Sector.objects.all().delete()
    for i, data in enumerate(SECTORS_DATA):
        Sector.objects.create(order=i, is_published=True, **data)


def reverse_noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("sectors", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(replace_sectors, reverse_noop),
    ]
