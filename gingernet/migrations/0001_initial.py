# Generated by Django 2.2.3 on 2020-06-25 04:49

import DjangoUeditor.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApiAuth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(default='', max_length=64, verbose_name='接入名称')),
                ('api_token', models.CharField(default='unknown', max_length=128, verbose_name='接入 api Token')),
                ('is_expire', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=128, verbose_name='Token是否过期')),
                ('status', models.CharField(choices=[('UnVerify', 'UnVerify'), ('Verifing', 'Verifing'), ('Verified', 'Verified')], default='checking', max_length=32, verbose_name='API 审核状态')),
            ],
            options={
                'verbose_name': 'API 授权表',
                'verbose_name_plural': 'API 授权表',
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('text_info', models.CharField(default='', max_length=50, verbose_name='banner 信息')),
                ('img', models.ImageField(upload_to='banner/', verbose_name='图片')),
                ('link_url', models.URLField(default='', max_length=100, verbose_name='url链接')),
                ('banner_mark', models.CharField(default='index', max_length=50, verbose_name='banner 标志')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否删除')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(default='', max_length=20, verbose_name='分类名称')),
                ('index', models.IntegerField(default=999, verbose_name='索引')),
                ('category_mark', models.CharField(default='', max_length=20, verbose_name='分类标志')),
            ],
            options={
                'verbose_name': '分类列表',
                'verbose_name_plural': '分类列表',
            },
        ),
        migrations.CreateModel(
            name='CompanyAdvantage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('title', models.CharField(max_length=70, verbose_name='标题')),
                ('excerpt', models.TextField(blank=True, default='', max_length=500, verbose_name='优势摘要')),
            ],
            options={
                'verbose_name': '公司优势',
                'verbose_name_plural': '公司优势',
            },
        ),
        migrations.CreateModel(
            name='CompanyIntro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(max_length=70, verbose_name='公司名字')),
                ('detail', DjangoUeditor.models.UEditorField(blank=True, verbose_name='公司详情')),
                ('is_del', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=16, verbose_name='是否删除')),
            ],
            options={
                'verbose_name': '公司介绍',
                'verbose_name_plural': '公司介绍',
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('qq', models.CharField(default='1294928442', max_length=70, verbose_name='QQ')),
                ('phone', models.CharField(default='13611267041', max_length=70, verbose_name='电话')),
                ('email', models.CharField(default='guoshijiang2012@163.com', max_length=70, verbose_name='邮箱')),
                ('img', models.ImageField(blank=True, null=True, upload_to='weima_img/%Y/%m/%d/', verbose_name='微信二维码')),
                ('is_del', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=16, verbose_name='是否删除')),
            ],
            options={
                'verbose_name': '联系我们',
                'verbose_name_plural': '联系我们',
            },
        ),
        migrations.CreateModel(
            name='Costomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(default='', max_length=70, verbose_name='名称')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='cos_logo/%Y/%m/%d/', verbose_name='Logo')),
                ('excerpt', models.TextField(blank=True, default='', max_length=200, verbose_name='摘要')),
                ('is_del', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=16, verbose_name='是否删除')),
            ],
            options={
                'verbose_name': '产品客户表',
                'verbose_name_plural': '产品客户表',
            },
        ),
        migrations.CreateModel(
            name='DevHis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('period', models.CharField(max_length=70, verbose_name='时间段')),
                ('detail', models.TextField(blank=True, default='', max_length=200, verbose_name='发展概述')),
                ('is_del', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=16, verbose_name='是否删除')),
            ],
            options={
                'verbose_name': '发展历程',
                'verbose_name_plural': '发展历程',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(default='', max_length=20, verbose_name='名字')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logo_img/%Y/%m/%d/', verbose_name='图片')),
                ('linkurl', models.URLField(default='', max_length=100, verbose_name='URL链接')),
            ],
            options={
                'verbose_name': '友情链接',
                'verbose_name_plural': '友情链接',
            },
        ),
        migrations.CreateModel(
            name='NavCat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(default='', max_length=20, verbose_name='导航名称')),
                ('nav_mark', models.CharField(default='', max_length=20, verbose_name='导航标志')),
            ],
            options={
                'verbose_name': '导航列表',
                'verbose_name_plural': '导航列表',
            },
        ),
        migrations.CreateModel(
            name='OnlineMsg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(max_length=70, verbose_name='姓名')),
                ('phone', models.CharField(max_length=70, verbose_name='电话')),
                ('email', models.CharField(max_length=70, verbose_name='邮箱')),
                ('content', models.TextField(blank=True, default='', max_length=500, verbose_name='留言内容')),
                ('is_handle', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=16, verbose_name='是否处理')),
                ('is_del', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=16, verbose_name='是否删除')),
            ],
            options={
                'verbose_name': '在线咨询',
                'verbose_name_plural': '在线咨询',
            },
        ),
        migrations.CreateModel(
            name='Partnet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(default='', max_length=70, verbose_name='名称')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='cos_logo/%Y/%m/%d/', verbose_name='Logo')),
                ('excerpt', models.TextField(blank=True, default='', max_length=200, verbose_name='摘要')),
                ('is_del', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=16, verbose_name='是否删除')),
            ],
            options={
                'verbose_name': '合作伙伴表',
                'verbose_name_plural': '合作伙伴表',
            },
        ),
        migrations.CreateModel(
            name='ProductAdvantage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(default='', max_length=70, verbose_name='名称')),
                ('excerpt', models.TextField(blank=True, default='', max_length=200, verbose_name='摘要')),
                ('is_del', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=16, verbose_name='是否删除')),
            ],
            options={
                'verbose_name': '产品优势表',
                'verbose_name_plural': '产品优势表',
            },
        ),
        migrations.CreateModel(
            name='ProductDocs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(default='', max_length=70, verbose_name='名称')),
                ('img', models.ImageField(blank=True, null=True, upload_to='docs_img/%Y/%m/%d/', verbose_name='图片')),
                ('excerpt', models.TextField(blank=True, default='', max_length=200, verbose_name='摘要')),
                ('detail', DjangoUeditor.models.UEditorField(blank=True, verbose_name='详情')),
                ('is_del', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=16, verbose_name='是否删除')),
            ],
            options={
                'verbose_name': '产品接口文档',
                'verbose_name_plural': '产品接口文档',
            },
        ),
        migrations.CreateModel(
            name='ProductFunc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(default='', max_length=70, verbose_name='产品名称')),
                ('excerpt', models.TextField(blank=True, default='', max_length=200, verbose_name='摘要')),
                ('is_del', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=16, verbose_name='是否删除')),
            ],
            options={
                'verbose_name': '产品功能表',
                'verbose_name_plural': '产品功能表',
            },
        ),
        migrations.CreateModel(
            name='TechTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(max_length=70, verbose_name='团队名字')),
                ('detail', DjangoUeditor.models.UEditorField(blank=True, verbose_name='团队详情')),
                ('is_del', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=16, verbose_name='是否删除')),
            ],
            options={
                'verbose_name': '技术团队',
                'verbose_name_plural': '技术团队',
            },
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(default='', max_length=70, verbose_name='方案名称')),
                ('excerpt', models.TextField(blank=True, default='', max_length=200, verbose_name='方案摘要')),
                ('img', models.ImageField(blank=True, null=True, upload_to='solution_img/%Y/%m/%d/', verbose_name='方案图片')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='方案查看次数')),
                ('detail', DjangoUeditor.models.UEditorField(blank=True, verbose_name='方案详情')),
                ('is_del', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=16, verbose_name='是否删除')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='solution_category', to='gingernet.Category', verbose_name='方案分类')),
            ],
            options={
                'verbose_name': '解决方案表',
                'verbose_name_plural': '解决方案表',
            },
        ),
        migrations.CreateModel(
            name='Research',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(default='', max_length=70, verbose_name='研究标题')),
                ('excerpt', models.TextField(blank=True, default='', max_length=200, verbose_name='研究摘要')),
                ('img', models.ImageField(blank=True, null=True, upload_to='solution_img/%Y/%m/%d/', verbose_name='研究图片')),
                ('pdf_file', models.FileField(blank=True, null=True, upload_to='pdf_file/%Y/%m/%d/', verbose_name='pdf文件')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='研究内容查看次数')),
                ('detail', DjangoUeditor.models.UEditorField(blank=True, verbose_name='研究内容')),
                ('is_del', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=16, verbose_name='是否删除')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='research_category', to='gingernet.Category', verbose_name='研究分类')),
            ],
            options={
                'verbose_name': '研究中心表',
                'verbose_name_plural': '研究中心表',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(default='', max_length=70, verbose_name='产品名称')),
                ('excerpt', models.TextField(blank=True, default='', max_length=200, verbose_name='摘要')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='product_icon/%Y/%m/%d/', verbose_name='图片')),
                ('img', models.ImageField(blank=True, null=True, upload_to='product_img/%Y/%m/%d/', verbose_name='图片')),
                ('views', models.PositiveIntegerField(default=0)),
                ('detail', DjangoUeditor.models.UEditorField(blank=True, verbose_name='详情')),
                ('product_cat', models.CharField(choices=[('blockchain', 'blockchain'), ('other', 'other')], default='blockchain', max_length=70, verbose_name='产品名称')),
                ('is_del', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=16, verbose_name='是否删除')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='product_category', to='gingernet.Category', verbose_name='分类')),
                ('product_adv', models.ManyToManyField(blank=True, null=True, to='gingernet.ProductAdvantage', verbose_name='产品优势')),
                ('product_cos', models.ManyToManyField(blank=True, null=True, to='gingernet.Costomer', verbose_name='客户案例')),
                ('product_doc', models.ManyToManyField(blank=True, null=True, to='gingernet.ProductDocs', verbose_name='产品文档')),
                ('product_func', models.ManyToManyField(blank=True, null=True, to='gingernet.ProductFunc', verbose_name='产品功能')),
            ],
            options={
                'verbose_name': '产品列表',
                'verbose_name_plural': '产品列表',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('title', models.CharField(max_length=70, verbose_name='标题')),
                ('excerpt', models.TextField(blank=True, default='', max_length=200, verbose_name='咨询摘要')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='news_icon/%Y/%m/%d/', verbose_name='新闻封面')),
                ('img', models.ImageField(blank=True, null=True, upload_to='news_img/%Y/%m/%d/', verbose_name='新闻封面')),
                ('body', DjangoUeditor.models.UEditorField(blank=True, verbose_name='新闻内容')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='查看次数')),
                ('author', models.CharField(default='知鱼定制', max_length=70, verbose_name='作者')),
                ('is_del', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=16, verbose_name='是否删除')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='news_category', to='gingernet.Category', verbose_name='类别')),
            ],
            options={
                'verbose_name': '新闻管理',
                'verbose_name_plural': '新闻管理',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='nav_cat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='nav_category', to='gingernet.NavCat', verbose_name='类别导航'),
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('title', models.CharField(default='', max_length=70, verbose_name='案例标题')),
                ('img', models.ImageField(blank=True, null=True, upload_to='case_img/%Y/%m/%d/', verbose_name='案例图片')),
                ('body', DjangoUeditor.models.UEditorField(blank=True, verbose_name='案例内容')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='案例查看次数')),
                ('is_del', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=16, verbose_name='是否删除')),
                ('nav_cat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gingernet.NavCat', verbose_name='案例分类')),
            ],
            options={
                'verbose_name': '客户案例',
                'verbose_name_plural': '客户案例',
            },
        ),
    ]
