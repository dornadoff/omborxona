# Generated by Django 4.1.7 on 2023-02-24 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ombor', '0003_rename_ombot_mahsulot_ombor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistika',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miqdor', models.PositiveIntegerField()),
                ('sana', models.DateTimeField(auto_now_add=True)),
                ('umumiy_summa', models.PositiveBigIntegerField()),
                ('tolandi', models.PositiveBigIntegerField()),
                ('nasiya', models.PositiveBigIntegerField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ombor.client')),
                ('mahsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ombor.mahsulot')),
            ],
        ),
    ]
