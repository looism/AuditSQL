# Generated by Django 2.0.2 on 2018-08-15 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuditContents',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键id')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('url', models.CharField(default='', max_length=1024, verbose_name='上线的Confluence链接')),
                ('operate_type', models.CharField(choices=[('DDL', '数据库定义语言'), ('DML', '数据库操纵语言')], default='DML', max_length=5, verbose_name='操作类型: DDL or DML')),
                ('envi_desc', models.SmallIntegerField(default=0, verbose_name='环境：0：M1、1：staging、2：生产、3：线下其他环境')),
                ('proposer', models.CharField(default='', max_length=30, verbose_name='申请人， 一般为开发或者产品，存储username')),
                ('operator', models.CharField(default='', max_length=30, verbose_name='审核DBA')),
                ('operate_time', models.DateTimeField(auto_now_add=True, verbose_name='审核时间')),
                ('host', models.CharField(default='', max_length=30, verbose_name='操作数据库主机')),
                ('database', models.CharField(default='', max_length=80, verbose_name='操作数据库')),
                ('port', models.IntegerField(default=3306, verbose_name='端口')),
                ('progress', models.CharField(choices=[('0', '待批准'), ('1', '未批准'), ('2', '已批准'), ('3', '处理中'), ('4', '已完成'), ('5', '已关闭'), ('6', '已勾住')], default='0', max_length=10, verbose_name='任务进度')),
                ('remark', models.SmallIntegerField(default=0, verbose_name='工单备注, 0: 周三上线，1：紧急上线，2：数据修复')),
                ('tasks', models.CharField(default='', max_length=256, verbose_name='部署步骤版本')),
                ('close_user', models.CharField(default='', max_length=30, verbose_name='关闭记录的用户')),
                ('close_reason', models.CharField(default='', max_length=1024, verbose_name='关闭原因')),
                ('close_time', models.DateTimeField(auto_now_add=True, verbose_name='关闭时间')),
                ('contents', models.TextField(default='', verbose_name='提交的内容')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '审核内容',
                'verbose_name_plural': '审核内容',
                'db_table': 'auditsql_work_order',
            },
        ),
        migrations.CreateModel(
            name='AuditTasks',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键id')),
                ('username', models.CharField(default='', max_length=128, verbose_name='创建用户')),
                ('tasks', models.CharField(default='', max_length=128, verbose_name='任务名')),
                ('expire_time', models.DateTimeField(default='2000-11-01 01:01:01', verbose_name='任务截止上线日期')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '审核任务',
                'verbose_name_plural': '审核任务',
                'db_table': 'auditsql_audit_tasks',
            },
        ),
        migrations.CreateModel(
            name='DomainName',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键id')),
                ('domain_name', models.CharField(default='', max_length=256, verbose_name='域名地址')),
            ],
            options={
                'verbose_name': '域名地址',
                'verbose_name_plural': '域名地址',
                'db_table': 'auditsql_domain_name',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='IncepMakeExecTask',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键id')),
                ('uid', models.IntegerField(default=0, verbose_name='操作用户uid')),
                ('user', models.CharField(max_length=30, verbose_name='操作用户')),
                ('taskid', models.CharField(max_length=128, verbose_name='任务号')),
                ('related_id', models.IntegerField(default=0, verbose_name='关联AuditContents的主键id')),
                ('envi_desc', models.SmallIntegerField(default=0, verbose_name='环境：0：M1、1：staging、2：生产、3：线下其他环境')),
                ('dst_host', models.CharField(max_length=30, verbose_name='操作目标数据库主机')),
                ('dst_database', models.CharField(max_length=80, verbose_name='操作目标数据库')),
                ('dst_port', models.IntegerField(default=3306, verbose_name='端口')),
                ('sql_content', models.TextField(default='', verbose_name='执行的SQL')),
                ('type', models.CharField(choices=[('DDL', '数据库定义语言'), ('DML', '数据库操纵语言')], default='', max_length=5)),
                ('sqlsha1', models.CharField(default='', max_length=120, verbose_name='sqlsha1')),
                ('rollback_sqlsha1', models.CharField(default='', max_length=120, verbose_name='rollback sqlsha1')),
                ('celery_task_id', models.CharField(default='', max_length=256, verbose_name='celery执行任务ID')),
                ('exec_status', models.CharField(choices=[('0', '未执行'), ('1', '已完成'), ('2', '处理中'), ('3', '回滚中'), ('4', '已回滚'), ('5', '失败'), ('6', '异常')], default='0', max_length=10, verbose_name='执行进度')),
                ('sequence', models.CharField(default='', max_length=1024, verbose_name='备份记录id，inception生成的sequence')),
                ('affected_row', models.IntegerField(default=0, verbose_name='预计影响行数')),
                ('backup_dbname', models.CharField(default='', max_length=1024, verbose_name='inception生成的备份的库名')),
                ('exec_log', models.TextField(default='', verbose_name='执行成功的记录')),
                ('make_time', models.DateTimeField(auto_now_add=True, verbose_name='生成时间')),
            ],
            options={
                'verbose_name': '生成Inception执行任务',
                'verbose_name_plural': '生成Inception执行任务',
                'db_table': 'auditsql_incep_tasks',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='MonitorSchema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_schema', models.CharField(max_length=512)),
                ('table_name', models.CharField(max_length=512)),
                ('table_stru', models.TextField(default='')),
                ('md5_sum', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': '监控表结构变更表',
                'verbose_name_plural': '监控表结构变更表',
                'db_table': 'auditsql_monitor_schema',
                'permissions': (),
            },
        ),
        migrations.CreateModel(
            name='OlAuditContentsReply',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键')),
                ('reply_contents', models.TextField(default='', verbose_name='回复内容')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='回复时间')),
                ('reply', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='project_manager.AuditContents')),
            ],
            options={
                'verbose_name': '线上审核回复表',
                'verbose_name_plural': '线上审核回复表',
                'db_table': 'auditsql_work_order_reply',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Webhook',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键id')),
                ('webhook_addr', models.CharField(default='', max_length=256, verbose_name='webhook地址')),
            ],
            options={
                'verbose_name': '钉钉机器人',
                'verbose_name_plural': '钉钉机器人',
                'db_table': 'auditsql_webhook',
                'default_permissions': (),
            },
        ),
    ]
