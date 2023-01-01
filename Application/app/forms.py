"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class BmiForm(forms.Form):
    height = forms.FloatField(
        label='請輸入身高(m)', 
        widget=forms.NumberInput(attrs={'class':'form-control'}),
        error_messages={'required': '請輸入身高'})
    weight = forms.CharField(
        label='請輸入體重(kg)', 
        widget=forms.TextInput(attrs={'class':'form-control'}),
        error_messages={'required': '請輸入體重'})

def clean(self):
        cd = self.cleaned_data

        try:
            weight = float(cd.get('weight'))
            height = float(cd.get('height'))

            height_condition = (height > 2.5) or (height <= 0)
            if height_condition:
                self.add_error('height', "請輸入合理範圍的身高!")

            weight_condition = (weight > 200) or (weight <= 15)
            if weight_condition:
                self.add_error('weight', "請輸入合理範圍的體重!")
        except:
            self.add_error('weight', "請輸入數字!")

        return cd