# # Generated by Django 3.1.12 on 2024-12-31 15:13
#
# from django.db import migrations, models
#
#
# class Migration(migrations.Migration):
#
#     dependencies = [
#         ('bbdmsapp', '0007_donorreg_status_alter_customuser_user_type'),
#     ]
#
#     operations = [
#         migrations.AddField(
#             model_name='customuser',
#             name='email_verified',
#             field=models.BooleanField(default=False),
#         ),
#         migrations.AlterField(
#             model_name='bloodgroup',
#             name='id',
#             field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
#         ),
#         migrations.AlterField(
#             model_name='bloodrequest',
#             name='id',
#             field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
#         ),
#         migrations.AlterField(
#             model_name='contact',
#             name='id',
#             field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
#         ),
#         migrations.AlterField(
#             model_name='customuser',
#             name='id',
#             field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
#         ),
#         migrations.AlterField(
#             model_name='customuser',
#             name='profile_pic',
#             field=models.ImageField(blank=True, null=True, upload_to='media/profile_pic'),
#         ),
#         migrations.AlterField(
#             model_name='customuser',
#             name='user_type',
#             field=models.CharField(choices=[(2, 'donor'), (1, 'admin'), (3, 'requester')], default=1, max_length=50),
#         ),
#         migrations.AlterField(
#             model_name='donorreg',
#             name='id',
#             field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
#         ),
#     ]

# Generated by Django 3.1.12 on 2024-12-31 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbdmsapp', '0007_donorreg_status_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='email_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='media/profile_pic'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(2, 'donor'), (1, 'admin'), (3, 'requester')], default=1, max_length=50),
        ),
    ]
