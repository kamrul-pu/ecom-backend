# Generated by Django 4.2.6 on 2023-10-09 16:10

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('DRAFT', 'DRAFT'), ('INACTIVE', 'Inactive'), ('REMOVED', 'Removed')], db_index=True, default='ACTIVE', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', versatileimagefield.fields.VersatileImageField(blank=True, height_field='height', null=True, upload_to='brand', width_field='width')),
                ('width', models.PositiveIntegerField(blank=True, null=True)),
                ('height', models.PositiveIntegerField(blank=True, null=True)),
                ('origin', models.CharField(blank=True, max_length=64)),
                ('popularity', models.PositiveIntegerField(default=0)),
                ('entry_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_entry_by', to=settings.AUTH_USER_MODEL, verbose_name='entry by')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='last updated by')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('DRAFT', 'DRAFT'), ('INACTIVE', 'Inactive'), ('REMOVED', 'Removed')], db_index=True, default='ACTIVE', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', versatileimagefield.fields.VersatileImageField(blank=True, height_field='height', null=True, upload_to='category', width_field='width')),
                ('width', models.PositiveIntegerField(blank=True, null=True)),
                ('height', models.PositiveIntegerField(blank=True, null=True)),
                ('entry_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_entry_by', to=settings.AUTH_USER_MODEL, verbose_name='entry by')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='last updated by')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('DRAFT', 'DRAFT'), ('INACTIVE', 'Inactive'), ('REMOVED', 'Removed')], db_index=True, default='ACTIVE', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('origin', models.CharField(blank=True, max_length=64)),
                ('popularity', models.PositiveIntegerField(default=0)),
                ('logo', versatileimagefield.fields.VersatileImageField(blank=True, height_field='height', null=True, upload_to='manufacturer_logo', width_field='width')),
                ('width', models.PositiveIntegerField(blank=True, null=True)),
                ('height', models.PositiveIntegerField(blank=True, null=True)),
                ('entry_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_entry_by', to=settings.AUTH_USER_MODEL, verbose_name='entry by')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='last updated by')),
            ],
            options={
                'verbose_name': 'Product Manufacturer',
                'verbose_name_plural': 'Product Manufacturer',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('DRAFT', 'DRAFT'), ('INACTIVE', 'Inactive'), ('REMOVED', 'Removed')], db_index=True, default='ACTIVE', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('buying_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('mrp', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('discounted', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('discounted_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('stock', models.BigIntegerField(default=0)),
                ('is_published', models.BooleanField(default=True)),
                ('is_salesable', models.BooleanField(default=False)),
                ('image', versatileimagefield.fields.VersatileImageField(blank=True, height_field='height', null=True, upload_to='brand', width_field='width')),
                ('width', models.PositiveIntegerField(blank=True, null=True)),
                ('height', models.PositiveIntegerField(blank=True, null=True)),
                ('rating', models.DecimalField(decimal_places=1, default=0.0, max_digits=2)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='brand_products', to='product.brand')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.category')),
                ('entry_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_entry_by', to=settings.AUTH_USER_MODEL, verbose_name='entry by')),
                ('manufacturer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='manufacturer_products', to='product.manufacturer')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='last updated by')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]