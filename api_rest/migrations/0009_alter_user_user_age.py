# Generated by Django 4.2.5 on 2023-09-29 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0008_delete_tarefa_user_user_age_user_user_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_age',
            field=models.IntegerField(default=0, verbose_name='Idade'),
        ),
    ]