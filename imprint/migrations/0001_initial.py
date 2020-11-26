# Generated by Django 3.1.1 on 2020-11-24 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('num', models.IntegerField()),
                ('contact_back_img', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_image1', models.ImageField(upload_to='pics')),
                ('home_image2', models.ImageField(upload_to='pics')),
                ('home_desc1', models.TextField()),
                ('home_desc2', models.TextField()),
                ('home_good_experiance_image', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='Inspire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pics')),
                ('description', models.TextField()),
                ('desc_heading', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_heading', models.CharField(max_length=100)),
                ('course_price', models.IntegerField()),
                ('offer_percent', models.IntegerField()),
                ('register_before', models.CharField(max_length=100)),
                ('offer_price', models.IntegerField()),
                ('offer', models.BooleanField(default=False)),
                ('course_image', models.ImageField(upload_to='pics')),
                ('course_description', models.TextField()),
                ('price_back_img', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='Student_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Syas_about_us',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('Student_image', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_image', models.ImageField(upload_to='pics')),
                ('teacher_name', models.CharField(max_length=100)),
                ('teacher_subject', models.CharField(max_length=100)),
                ('teacher_info', models.CharField(max_length=100)),
                ('teacher_message', models.TextField()),
                ('teacher_back_img', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='Welcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('welcome_note', models.TextField()),
            ],
        ),
    ]