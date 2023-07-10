# Generated by Django 3.2.19 on 2023-05-21 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='用户名')),
                ('password', models.CharField(max_length=50, verbose_name='密码')),
                ('employee_id', models.CharField(max_length=11, verbose_name='工号')),
                ('real_name', models.CharField(max_length=50, verbose_name='姓名')),
                ('gender', models.CharField(choices=[('M', '男'), ('F', '女')], max_length=1)),
                ('age', models.PositiveIntegerField()),
                ('identity', models.CharField(choices=[('S', '超级管理员'), ('N', '普通管理员')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=13, unique=True, verbose_name='ISBN')),
                ('title', models.CharField(max_length=50, verbose_name='书名')),
                ('publisher', models.CharField(blank=True, max_length=50, null=True, verbose_name='出版社')),
                ('author', models.CharField(max_length=50, verbose_name='作者')),
                ('retail_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FinancialBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('I', '收入'), ('O', '支出')], max_length=1, verbose_name='类型')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='金额')),
                ('date', models.DateField(verbose_name='日期')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='进货价格')),
                ('amount', models.PositiveBigIntegerField()),
                ('state', models.CharField(choices=[('未付款', '未付款'), ('已付款', '已付款'), ('已退货', '已退货')], max_length=6)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.bookinfo')),
            ],
        ),
    ]