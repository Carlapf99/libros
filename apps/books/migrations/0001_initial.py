from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=180)),
                ('slug', models.SlugField(unique=True)),
                ('cover', models.ImageField(upload_to='books/')),
                ('synopsis', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('purchase_url', models.URLField()),
                ('is_featured', models.BooleanField(default=False)),
                ('published_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
