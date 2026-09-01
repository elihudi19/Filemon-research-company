import core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insights', '0002_article_video_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='video_file',
            field=models.FileField(blank=True, help_text='AU pakia video moja kwa moja (hiari, MP4/MOV/WEBM, upeo 50MB). Kama zote mbili zimejazwa, link ya YouTube/Vimeo itatumika kwanza.', null=True, upload_to='articles/videos/', validators=[core.validators.validate_video_file]),
        ),
    ]
