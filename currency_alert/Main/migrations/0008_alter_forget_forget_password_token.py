# Generated by Django 4.2.6 on 2023-10-09 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0007_forget'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forget',
            name='forget_password_token',
            field=models.CharField(max_length=100, null=True),
        ),
    ]