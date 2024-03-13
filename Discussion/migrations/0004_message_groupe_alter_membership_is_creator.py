# Generated by Django 4.2.4 on 2024-02-17 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Discussion', '0003_alter_membership_is_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='groupe',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Discussion.group'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='is_creator',
            field=models.BooleanField(default=True),
        ),
    ]