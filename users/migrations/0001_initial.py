# Generated by Django 2.2.7 on 2019-12-01 17:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import users.kmodels.image_model
import users.kmodels.user_model


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line_1', models.CharField(default='', max_length=50)),
                ('address_line_2', models.CharField(max_length=50, null=True)),
                ('landmark', models.CharField(max_length=50, null=True)),
                ('postalCode', models.IntegerField(null=True)),
                ('latitude', models.FloatField(max_length=20, null=True)),
                ('longitude', models.FloatField(max_length=20, null=True)),
                ('geoAddress', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=25, null=True)),
                ('state', models.CharField(max_length=25, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
            options={
                'verbose_name': 'Knit Address',
                'verbose_name_plural': 'Knit Addresses',
                'db_table': 'knit_address',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='KImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, max_length=254, null=True, upload_to=users.kmodels.image_model.nameFile)),
                ('source', models.CharField(blank=True, default='customer', max_length=50, null=True)),
                ('size', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'db_table': 'knit_image',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='KUserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(default=None, max_length=80, null=True)),
                ('description', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'verbose_name': 'Knit User type',
                'verbose_name_plural': 'Knit User types',
                'db_table': 'knit_user_type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('userName', models.CharField(max_length=50, unique=True, verbose_name='User Name')),
                ('phone', models.CharField(max_length=50, unique=True, verbose_name='Phone Number')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email Address')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('user_role', models.CharField(choices=[('USER', 'USER'), ('ADMIN', 'ADMIN'), ('LEADER', 'LEADER'), ('SUPER_ADMIN', 'SUPER ADMIN'), ('GUEST', 'GUEST'), ('DEL_BOY', 'DELIVERY BOY')], default='GUEST', max_length=80)),
                ('is_admin', models.IntegerField(default=False)),
                ('is_active', models.IntegerField(default=False)),
                ('images', models.ManyToManyField(blank=True, default=None, null=True, to='users.KImage')),
                ('user_type', models.ManyToManyField(blank=True, default=None, null=True, to='users.KUserType')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'db_table': 'user',
                'managed': True,
            },
            managers=[
                ('objects', users.kmodels.user_model.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='KVendorUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=80, null=True)),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('end_time', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('masters_count', models.IntegerField(blank=True, default=None, null=True)),
                ('is_weekends', models.BooleanField(blank=True, default=False, null=True)),
                ('is_weekdays', models.BooleanField(blank=True, default=True, null=True)),
                ('alternate_days', models.CharField(blank=True, max_length=20, null=True)),
                ('is_open', models.BooleanField(default=False)),
                ('is_emergency_available', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('address', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.KAddress')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
            options={
                'db_table': 'knit_vendor_user',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='KCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=80, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('address', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.KAddress')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
            options={
                'verbose_name': 'Knit Customer',
                'verbose_name_plural': 'Knit Customers',
                'db_table': 'knit_customer',
                'managed': True,
            },
        ),
    ]
