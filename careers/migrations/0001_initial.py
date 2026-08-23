import core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobPosting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_en', models.CharField(max_length=200)),
                ('title_sw', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('department_en', models.CharField(blank=True, max_length=150)),
                ('department_sw', models.CharField(blank=True, max_length=150)),
                ('employment_type', models.CharField(choices=[('full_time', 'Full-Time'), ('part_time', 'Part-Time'), ('contract', 'Contract'), ('internship', 'Internship')], default='part_time', max_length=20)),
                ('location', models.CharField(default='Dar es Salaam, Tanzania', max_length=150)),
                ('description_en', models.TextField()),
                ('description_sw', models.TextField()),
                ('requirements_en', models.TextField(blank=True)),
                ('requirements_sw', models.TextField(blank=True)),
                ('application_deadline', models.DateField(blank=True, null=True)),
                ('is_published', models.BooleanField(default=True)),
                ('posted_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-posted_date'],
            },
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=30)),
                ('cover_message', models.TextField()),
                ('resume', models.FileField(help_text='CV/Resume (PDF/DOC), upeo wa 5MB.', upload_to='careers/resumes/', validators=[core.validators.validate_document_file])),
                ('status', models.CharField(choices=[('new', 'Mpya'), ('reviewing', 'Inapitiwa'), ('shortlisted', 'Amechaguliwa Awali'), ('rejected', 'Hakufaulu'), ('hired', 'Ameajiriwa')], default='new', max_length=20)),
                ('submitted_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='careers.jobposting')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
