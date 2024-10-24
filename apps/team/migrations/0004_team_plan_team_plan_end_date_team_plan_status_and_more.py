# Generated by Django 5.1.1 on 2024-10-16 14:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='plan',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='team.plan'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='plan_end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='plan_status',
            field=models.CharField(choices=[('active', 'Active'), (' canceled', 'Canceled')], default='active', max_length=20),
        ),
        migrations.AddField(
            model_name='team',
            name='stripe_customer_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='stripe_subscription_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]