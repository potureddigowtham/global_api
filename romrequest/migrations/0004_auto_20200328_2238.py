# Generated by Django 3.0.3 on 2020-03-28 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('romrequest', '0003_auto_20200328_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='romrequest',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='romrequest',
            name='loction',
            field=models.CharField(choices=[('chennai', 'Chennai'), ('bangalore', 'Bangalore'), ('coimbatore', 'Coimbatore')], default='bangalore', max_length=30),
        ),
        migrations.AlterField(
            model_name='romrequest',
            name='sbu',
            field=models.CharField(choices=[('fluid', 'Fluid'), ('club car', 'Club Car'), ('cts', 'CTS'), ('power tools and lifting', 'Power Tools and Lifting')], default='cts', max_length=30),
        ),
    ]
