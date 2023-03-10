# Generated by Django 4.1.5 on 2023-02-11 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('ACCEPTED', 'ACCEPTED'), ('NEW', 'NEW'), ('CANCELLED', 'CANCELLED'), ('COMPLETED', 'COMPLETED')], default='NEW', max_length=10),
        ),
    ]
