from django.db import migrations


SERVICES_DATA = [
    {
        "icon": "code",
        "title_en": "Custom Software & Mobile App Development",
        "title_sw": "Uundaji wa Mifumo Maalum na Programu za Simu",
        "description_en": (
            "We build digital systems tailored to the real needs of your business "
            "or institution, using modern, robust, and scalable technologies.\n\n"
            "* Web Platforms & Portals: Development of Management Information "
            "Systems (MIS), Enterprise Resource Planning (ERP) systems, and "
            "modern websites.\n"
            "* Mobile Applications: Building Android and iOS apps with clean "
            "user experience (UI/UX) and offline-first capabilities.\n"
            "* API & Payment Integration: Connecting your systems with mobile "
            "money services (M-Pesa, Tigo Pesa, Airtel Money), SMS platforms, "
            "or other third-party systems."
        ),
        "description_sw": (
            "Tunaunda mifumo ya kidijitali iliyoboreshwa kulingana na mahitaji "
            "halisi ya biashara au taasisi yako. Mifumo yetu inajengwa kwa "
            "kutumia teknolojia za kisasa, imara, na zenye uwezo wa kukua "
            "kulingana na mahitaji ya baadaye (scalable systems).\n\n"
            "* Mifumo na Tovuti za Wavuti: Ujenzi wa mifumo ya usimamizi wa "
            "taarifa (MIS), mifumo ya uendeshaji wa biashara (ERP), na wavuti "
            "za kisasa.\n"
            "* Programu za Simu: Kuunda apps za simu (Android na iOS) zenye "
            "muonekano rahisi kwa mtumiaji (UI/UX) na uwezo wa kufanya kazi "
            "hata bila mtandao.\n"
            "* Uunganishaji wa API na Malipo: Kuunganisha mifumo yako na njia "
            "za malipo ya simu (M-Pesa, Tigo Pesa, Airtel Money), majukwaa ya "
            "SMS, au mifumo mingine ya nje."
        ),
    },
    {
        "icon": "bar-chart-2",
        "title_en": "Data Analytics & Business Intelligence (BI)",
        "title_sw": "Uchambuzi wa Data na Akili ya Kibiashara (BI)",
        "description_en": (
            "We help institutions turn scattered data into clear, actionable "
            "insight for strategic decision-making.\n\n"
            "* Interactive Dashboards: Building digital dashboards that show "
            "sales trends, performance, and key performance indicators (KPIs) "
            "in real time.\n"
            "* Data Wrangling & Cleaning: Processing and cleaning disorganized "
            "or inconsistent data to prepare it for formal analysis.\n"
            "* Automated Reporting: Setting up systems that generate weekly or "
            "monthly reports automatically, saving staff time."
        ),
        "description_sw": (
            "Tunasaidia taasisi kubadili data zao zilizotapakaa kuwa taarifa "
            "zenye uelewa mpana na rahisi kutumika katika kufanya maamuzi ya "
            "kimkakati.\n\n"
            "* Dashboards Zenye Mwingiliano: Ujenzi wa dashboards za kidijitali "
            "zinazoonyesha mwelekeo wa mauzo, utendaji wa kazi, na viashiria "
            "kuu vya mafanikio (KPIs) kwa wakati halisi.\n"
            "* Usafishaji wa Data: Kuchakata na kusafisha data zilizochanganyika "
            "au zenye makosa ili ziwe tayari kwa uchambuzi rasmi.\n"
            "* Ripoti za Kiotomatiki: Kuweka mifumo inayozalisha ripoti za kila "
            "wiki au kila mwezi kiotomatiki bila kupoteza muda wa wafanyakazi."
        ),
    },
    {
        "icon": "clipboard",
        "title_en": "Digital Data Collection & Survey Solutions",
        "title_sw": "Ukusanyaji wa Data za Kidijitali na Masuluhisho ya Tafiti",
        "description_en": (
            "We streamline the entire field data collection process by "
            "eliminating paper-based methods and reducing data loss or errors.\n\n"
            "* ODK & Mobile Survey Design: Designing and configuring digital "
            "questionnaires through ODK (Open Data Kit), KoboToolbox, and "
            "other modern mobile tools.\n"
            "* Real-Time Data Monitoring: Setting up systems that allow "
            "research supervisors to view field data as it is collected "
            "(real-time data validation).\n"
            "* Capacity Building: Training data collection teams (enumerators) "
            "on proper use of digital tools and research ethics."
        ),
        "description_sw": (
            "Tunarahisisha mchakato mzima wa ukusanyaji wa data za tafiti "
            "nyanjani kwa kuondoa matumizi ya karatasi na kuzuia upotevu au "
            "makosa ya takwimu.\n\n"
            "* Usanifu wa Tafiti kwa ODK na Simu: Kuandaa na kusanidi dodoso za "
            "kidijitali kupitia ODK (Open Data Kit), KoboToolbox, na zana za "
            "kisasa za simu.\n"
            "* Ufuatiliaji wa Data kwa Wakati Halisi: Kuweka mifumo "
            "inayomwezesha msimamizi wa utafiti kuona data zinazokusanywa "
            "uwanjani papo hapo.\n"
            "* Kujenga Uwezo: Kutoa mafunzo kwa timu za ukusanyaji data "
            "(enumerators) kuhusu matumizi sahihi ya zana za kidijitali na "
            "maadili ya utafiti."
        ),
    },
    {
        "icon": "cpu",
        "title_en": "Machine Learning & Predictive Analytics",
        "title_sw": "Akili Bandia (Machine Learning) na Uchambuzi Tabiri",
        "description_en": (
            "We apply modern Data Science and Artificial Intelligence "
            "techniques to help institutions predict future outcomes and "
            "prepare in advance.\n\n"
            "* Predictive Modeling: Building models that forecast market "
            "trends, education-sector performance, or customer behavior in "
            "business.\n"
            "* Risk & Churn Assessment: Analyzing financial risk and "
            "identifying customers or users who are likely to stop using a "
            "given service.\n"
            "* Pattern Recognition: Identifying hidden patterns within Big "
            "Data to uncover new opportunities for institutional growth."
        ),
        "description_sw": (
            "Tunatumia kanuni za kisasa za Sayansi ya Data (Data Science) na "
            "Akili Bandia (AI) kusaidia taasisi kutabiri matokeo ya baadaye na "
            "kujiandaa mapema.\n\n"
            "* Uundaji wa Mifano Tabiri: Kujenga mifumo inayotabiri mwenendo wa "
            "soko, utendaji wa sekta ya elimu, au tabia za wateja kwenye "
            "biashara.\n"
            "* Tathmini ya Vihatarishi: Uchambuzi wa vihatarishi vya kifedha na "
            "kubaini wateja au watumiaji wanaoelekea kuacha kutumia huduma "
            "fulani.\n"
            "* Utambuzi wa Mifumo: Kuitambua mifumo iliyojificha kwenye data "
            "kubwa (Big Data) ili kuvumbua fursa mpya za kukuza taasisi."
        ),
    },
    {
        "icon": "map",
        "title_en": "GIS & Spatial Data Analysis",
        "title_sw": "GIS na Uchambuzi wa Data za Kijiografia",
        "description_en": (
            "We conduct Geographic Information Systems (GIS) analysis to bring "
            "spatial meaning to development, business, and natural-resource "
            "projects.\n\n"
            "* Spatial Mapping: Creating digital maps showing the distribution "
            "of resources, customers, or social services using tools such as "
            "QGIS.\n"
            "* Site Selection & Proximity Analysis: Analyzing optimal locations "
            "for opening business branches or service centers based on "
            "population and distance.\n"
            "* Environmental & Resource Tracking: Monitoring changes in land "
            "use, agriculture, and the environment using geographic data."
        ),
        "description_sw": (
            "Tunafanya uchambuzi wa data za kijiografia (Geographic Information "
            "Systems) ili kutoa maana ya ki-maeneo katika miradi ya maendeleo, "
            "biashara, na maliasili.\n\n"
            "* Uchoraji wa Ramani: Kuunda ramani za kidijitali zinazoonyesha "
            "mtawanyiko wa rasilimali, wateja, au huduma za kijamii kwa "
            "kutumia zana kama QGIS.\n"
            "* Uchambuzi wa Uchaguzi wa Maeneo: Uchambuzi wa maeneo sahihi ya "
            "kufungua matawi ya biashara au vituo vya huduma kulingana na "
            "idadi ya watu na umbali.\n"
            "* Ufuatiliaji wa Mazingira na Rasilimali: Kuonyesha na kufuatilia "
            "mabadiliko ya matumizi ya ardhi, kilimo, na mazingira kwa "
            "kutumia takwimu za kijiografia."
        ),
    },
    {
        "icon": "activity",
        "title_en": "Monitoring, Evaluation, and Learning (MEL) Digital Solutions",
        "title_sw": "Masuluhisho ya Kidijitali ya Ufuatiliaji, Tathmini, na Ujifunzaji (MEL)",
        "description_en": (
            "We help NGOs, government agencies, and donors measure the impact "
            "of their projects through modern Monitoring and Evaluation "
            "systems.\n\n"
            "* Digital MEL Frameworks: Setting up performance indicators and "
            "systems to track project progress from start to finish.\n"
            "* Impact Assessment & Baseline Studies: Conducting baseline, "
            "mid-term, and endline evaluation studies.\n"
            "* Data-Driven Storytelling: Turning research findings into "
            "reports with visuals, maps, and statistics that are easy for "
            "donors and communities to understand."
        ),
        "description_sw": (
            "Tunasaidia Mashirika Yasiyo ya Kiserikali (NGOs), Serikali, na "
            "Wafadhili kupima athari za miradi yao kupitia mifumo ya kisasa ya "
            "Ufuatiliaji na Tathmini.\n\n"
            "* Mifumo ya Kidijitali ya MEL: Kusanidi viashiria vya utendaji na "
            "mifumo ya kufuatilia maendeleo ya mradi kuanzia mwanzo hadi "
            "mwisho.\n"
            "* Tathmini ya Athari na Tafiti za Awali: Kufanya tafiti za awali "
            "(baseline), za katikati (mid-term), na tathmini ya mwisho ya "
            "mradi (endline evaluation).\n"
            "* Ueleweshaji wa Data: Kubadili matokeo ya utafiti kuwa ripoti "
            "zenye vielelezo vya picha, ramani, na takwimu zinazoeleweka kwa "
            "urahisi kwa wafadhili na jamii."
        ),
    },
]


def replace_services(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    Service.objects.all().delete()
    for i, data in enumerate(SERVICES_DATA):
        Service.objects.create(order=i, is_published=True, **data)


def reverse_noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(replace_services, reverse_noop),
    ]
