# Generated by Django 3.2.8 on 2021-12-14 03:15

from django.db import migrations, models
import service.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Academic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentid', models.IntegerField(db_column='StudentId')),
                ('school', models.CharField(db_column='School', max_length=45)),
                ('college', models.CharField(db_column='College', max_length=45)),
                ('ssc_o_level_gpa', models.FloatField(db_column='SSC/O_Level_GPA')),
                ('hsc_a_level_gpa', models.FloatField(db_column='HSC/A_Level_GPA')),
                ('dateofenrolling', models.DateField(blank=True, db_column='DateOfEnrolling', null=True)),
             
            ],
            options={
                'db_table': 'academic',
                'managed': False,
            },
        ),
       
        migrations.CreateModel(
            name='Course',
            fields=[
                ('coursecode', models.CharField(db_column='CourseCode', max_length=8, primary_key=True, serialize=False)),
                ('coursename', models.CharField(blank=True, db_column='CourseName', max_length=50, null=True)),
                ('credit', models.FloatField(db_column='Credit')),
            ],
            options={
                'db_table': 'course',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Financial',
            fields=[
                ('studentid', models.IntegerField(db_column='StudentId', primary_key=True, serialize=False)),
                ('payableamount', models.IntegerField(db_column='PayableAmount')),
                ('paidamount', models.IntegerField(blank=True, db_column='PaidAmount', null=True)),
                ('f_income', models.IntegerField(blank=True, db_column='F_Income', null=True)),
                ('m_income', models.IntegerField(blank=True, db_column='M_Income', null=True)),
            ],
            options={
                'db_table': 'financial',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('studentid', models.IntegerField(db_column='StudentId', primary_key=True, serialize=False)),
                ('semester', models.CharField(db_column='Semester', max_length=20)),
                ('coursecode', models.CharField(blank=True, db_column='CourseCode', max_length=100, null=True)),
                ('credit', models.FloatField(db_column='Credit')),
                ('course_grade', models.FloatField(db_column='Course_Grade')),
                ('cgpa', models.FloatField(db_column='CGPA')),
            ],
            options={
                'db_table': 'result',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('repassword', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'service_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('bin', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('organizationname', models.CharField(blank=True, max_length=20, null=True)),
                ('organizationtype', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.CharField(blank=True, max_length=20, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=service.models.filepath)),
                ('need_info', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item1',
            fields=[
                ('studentid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('studentname', models.CharField(max_length=50)),
                ('image', models.FileField(blank=True, null=True, upload_to=service.models.filepath)),
                ('age', models.CharField(max_length=2)),
                ('bloodgroup', models.CharField(max_length=3)),
                ('nid_no', models.CharField(max_length=17)),
                ('email', models.CharField(max_length=30)),
                ('fathername', models.CharField(max_length=50)),
                ('nid_no_of_father', models.CharField(max_length=17)),
                ('mothername', models.CharField(max_length=50)),
                ('nid_no_of_mother', models.CharField(max_length=17)),
            ],
        ),
    ]
