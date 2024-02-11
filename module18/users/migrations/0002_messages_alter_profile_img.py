# Generated by Django 5.0 on 2023-12-30 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Topic')),
                ('sender', models.EmailField(max_length=254, verbose_name='Sender')),
                ('text', models.TextField(verbose_name='Text')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='profile-default.png', upload_to='user_img', verbose_name='Photo'),
        ),
    ]
