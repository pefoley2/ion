# Generated by Django 3.2.15 on 2022-12-24 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0007_alter_cslapplication_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cslapplication',
            name='algorithm',
            field=models.CharField(blank=True, choices=[('', 'No OIDC support')], default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='cslapplication',
            name='authorization_grant_type',
            field=models.CharField(choices=[('authorization-code', 'Authorization code'), ('client-credentials', 'Client credentials')], max_length=32),
        ),
    ]
