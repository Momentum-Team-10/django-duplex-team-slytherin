# Generated by Django 3.2.9 on 2021-11-13 20:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('snippet', '0002_snippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='decks', to='snippet.user'),
            preserve_default=False,
        ),
    ]
