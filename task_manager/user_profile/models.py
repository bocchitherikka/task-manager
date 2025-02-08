from django.db import models
from django.contrib.auth import get_user_model
from multiselectfield import MultiSelectField
from .choice_fields_options import (
    DEFAULT,
    LANGUAGES_CHOICES,
    PRIVACY_CHOICES
)

User = get_user_model()


class Profile(models.Model):
    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    profile_picture = models.ImageField(
        upload_to='static/profile_pictures/',
        blank=True
    )
    bio = models.TextField(
        max_length=300,
        blank=True
    )
    languages = MultiSelectField(
        choices=LANGUAGES_CHOICES,
        max_length=300,
        blank=True
    )
    privacy = models.CharField(
        choices=PRIVACY_CHOICES,
        default=PRIVACY_CHOICES[DEFAULT],
        max_length=16
    )
    dark_theme = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.owner.__str__()


class SocialLinks(models.Model):
    profile = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE
    )
    facebook_link = models.URLField(
        blank=True
    )
    twitter_link = models.URLField(
        blank=True
    )
    linkedin_link = models.URLField(
        blank=True
    )
    instagram_link = models.URLField(
        blank=True
    )
    youtube_link = models.URLField(
        blank=True
    )
    tiktok_link = models.URLField(
        blank=True
    )
    reddit_link = models.URLField(
        blank=True
    )
    telegram_link = models.URLField(
        blank=True
    )
    discord_link = models.URLField(
        blank=True
    )
    steam_link = models.URLField(
        blank=True
    )
    twitch_link = models.URLField(
        blank=True
    )

    def __str__(self):
        return self.profile.__str__()
