# Generated by Django 4.0 on 2021-12-29 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzamart', '0007_alter_order_delivering_alter_order_preparing_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.CharField(default=' ', max_length=200),
            preserve_default=False,
        ),
    ]
