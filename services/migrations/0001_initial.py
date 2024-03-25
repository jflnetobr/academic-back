# Generated by Django 4.2.4 on 2024-03-25 00:54

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('dt_created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('dt_updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('dt_deleted_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('co_form', models.AutoField(db_column='co_formulario', primary_key=True, serialize=False, unique=True)),
                ('no_form', models.CharField(db_column='no_formulario', max_length=255)),
                ('ds_form', models.TextField(db_column='ds_formulario')),
                ('nco_step', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), db_column='nco_etapa_formulario', size=None)),
                ('nco_status', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), db_column='nco_status_formulario', size=None)),
            ],
            options={
                'db_table': 'tb_formulario',
            },
        ),
        migrations.CreateModel(
            name='FormItem',
            fields=[
                ('dt_created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('dt_updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('dt_deleted_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('co_form_item', models.AutoField(db_column='co_item_formulario', primary_key=True, serialize=False, unique=True)),
                ('ds_item', models.TextField(db_column='ds_item')),
            ],
            options={
                'db_table': 'tb_item_formulario',
            },
        ),
        migrations.CreateModel(
            name='FormQuestion',
            fields=[
                ('dt_created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('dt_updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('dt_deleted_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('co_form_question', models.AutoField(db_column='co_pergunta_formulario', primary_key=True, serialize=False, unique=True)),
                ('no_question', models.CharField(db_column='no_titulo_pergunta', max_length=255)),
                ('ds_question', models.TextField(db_column='ds_pergunta')),
                ('co_type_question', models.TextField(db_column='ds_tipo_pergunta')),
                ('nco_form_item', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, db_column='nco_item_formulario', null=True, size=None)),
            ],
            options={
                'db_table': 'tb_pergunta_formulario',
            },
        ),
        migrations.CreateModel(
            name='FormStep',
            fields=[
                ('dt_created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('dt_updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('dt_deleted_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('co_form_step', models.AutoField(db_column='co_etapa_formulario', primary_key=True, serialize=False, unique=True)),
                ('no_form_step', models.CharField(db_column='no_etapa_formulario', max_length=255)),
                ('ds_form_step', models.TextField(db_column='ds_etapa_formulario')),
                ('nco_form_question', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), db_column='nco_pergunta_formulario', size=None)),
            ],
            options={
                'db_table': 'tb_etapa_formulario',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('dt_created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('dt_updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('dt_deleted_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('co_news', models.AutoField(db_column='co_noticia', primary_key=True, serialize=False, unique=True)),
                ('no_news', models.CharField(db_column='no_titulo_noticia', max_length=255)),
                ('ds_news', models.TextField(db_column='ds_noticia')),
                ('dt_news', models.DateField(db_column='dt_noticia')),
            ],
            options={
                'db_table': 'tb_noticia',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('dt_created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('dt_updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('dt_deleted_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('co_notification', models.AutoField(db_column='co_notificacao', primary_key=True, serialize=False, unique=True)),
                ('ds_notification', models.TextField(db_column='ds_notificacao')),
                ('co_status', models.IntegerField(db_column='co_status')),
                ('ds_link', models.TextField(blank=True, db_column='ds_link', null=True)),
                ('nco_user', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), db_column='nco_usuario', size=None)),
            ],
            options={
                'db_table': 'tb_notificacao',
            },
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('dt_created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('dt_updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('dt_deleted_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('co_tutorial', models.AutoField(db_column='co_tutorial', primary_key=True, serialize=False, unique=True)),
                ('no_tutorial', models.CharField(db_column='no_titulo_tutorial', max_length=255)),
                ('ds_tutorial', models.TextField(db_column='ds_tutorial')),
                ('content_tutorial', models.TextField(db_column='content_tutorial', default='')),
            ],
            options={
                'db_table': 'tb_tutorial',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('dt_created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('dt_updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('dt_deleted_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('co_user', models.AutoField(db_column='co_usuario', primary_key=True, serialize=False, unique=True)),
                ('no_user', models.CharField(db_column='no_usuario', max_length=255)),
                ('co_registration', models.CharField(blank=True, db_column='co_matricula', max_length=100)),
                ('co_profile', models.IntegerField(db_column='co_tipo_perfil')),
                ('ds_email', models.CharField(db_column='ds_email', max_length=255)),
                ('ds_password', models.CharField(blank=True, db_column='ds_senha', max_length=255)),
                ('ds_phone', models.CharField(blank=True, db_column='ds_telefone', max_length=255)),
            ],
            options={
                'db_table': 'tb_usuario',
            },
        ),
        migrations.CreateModel(
            name='Solicitation',
            fields=[
                ('dt_created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('dt_updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('dt_deleted_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('co_solicitation', models.AutoField(db_column='co_solicitacao', primary_key=True, serialize=False)),
                ('co_status', models.IntegerField(db_column='co_status')),
                ('nco_answer_form_question', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, db_column='nco_resposta_questao_formulario', null=True, size=None)),
                ('co_form', models.ForeignKey(db_column='co_formulario', on_delete=django.db.models.deletion.CASCADE, to='services.form')),
                ('co_user', models.ForeignKey(db_column='co_usuario', on_delete=django.db.models.deletion.CASCADE, to='services.user')),
            ],
            options={
                'db_table': 'tb_solicitacao',
            },
        ),
        migrations.CreateModel(
            name='MessageForm',
            fields=[
                ('dt_created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('dt_updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('dt_deleted_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('co_message_form', models.AutoField(db_column='co_mensagem_formulario', primary_key=True, serialize=False, unique=True)),
                ('ds_message', models.TextField(db_column='ds_conteudo_mensagem')),
                ('co_solicitation', models.ForeignKey(db_column='co_solicitacao', on_delete=django.db.models.deletion.CASCADE, to='services.solicitation')),
            ],
            options={
                'db_table': 'tb_mensagem_formulario',
            },
        ),
        migrations.CreateModel(
            name='AnswerFormQuestion',
            fields=[
                ('dt_created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('dt_updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('dt_deleted_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('co_answer_form_question', models.AutoField(db_column='co_pergunta_resposta_formulario', primary_key=True, serialize=False, unique=True)),
                ('nds_answer_question_item', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, db_column='ds_resposta_questao_item', null=True, size=None)),
                ('nds_answer_question_str', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, db_column='ds_resposta_questao_str', null=True, size=None)),
                ('co_form_question', models.ForeignKey(db_column='co_pergunta_formulario', on_delete=django.db.models.deletion.CASCADE, to='services.formquestion')),
                ('co_solicitation', models.ForeignKey(db_column='co_solicitacao', on_delete=django.db.models.deletion.CASCADE, to='services.solicitation')),
            ],
            options={
                'db_table': 'tb_pergunta_resposta_formulario',
            },
        ),
    ]
