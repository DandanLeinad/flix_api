# Generated by Django 5.0.3 on 2024-04-05 18:23

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starts', models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Avaliação nao pode ser inferior a 0'), django.core.validators.MaxValueValidator(5, 'Avaliação não pode ser superior a 5')])),
                ('comment', models.TextField(blank=True, null=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reviews', to='movies.movie')),
            ],
        ),
    ]