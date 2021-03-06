# Generated by Django 2.0.1 on 2020-02-04 10:18

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_student', models.BooleanField(default=False)),
                ('is_organization', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GPA', models.FloatField(max_length=10.0)),
                ('dob', models.DateField()),
                ('state', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('gender', multiselectfield.db.fields.MultiSelectField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Non-Binary', 'Non-Binary')], max_length=22)),
                ('category', multiselectfield.db.fields.MultiSelectField(choices=[('Competitions', 'Competitions'), ('Conferences', 'Conferences'), ('Exchange-Programs', 'Exchange-Programs'), ('Fellowships', 'Fellowships'), ('Internships', 'Internships'), ('Scholarships', 'Scholarships'), ('Workshops', 'Workshops')], max_length=89, null=True)),
                ('qualification', multiselectfield.db.fields.MultiSelectField(choices=[('Post-Doctorate', 'Post-Doctorate'), ('Doctorate', 'Doctorate'), ('Masters', 'Masters'), ('Bachelors', 'Bachelors'), ('School', 'School')], max_length=49, null=True)),
                ('domain', multiselectfield.db.fields.MultiSelectField(choices=[('Engineering', 'Engineering'), ('Medicine', 'Medicine'), ('Management', 'Management'), ('Humanities', 'Humanities'), ('Science', 'Science')], max_length=50, null=True)),
            ],
        ),
    ]
