from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposalrequest',
            name='phone',
            field=models.CharField(max_length=30),
        ),
    ]
