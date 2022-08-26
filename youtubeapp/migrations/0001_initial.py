# Generated by Django 4.1 on 2022-08-26 04:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('tel', models.CharField(max_length=13)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vedio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('vedio', models.FileField(upload_to='')),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='youtubeapp.account')),
            ],
        ),
        migrations.CreateModel(
            name='Pleylist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('ochiq', models.BooleanField(default=True)),
                ('vediolar', models.ManyToManyField(to='youtubeapp.vedio')),
            ],
        ),
        migrations.CreateModel(
            name='Obuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obunachilar', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='obunachilar', to='youtubeapp.account')),
                ('obunalar', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='obunalar', to='youtubeapp.account')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='youtubeapp.account')),
                ('video', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='youtubeapp.vedio')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('vedio', models.FileField(upload_to='')),
                ('account', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='youtubeapp.account')),
            ],
        ),
    ]
