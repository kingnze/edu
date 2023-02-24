# Generated by Django 4.1.7 on 2023-02-24 13:20

import ckeditor.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=200)),
                ('lname', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'Contacts',
                'verbose_name_plural': 'Contacts',
                'db_table': 'contact',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=550)),
                ('slug', models.SlugField(blank=True, max_length=550, null=True)),
                ('published', models.BooleanField(blank=True, default=True, null=True)),
                ('flag', models.BooleanField(blank=True, default=False, null=True)),
                ('date_posted', models.DateTimeField(default=datetime.datetime(2023, 2, 24, 14, 20, 25, 919953))),
                ('body', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Discipline',
                'verbose_name_plural': 'Discipline',
                'db_table': 'Discipline',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Dressing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=550)),
                ('slug', models.SlugField(blank=True, max_length=550, null=True)),
                ('published', models.BooleanField(blank=True, default=True, null=True)),
                ('flag', models.BooleanField(blank=True, default=False, null=True)),
                ('date_posted', models.DateTimeField(default=datetime.datetime(2023, 2, 24, 14, 20, 25, 914959))),
                ('body', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Dressing',
                'verbose_name_plural': 'Dressing',
                'db_table': 'Dressing',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Facilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=550)),
                ('leadimg', models.ImageField(default='myleadimg.jpg', upload_to='')),
                ('published', models.BooleanField(default=True)),
                ('flag', models.BooleanField(default=False)),
                ('date_posted', models.DateTimeField(default=datetime.datetime(2023, 2, 24, 14, 20, 25, 914959))),
            ],
            options={
                'verbose_name': 'Facilities',
                'verbose_name_plural': 'Facilities',
                'db_table': 'Facilities',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=550)),
                ('slug', models.SlugField(blank=True, max_length=550, null=True)),
                ('leadimg', models.ImageField(default='myleadimg.jpg', upload_to='')),
                ('published', models.BooleanField(default=True)),
                ('flag', models.BooleanField(default=False)),
                ('date_posted', models.DateTimeField(default=datetime.datetime(2023, 2, 24, 14, 20, 25, 919953))),
            ],
            options={
                'verbose_name': 'Gallery',
                'verbose_name_plural': 'Gallery',
                'db_table': 'Gallery',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=550)),
                ('slug', models.SlugField(blank=True, max_length=550, null=True)),
                ('published', models.BooleanField(blank=True, default=True, null=True)),
                ('flag', models.BooleanField(blank=True, default=False, null=True)),
                ('date_posted', models.DateTimeField(default=datetime.datetime(2023, 2, 24, 14, 20, 25, 914959))),
                ('leadimg', models.ImageField(default='myleadimg.jpg', upload_to='')),
                ('body', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'History',
                'verbose_name_plural': 'History',
                'db_table': 'History',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=550)),
                ('position', models.CharField(max_length=550)),
                ('leadimg', models.ImageField(default='myleadimg.jpg', upload_to='')),
                ('published', models.BooleanField(blank=True, default=True, null=True)),
                ('flag', models.BooleanField(blank=True, default=False, null=True)),
                ('date_posted', models.DateTimeField(default=datetime.datetime(2023, 2, 24, 14, 20, 25, 914959))),
            ],
            options={
                'verbose_name': 'Management',
                'verbose_name_plural': 'Management',
                'db_table': 'Management',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Staffmembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=550)),
                ('position', models.CharField(max_length=550)),
                ('leadimg', models.ImageField(default='myleadimg.jpg', upload_to='')),
                ('published', models.BooleanField(blank=True, default=True, null=True)),
                ('flag', models.BooleanField(blank=True, default=False, null=True)),
                ('date_posted', models.DateTimeField(default=datetime.datetime(2023, 2, 24, 14, 20, 25, 914959))),
            ],
            options={
                'verbose_name': 'Staffmembers',
                'verbose_name_plural': 'Staffmembers',
                'db_table': 'Staffmembers',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countnumber', models.CharField(max_length=550)),
                ('counttext', models.CharField(max_length=550)),
                ('countnumber1', models.CharField(blank=True, max_length=550, null=True)),
                ('counttext1', models.CharField(blank=True, max_length=550, null=True)),
                ('countnumber2', models.CharField(blank=True, max_length=550, null=True)),
                ('counttext2', models.CharField(blank=True, max_length=550, null=True)),
                ('countnumber3', models.CharField(blank=True, max_length=550, null=True)),
                ('counttext3', models.CharField(blank=True, max_length=550, null=True)),
            ],
            options={
                'verbose_name': 'Stats',
                'verbose_name_plural': 'Stats',
                'db_table': 'Stats',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('indentity', models.CharField(blank=True, max_length=500, null=True)),
                ('leadimg', models.ImageField(default='myleadimg.jpg', upload_to='')),
                ('body', models.TextField()),
                ('date_posted', models.DateTimeField(default=datetime.datetime(2023, 2, 24, 14, 20, 25, 919953))),
                ('published', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Testimonials',
                'verbose_name_plural': 'Testimonials',
                'db_table': 'Testimonial',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=550)),
                ('slug', models.SlugField(blank=True, max_length=550, null=True)),
                ('published', models.BooleanField(blank=True, default=True, null=True)),
                ('flag', models.BooleanField(blank=True, default=False, null=True)),
                ('date_posted', models.DateTimeField(default=datetime.datetime(2023, 2, 24, 14, 20, 25, 919953))),
                ('body', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'TimeTable',
                'verbose_name_plural': 'TimeTable',
                'db_table': 'TimeTable',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TuitionAndPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=550)),
                ('slug', models.SlugField(blank=True, max_length=550, null=True)),
                ('published', models.BooleanField(blank=True, default=True, null=True)),
                ('flag', models.BooleanField(blank=True, default=False, null=True)),
                ('date_posted', models.DateTimeField(default=datetime.datetime(2023, 2, 24, 14, 20, 25, 919953))),
                ('body', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'TuitionAndPayment',
                'verbose_name_plural': 'TuitionAndPayment',
                'db_table': 'TuitionAndPayment',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Ourservice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=550)),
                ('slug', models.SlugField(blank=True, max_length=550, null=True)),
                ('published', models.BooleanField(blank=True, default=True, null=True)),
                ('flag', models.BooleanField(blank=True, default=False, null=True)),
                ('date_posted', models.DateTimeField(default=datetime.datetime(2023, 2, 24, 14, 20, 25, 914959))),
                ('leadimg', models.ImageField(default='myleadimg.jpg', upload_to='')),
                ('body', ckeditor.fields.RichTextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Ourservice',
                'verbose_name_plural': 'Ourservice',
                'db_table': 'Ourservice',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=550)),
                ('slug', models.SlugField(blank=True, max_length=550, null=True)),
                ('published', models.BooleanField(blank=True, default=True, null=True)),
                ('flag', models.BooleanField(blank=True, default=False, null=True)),
                ('date_posted', models.DateTimeField(default=datetime.datetime(2023, 2, 24, 14, 20, 25, 919953))),
                ('leadimg', models.ImageField(default='myleadimg.jpg', upload_to='')),
                ('leadimg1', models.ImageField(blank=True, null=True, upload_to='')),
                ('body', ckeditor.fields.RichTextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blog',
                'db_table': 'Blog',
                'managed': True,
            },
        ),
    ]
