# Generated by Django 3.1 on 2020-08-22 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200822_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='text',
            field=models.TextField(null=True, verbose_name='Текст статьи'),
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата и время публикации'),
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.CharField(max_length=1000, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.ImageField(upload_to='blog', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название статьи'),
        ),
    ]
