# Generated by Django 3.1 on 2020-09-05 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writing', '0003_auto_20200828_1700'),
        ('login', '0003_auto_20200903_1314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='user_postlist',
        ),
        migrations.AddField(
            model_name='account',
            name='own_blog',
            field=models.ManyToManyField(blank=True, related_name='own_blog', to='writing.Blog'),
        ),
        migrations.AlterField(
            model_name='account',
            name='introduction',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='profile_photo',
            field=models.ImageField(blank=True, default='media/default.jpg', upload_to='media/images'),
        ),
    ]
