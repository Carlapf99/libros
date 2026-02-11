from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='AuthorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150)),
                ('hero_quote', models.CharField(max_length=255)),
                ('biography', models.TextField()),
                ('photo', models.ImageField(upload_to='author/')),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Perfil del autor',
                'verbose_name_plural': 'Perfil del autor',
            },
        ),
    ]
