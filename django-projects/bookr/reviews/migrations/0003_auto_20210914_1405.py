# Generated by Django 3.2.7 on 2021-09-14 14:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0002_auto_20210912_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.RemoveField(
            model_name='review',
            name='date_of_borrow',
        ),
        migrations.RemoveField(
            model_name='review',
            name='date_of_return',
        ),
        migrations.RemoveField(
            model_name='review',
            name='reader',
        ),
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.CharField(default='', max_length=20, verbose_name='ISBN number of the book'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='publication_date',
            field=models.DateField(verbose_name='Date the book was published'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(default='', help_text='The contact email for person', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='content',
            field=models.TextField(default='', help_text='The review text'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='craetor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, help_text='The date and time the review was created.'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='date_edited',
            field=models.DateTimeField(help_text='The date and time the review was edited.', null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(help_text='The rating the reviewers has given'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(help_text='The title of the book', max_length=70),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(help_text='The person last name', max_length=20),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(help_text='The person first name', max_length=20),
        ),
        migrations.RenameModel(
            old_name='Reader',
            new_name='Contributor',
        ),
        migrations.CreateModel(
            name='BookContributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('AUTHOR', 'Author'), ('CO_AUTHOR', 'Co-Author'), ('EDITOR', 'Editor')], max_length=20, verbose_name='The role this contributor had in the book')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.book')),
                ('contributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.contributor')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='contributors',
            field=models.ManyToManyField(through='reviews.BookContributor', to='reviews.Contributor'),
        ),
    ]
