# Generated by Django 3.0.4 on 2020-06-27 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1024)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('approved', models.DateTimeField(blank=True, null=True)),
                ('votes', models.IntegerField(default=0, editable=False, help_text='Number of votes')),
            ],
        ),
    ]