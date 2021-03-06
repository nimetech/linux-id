# Generated by Django 3.0.3 on 2020-09-02 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_meta_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=models.ImageField(default='featured_image/none.png', upload_to='featured_image'),
        ),
        migrations.AlterField(
            model_name='post',
            name='meta_keyword',
            field=models.CharField(default=None, max_length=750),
        ),
    ]
