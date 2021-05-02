from django import forms
from .models import gym

class gymForm(forms.ModelForm):
    class Meta:
        model = gym
        fields = '__all__'
        genderChoices = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Others', 'Others')
        )
        widgets = {
            'gender': forms.RadioSelect(choices=genderChoices, attrs={'class': "custom-list"}),
        }