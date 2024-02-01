# Generated by Django 3.2.12 on 2024-02-01 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('BookID', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=100)),
                ('ISBN', models.CharField(max_length=13)),
                ('PublishedDate', models.DateField()),
                ('Genre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('UserID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=100)),
                ('MembershipDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='BorrowedBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BorrowDate', models.DateField()),
                ('ReturnDate', models.DateField()),
                ('BookID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.user')),
            ],
        ),
        migrations.CreateModel(
            name='BookDetails',
            fields=[
                ('DetailsID', models.AutoField(primary_key=True, serialize=False)),
                ('NumberOfPages', models.IntegerField()),
                ('Publisher', models.CharField(max_length=100)),
                ('Language', models.CharField(max_length=100)),
                ('BookID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
            ],
        ),
    ]