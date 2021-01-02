# Generated by Django 3.1.4 on 2021-01-02 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('todo', 'Todo'), ('in progress', 'In progress'), ('done', 'Done')], default='todo', max_length=16)),
            ],
        ),
    ]
