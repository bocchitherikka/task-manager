from django import forms

from .models import Task, TASK_STATUS_CHOICES


class TaskForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(),
        label='Название таски'
    )
    description = forms.CharField(
        widget=forms.Textarea,
        label='Более подробное описание таски'
    )
    status = forms.ChoiceField(
        choices=TASK_STATUS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Статус'
    )
    end_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'type': 'date',
            'min': '1970-01-01'
        }),
        label="Дата дедлайна"
    )
    contributors = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'rows': 1}),
        label="Укажите юзернеймы пользователей, "
              "с которыми будете вместе работать "
              "над этой таской (через пробел, без "
              "лишних разделительных символов)"
    )

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'end_date',]

    def clean_contributors(self) -> list:
        info = self.cleaned_data['contributors']
        if info:
            return ''.join(info).split(' ')
        return []
