# Generated by Django 2.1.2 on 2018-12-12 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chaos_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relation',
            name='friend_a',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friends_b', to='chaos_app.Person'),
        ),
        migrations.AlterField(
            model_name='relation',
            name='friend_b',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friends_a', to='chaos_app.Person'),
        ),
    ]