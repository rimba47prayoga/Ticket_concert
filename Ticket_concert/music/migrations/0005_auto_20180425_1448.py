# Generated by Django 2.0.4 on 2018-04-25 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0004_auto_20180424_2351'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket_transaction',
            fields=[
                ('idapp', models.AutoField(primary_key=True, serialize=False)),
                ('total_buy', models.IntegerField()),
                ('createddate', models.DateTimeField(auto_now_add=True)),
                ('modifieddate', models.DateTimeField(auto_now=True)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='ticket',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='ticket_buyed',
        ),
    ]