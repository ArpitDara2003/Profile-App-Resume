# Generated by Django 5.0.4 on 2024-05-02 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_username', models.CharField(default='Robot', max_length=255)),
                ('certificate_name', models.CharField(max_length=255)),
                ('certificate_image', models.ImageField(default='static/images/img1.png', upload_to='static/certificates')),
                ('short_discription', models.CharField(default='', max_length=255)),
                ('detailed_discription', models.CharField(default='', max_length=6000)),
            ],
        ),
        migrations.CreateModel(
            name='Creater',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(default='Robot', max_length=255)),
                ('discription', models.CharField(default='', max_length=255)),
                ('image', models.ImageField(default='static/certificates/Robot.png', upload_to='static/images')),
                ('full_name', models.CharField(default='', max_length=255)),
                ('detailed_discription', models.CharField(default='', max_length=1000)),
                ('date_of_birth', models.CharField(default='', max_length=15)),
                ('address', models.CharField(default='', max_length=255)),
                ('linkedin', models.CharField(default='', max_length=255)),
                ('instagram', models.CharField(default='', max_length=255)),
                ('facebook', models.CharField(default='', max_length=255)),
                ('contact_no', models.CharField(default='', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_username', models.CharField(default='Robot', max_length=255)),
                ('skill_name', models.CharField(default='', max_length=255)),
                ('skill_discription', models.CharField(default='', max_length=255)),
                ('detailed_discription', models.CharField(default='', max_length=6000)),
                ('point1', models.CharField(default='', max_length=255)),
                ('point2', models.CharField(default='', max_length=255)),
                ('point3', models.CharField(default='', max_length=255)),
                ('point4', models.CharField(default='', max_length=255)),
                ('point5', models.CharField(default='', max_length=255)),
                ('highlighted', models.BooleanField(default=True)),
            ],
        ),
    ]
