# Generated by Django 4.2.4 on 2024-03-10 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_answerform_nco_answer_form_question_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='content_tutorial',
            field=models.TextField(db_column='content_tutorial', default=''),
        ),
    ]
