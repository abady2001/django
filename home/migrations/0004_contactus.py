# Generated by Django 4.1 on 2022-10-12 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_takepart_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('user', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
