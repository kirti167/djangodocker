# Generated by Django 3.2.4 on 2021-11-10 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp_portal', '0002_alter_fees_paymentid'),
    ]

    operations = [
        migrations.AddField(
            model_name='fees',
            name='contact',
            field=models.CharField(blank=True, default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='fees',
            name='created_at',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='fees',
            name='email',
            field=models.CharField(blank=True, default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='fees',
            name='method',
            field=models.CharField(blank=True, default=0, max_length=100),
        ),
    ]
