# Generated by Django 4.0.4 on 2022-05-05 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient_Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=50)),
                ('mobile_no', models.CharField(blank=True, max_length=20, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('years_diabetes', models.IntegerField()),
                ('submittedAt', models.DateTimeField()),
                ('ischecked', models.BooleanField(default=False)),
                ('leftRetina', models.ImageField(upload_to='images/')),
                ('rightRetina', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
