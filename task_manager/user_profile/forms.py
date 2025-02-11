from django import forms

from .choice_fields_options import LANGUAGES_CHOICES, PRIVACY_CHOICES
from .models import Profile, SocialLinks


class ProfileForm(forms.ModelForm):
    dark_theme = forms.BooleanField(
        label='Тёмная тема'
    )
    profile_picture = forms.ImageField(
        label='Картинка профиля'
    )
    bio = forms.CharField(
        widget=forms.Textarea,
        label='Расскажите о себе!'
    )
    privacy = forms.ChoiceField(
        choices=PRIVACY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Настройки приватности'
    )
    languages = forms.MultipleChoiceField(
        choices=LANGUAGES_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label='Языки, которыми вы владеете'
    )

    class Meta:
        model = Profile
        fields = [
            'dark_theme',
            'profile_picture',
            'bio',
            'privacy',
            'languages'
        ]


class SocialLinksForm(forms.ModelForm):
    facebook_link = forms.URLField(
        label='Facebook'
    )
    twitter_link = forms.URLField(
        label='Twitter'
    )
    linkedin_link = forms.URLField(
        label='LinkedIn'
    )
    instagram_link = forms.URLField(
        label='Instagram'
    )
    youtube_link = forms.URLField(
        label='Youtube'
    )
    tiktok_link = forms.URLField(
        label='Tiktok'
    )
    reddit_link = forms.URLField(
        label='Reddit'
    )
    telegram_link = forms.URLField(
        label='Telegram'
    )
    discord_link = forms.URLField(
        label='Discord'
    )
    steam_link = forms.URLField(
        label='Steam'
    )
    twitch_link = forms.URLField(
        label='Twitch'
    )

    class Meta:
        model = SocialLinks
        fields = [
            'facebook_link',
            'twitter_link',
            'linkedin_link',
            'instagram_link',
            'youtube_link',
            'tiktok_link',
            'reddit_link',
            'telegram_link',
            'discord_link',
            'steam_link',
            'twitch_link'
        ]
