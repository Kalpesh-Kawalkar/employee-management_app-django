# Generated by Django 4.1.6 on 2023-04-09 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0003_alter_emp_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='address',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
