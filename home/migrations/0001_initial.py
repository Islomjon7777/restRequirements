# Generated by Django 5.0.3 on 2024-03-04 13:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BogchalarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('text', models.TextField()),
                ('bogcha_image', models.ImageField(upload_to='BogchaImages/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(default='user', max_length=100)),
                ('lastname', models.CharField(default='user', max_length=100)),
                ('userEmail', models.CharField(default='example@gmail.com', max_length=100)),
                ('userImg', models.ImageField(upload_to='userImages/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=150)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('bogchaComment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.bogchalarmodel')),
                ('userComment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.profilemodel')),
            ],
        ),
        migrations.AddField(
            model_name='bogchalarmodel',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.profilemodel'),
        ),
        migrations.CreateModel(
            name='TumanlarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tuman', models.CharField(choices=[('bektemir', 'Bektemir'), ('chilonzor', 'Chilonzor'), ('mirobod', 'Mirobod'), ('mirzo u.', 'Mirzo U.'), ('olmazor', 'Olmazor'), ('sergeli', 'Sergeli'), ('shayhontohur', 'Shayhontohur'), ('uchtepa', 'Uchtepa'), ('yakkasaroy', 'Yakkasaroy'), ('yashnaobod', 'Yashnaobod'), ('yunusobod', 'Yunusobod'), ('yangihayot', 'Yangihayot')], default='Bektemir', max_length=12)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('bogchalar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.bogchalarmodel')),
            ],
        ),
    ]