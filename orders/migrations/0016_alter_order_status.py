# Generated by Django 4.1.5 on 2023-02-12 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('NEW', 'NEW'), ('CANCELLED', 'CANCELLED'), ('COMPLETED', 'COMPLETED'), ('ACCEPTED', 'ACCEPTED')], default='NEW', max_length=10),
        ),
    ]
