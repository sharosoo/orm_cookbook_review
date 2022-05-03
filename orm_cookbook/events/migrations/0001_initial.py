# Generated by Django 3.2 on 2022-05-03 01:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('entities', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TempUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'temp_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ColumnName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.CharField(db_column='column1', max_length=40)),
                ('column2', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Epic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('participating_heroes', models.ManyToManyField(to='entities.Hero')),
                ('participating_villains', models.ManyToManyField(to='entities.Villain')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('details', models.TextField()),
                ('years_ago', models.PositiveIntegerField()),
                ('epic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.epic')),
            ],
        ),
        migrations.CreateModel(
            name='UserParent',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('father_name', models.CharField(max_length=100)),
                ('mother_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EventVillain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_primary', models.BooleanField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entities.villain')),
            ],
        ),
        migrations.CreateModel(
            name='EventHero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_primary', models.BooleanField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entities.hero')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
                ('pub_date', models.DateField()),
                ('slug', models.SlugField()),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reporter', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('headline',),
            },
        ),
    ]
