# Generated by Django 2.0.7 on 2018-07-13 10:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import project.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HourPaymentORM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.FloatField(default=0)),
                ('start_rout_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_rout_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MonthPaymentORM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectORM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('end_date', models.DateTimeField(null=True)),
                ('type_of_payment', models.CharField(choices=[('H_P', 'Почасовая'), ('M_P', 'Помесячная'), ('T_P', 'Позадачная')], max_length=3)),
                ('status', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.UserORM')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='WorkDayORM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(default=project.models.current_date)),
                ('paid', models.BooleanField(default=False)),
                ('month_payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.MonthPaymentORM')),
            ],
        ),
        migrations.CreateModel(
            name='WorkTaskORM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField(null=True)),
                ('price', models.FloatField(default=0)),
                ('completed', models.BooleanField(default=False)),
                ('paid', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.ProjectORM')),
            ],
        ),
        migrations.CreateModel(
            name='WorkTimeORM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_work', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_work', models.DateTimeField(null=True)),
                ('paid', models.BooleanField(default=False)),
                ('hour_payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.HourPaymentORM')),
            ],
        ),
        migrations.AddField(
            model_name='monthpaymentorm',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.ProjectORM'),
        ),
        migrations.AddField(
            model_name='hourpaymentorm',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.ProjectORM'),
        ),
    ]
