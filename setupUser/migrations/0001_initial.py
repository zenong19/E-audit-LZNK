# Generated by Django 4.0.4 on 2022-05-15 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='elemen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('element', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='indikator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('indicator', models.CharField(max_length=100)),
                ('element', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='jabatanAuditi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('department', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='jenis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='jenisBukti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('evidence', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='kumpulanAudit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=10)),
                ('position', models.CharField(max_length=10)),
                ('date', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='penemuanAudit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('outcome', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='perancanganAudit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('programme', models.CharField(max_length=10)),
                ('date', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='risiko',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('risk', models.CharField(max_length=100)),
                ('type', models.CharField(default=None, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='sejarahAudit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('position', models.CharField(max_length=10)),
                ('date', models.CharField(max_length=10)),
                ('staff', models.CharField(max_length=10)),
                ('programme', models.CharField(max_length=10)),
                ('element', models.CharField(max_length=10)),
                ('indicator', models.CharField(max_length=10)),
                ('subIndicator', models.CharField(max_length=10)),
                ('outcome', models.CharField(max_length=10)),
                ('remark', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='senaraiSemak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('criteria', models.CharField(max_length=10)),
                ('mark', models.CharField(max_length=10)),
                ('subIndicator', models.CharField(max_length=100)),
                ('prosedur', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='subIndikator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('subIndicator', models.CharField(max_length=100)),
                ('indicator', models.CharField(max_length=10)),
            ],
        ),
    ]
