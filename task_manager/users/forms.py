from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()


class CreationForm(UserCreationForm):
    first_name = forms.CharField(
        label='Имя',
        max_length=32,
        widget=forms.TextInput(),
        required=False
    )
    last_name = forms.CharField(
        label='Фамилия',
        max_length=32,
        widget=forms.TextInput(),
        required=False
    )
    email = forms.EmailField(
        label='Электронная почта',
        widget=forms.EmailInput(),
        required=False
    )
    username = forms.CharField(
        max_length=100,
        label='Уникальное имя пользователя (username)',
        help_text='Не более 100 символов. '
                  'Буквы латинского алфавита, '
                  'цифры или символы @.+-_',
        widget=forms.TextInput(),
        required=True
    )
    password1 = forms.CharField(
        label='Введите пароль',
        help_text='Требования:\n'
                  '- Пароль должен быть не короче 8 символов\n'
                  '- Пароль должен содержать цифры и символы латинского алфавита\n'
                  '- Пароль не должен быть схожим с иными вашими данными\n'
                  '- Парoль не должен быть простым (например 12345678, password и т.д.)',
        widget=forms.PasswordInput,
        required=True
    )
    password2 = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'first_name', 'last_name',
            'email', 'username',
            'password1', 'password2'
        )
