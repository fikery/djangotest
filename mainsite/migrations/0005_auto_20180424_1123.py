# Generated by Django 2.0.4 on 2018-04-24 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0004_auto_20180419_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=10, verbose_name='状态')),
            ],
        ),
        migrations.CreateModel(
            name='MPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(default='佚名', max_length=10, verbose_name='昵称')),
                ('message', models.TextField(verbose_name='内容')),
                ('del_pass', models.CharField(max_length=10)),
                ('pub_time', models.DateTimeField(auto_now=True)),
                ('enabled', models.BooleanField(default=False)),
                ('mood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.Mood')),
            ],
        ),
        migrations.AlterField(
            model_name='pproduct',
            name='description',
            field=models.TextField(default='暂无', verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='pproduct',
            name='nickname',
            field=models.CharField(default='华为p20', max_length=20, verbose_name='简称'),
        ),
        migrations.AlterField(
            model_name='pproduct',
            name='pmodel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.PModel', verbose_name='型号'),
        ),
        migrations.AlterField(
            model_name='pproduct',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='价格'),
        ),
        migrations.AlterField(
            model_name='pproduct',
            name='year',
            field=models.PositiveIntegerField(default=2018, verbose_name='出厂年份'),
        ),
    ]
