# Generated by Django 2.2.5 on 2022-06-05 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AgiletaskTracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='card_type',
            field=models.CharField(choices=[('feature', 'feature'), ('issue', 'issue')], default='feature', max_length=100),
        ),
        migrations.AlterField(
            model_name='card',
            name='priority',
            field=models.CharField(choices=[('low', 'low'), ('medium', 'medium'), ('high', 'high')], max_length=100),
        ),
        migrations.AlterField(
            model_name='card',
            name='status',
            field=models.CharField(choices=[('Todo', 'Todo'), ('inProgress', 'inProgress'), ('inreview', 'inreview'), ('closed', 'closed')], max_length=100),
        ),
    ]