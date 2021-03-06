# Generated by Django 4.0.3 on 2022-03-18 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('prefix', models.CharField(choices=[('นาย', 'นาย'), ('นาง', 'นาง'), ('นางสาว', 'นางสาว')], max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('อาจารย์ผู้ประสานงาน', 'อาจารย์ผู้ประสานงาน'), ('อาจารย์ผู้ออกนิเทศนักศึกษา', 'อาจารย์ผู้ออกนิเทศนักศึกษา')], default='อาจารย์ผู้ออกนิเทศนักศึกษา', max_length=255)),
            ],
        ),
    ]
