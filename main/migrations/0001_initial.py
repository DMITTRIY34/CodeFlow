# Generated by Django 4.1.7 on 2023-07-05 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=128)),
                ('content', models.TextField(blank=True)),
                ('hidden', models.BooleanField(default=False)),
            ],
        ),
    ]