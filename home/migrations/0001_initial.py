# Generated by Django 4.1.5 on 2023-04-05 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crops', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farm_name', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=False)),
                ('crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cult_crop', to='crops.crops')),
            ],
        ),
    ]
