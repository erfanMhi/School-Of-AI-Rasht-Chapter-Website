# Generated by Django 2.1.5 on 2019-01-29 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField()),
                ('finish_date', models.DateTimeField()),
                ('organizer', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('cover_url', models.ImageField(upload_to='events/covers/%Y/%m/%D/')),
                ('logo_url', models.ImageField(upload_to='events/logos/%Y/%m/%D/')),
                ('description', models.TextField(default='', max_length=500)),
                ('categories', models.ManyToManyField(to='events.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('resume_url', models.FileField(blank=True, max_length=200, null=True, upload_to='lecturers/resumes/%Y/%m/%D/')),
                ('photo_url', models.ImageField(blank=True, max_length=200, null=True, upload_to='lecturers/resumes/%Y/%m/%D/')),
            ],
        ),
        migrations.AddField(
            model_name='lecture',
            name='lecturer',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='events.Lecturer'),
        ),
    ]