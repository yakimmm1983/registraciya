

from django import forms
from django.contrib.auth import authenticate
from django.shortcuts import render
from django.core.exceptions import ValidationError
# class MyForm(forms.Form):
#     nickname = forms.CharField(label = 'Имя пользователя',max_length = 100)
#     age = forms.IntegerField(label='Пароль')
#
#     def clean_age(self):
#         age = self.cleaned_data.get('age')
#         if not age % 2:
#             raise ValidationError('Возраст должен быть четным')
#         return age
#
#     def clean(self):
#         cleanedData = super().clean()
#         age = cleanedData.get('age')
#         nickname = cleanedData.get('nickname')
#         if str(age) in nickname:
#             self.add_error('age','Возраст не может быть использован в имени')
#         self.add_error(None,'Форма некорректна всегда')

class AuthentificationForm(forms.Form):
    username = forms.CharField(max_length=254)
    password = forms.CharField(label= ("Password"),widget=forms.PasswordInput)
    def clean(self):
        cleanedData = super().clean()
        username = cleanedData.get('username')
        password = cleanedData.get('password')
        if username and password:
            self.user = authenticate(username=username,password=password)
            if self.user is None:
                raise forms.ValidationError()





