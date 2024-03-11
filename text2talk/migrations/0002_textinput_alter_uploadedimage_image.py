# Generated by Django 5.0.1 on 2024-03-11 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('text2talk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextInput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name='uploadedimage',
            name='image',
            field=models.ImageField(upload_to='D:\\Coding WIP\\ocr\\text2talk\\static\\images'),
        ),
    ]