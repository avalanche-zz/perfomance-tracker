from datetime import date
from django import forms


class AddStreamForm(forms.ModelForm):
    stream = forms.IntegerField(
        min_value=2000,
        max_value=2099,
        initial=date.today().year,
        label='Год зачисления'
    )
    required = forms.IntegerField(
        min_value = 0,
        initial=600,
        label='Количество баллов для допуска к аттестации'
    )
    autopass = forms.IntegerField(
        min_value=0,
        initial=1000,
        label='Количество баллов для оценки за аттестацию автоматом'
    )
