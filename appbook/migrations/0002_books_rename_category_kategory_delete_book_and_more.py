# Generated by Django 4.2.1 on 2023-06-30 09:53

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appbook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('page', models.IntegerField()),
                ('publish_date', models.DateTimeField()),
                ('book_of_author', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('slug', models.SlugField(max_length=255, null=True, unique=True)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('post_img', models.ImageField(upload_to='posts')),
                ('date_added', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to='files')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Kitoblar',
            },
        ),
        migrations.RenameModel(
            old_name='Category',
            new_name='Kategory',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.AddField(
            model_name='books',
            name='cat_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appbook.kategory'),
        ),
    ]
