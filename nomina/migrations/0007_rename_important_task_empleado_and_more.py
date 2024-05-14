# Generated by Django 5.0.6 on 2024-05-13 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomina', '0006_delete_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='important',
            new_name='empleado',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='title',
            new_name='usuario',
        ),
        migrations.RemoveField(
            model_name='task',
            name='datecompleted',
        ),
        migrations.RemoveField(
            model_name='task',
            name='description',
        ),
        migrations.AddField(
            model_name='task',
            name='apellido',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='task',
            name='email',
            field=models.EmailField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='task',
            name='nombre',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
