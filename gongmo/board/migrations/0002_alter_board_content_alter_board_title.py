# Generated by Django 4.1.3 on 2022-11-18 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="board",
            name="content",
            field=models.TextField(verbose_name="카카오톡 오픈 채팅방 url"),
        ),
        migrations.AlterField(
            model_name="board",
            name="title",
            field=models.CharField(max_length=20, verbose_name="공모전 이름& 구인인원"),
        ),
    ]
