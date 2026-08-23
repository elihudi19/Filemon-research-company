from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insights', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='video_url',
            field=models.URLField(blank=True, help_text='Bandika link ya YouTube au Vimeo (hiari). Mfano: https://www.youtube.com/watch?v=XXXXXXXXXXX'),
        ),
    ]
