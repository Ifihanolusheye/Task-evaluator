# Generated by Django 2.0.1 on 2020-03-18 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(choices=[('January', 'Jan'), ('February', 'Feb'), ('March', 'Mar'), ('April', 'Apr'), ('May', 'May'), ('June', 'Jun'), ('July', 'Jul'), ('August', 'Aug'), ('September', 'Sep'), ('October', 'Oct'), ('November', 'Nov'), ('December', 'Dec')], max_length=3)),
                ('Score', models.IntegerField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.Company')),
            ],
        ),
    ]
