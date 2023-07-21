# Generated by Django 4.2.2 on 2023-07-01 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('participant', '0001_initial'),
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=6)),
                ('payment_method', models.CharField(max_length=100)),
                ('payment_date', models.DateTimeField()),
                ('transaction_id', models.CharField(max_length=100)),
                ('payment_status', models.CharField(choices=[('paid', 'Paid'), ('pending', 'Pending'), ('failed', 'Failed')], max_length=10)),
                ('Participant_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='participant.participant')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event')),
            ],
        ),
    ]