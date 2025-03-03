# Generated by Django 5.1.5 on 2025-02-08 04:42

import django.db.models.deletion
import multiselectfield.db.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, upload_to='profile_pictures/')),
                ('bio', models.TextField(max_length=300)),
                ('languages', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('chinese', 'Китайский'), ('arabic', 'Арабский'), ('hindi', 'Хинди'), ('english', 'Английский'), ('spanish', 'Испанский'), ('bengali', 'Бенгальский'), ('portuguese', 'Португальский'), ('russian', 'Русский'), ('japanese', 'Японский'), ('german', 'Немецкий'), ('korean', 'Корейский'), ('french', 'Французский'), ('javanese', 'Яванский'), ('telugu', 'Телугу'), ('marathi', 'Маратхи'), ('vietnamese', 'Вьетнамский'), ('tamil', 'Тамильский'), ('italian', 'Итальянский'), ('turkish', 'Турецкий'), ('urdu', 'Урду'), ('punjabi', 'Панджаби'), ('ukrainian', 'Украинский'), ('gujarati', 'Гуджарати'), ('thai', 'Тайский'), ('polish', 'Польский'), ('malayalam', 'Малаялам'), ('kannada', 'Каннада'), ('odia', 'Ория'), ('burmese', 'Бирманский'), ('azerbaijani', 'Азербайджанский'), ('persian', 'Персидский'), ('sundanese', 'Сунданский'), ('pashto', 'Пушту'), ('romanian', 'Румынский'), ('bhojpuri', 'Бходжпури'), ('hausa', 'Хауса'), ('maithili', 'Майтхили'), ('malaysian', 'Малайский'), ('serbo_croatian', 'Сербохорватский'), ('awadhi', 'Авадхи'), ('uzbek', 'Узбекский'), ('yoruba', 'Йоруба'), ('dutch', 'Нидерландский'), ('sindhi', 'Синдхи'), ('igbo', 'Игбо'), ('amharic', 'Амхарский'), ('oromo', 'Оромо'), ('indonesian', 'Индонезийский'), ('tagalog', 'Тагальский'), ('nepali', 'Непальский'), ('assamese', 'Ассамский'), ('saraiki', 'Сараики'), ('cebuano', 'Себуанский'), ('hungarian', 'Венгерский'), ('chittagonian', 'Читтагонг'), ('zhuang', 'Чжуанский'), ('shona', 'Шона'), ('madurese', 'Мадурский'), ('sinhalese', 'Сингальский'), ('marwari', 'Марвари'), ('magahi', 'Магахи'), ('haryanvi', 'Харьянви'), ('greek', 'Греческий'), ('czech', 'Чешский'), ('chhattisgarhi', 'Чхаттисгархи'), ('fula', 'Фула'), ('dakhni', 'Дакхни'), ('malagasy', 'Малагасийский'), ('belarusian', 'Белорусский')], max_length=300)),
                ('privacy', models.CharField(choices=[('open', 'Открытый профиль'), ('friends_only', 'Только для друзей'), ('private', 'Закрытый профиль')], default=('open', 'Открытый профиль'), max_length=16)),
                ('dark_theme', models.BooleanField(default=False)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SocialLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_link', models.URLField(blank=True)),
                ('twitter_link', models.URLField(blank=True)),
                ('linkedin_link', models.URLField(blank=True)),
                ('instagram_link', models.URLField(blank=True)),
                ('youtube_link', models.URLField(blank=True)),
                ('tiktok_link', models.URLField(blank=True)),
                ('reddit_link', models.URLField(blank=True)),
                ('telegram_link', models.URLField(blank=True)),
                ('discord_link', models.URLField(blank=True)),
                ('steam_link', models.URLField(blank=True)),
                ('twitch_link', models.URLField(blank=True)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user_profile.profile')),
            ],
        ),
    ]
