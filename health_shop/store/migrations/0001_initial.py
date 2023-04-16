# Generated by Django 2.2.1 on 2022-07-15 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auth_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=300)),
                ('photo', models.ImageField(default='user_profile/default.png', upload_to='user_profile')),
            ],
        ),
    ]