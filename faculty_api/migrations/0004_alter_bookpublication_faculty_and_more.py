# Generated by Django 4.0.2 on 2022-02-15 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faculty_api', '0003_bookpublication_confrencepublication_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookpublication',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BookPublication', to='faculty_api.faculty'),
        ),
        migrations.AlterField(
            model_name='confrencepublication',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ConfrencePublication', to='faculty_api.faculty'),
        ),
        migrations.AlterField(
            model_name='journalpublication',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='JournalPublication', to='faculty_api.faculty'),
        ),
    ]