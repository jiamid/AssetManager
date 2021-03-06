# Generated by Django 2.2.7 on 2020-05-14 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssetDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assetNum', models.CharField(max_length=11)),
                ('assetName', models.CharField(max_length=22)),
                ('empId', models.CharField(max_length=8)),
                ('userName', models.CharField(max_length=4)),
                ('ownerDept', models.CharField(max_length=20)),
                ('adminId', models.CharField(max_length=11)),
                ('tagText', models.TextField()),
                ('lastTime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
        ),
    ]
