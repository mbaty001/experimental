# Generated by Django 3.2.7 on 2021-09-07 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cash', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='year',
            field=models.IntegerField(choices=[(2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021)], default=2021),
        ),
    ]