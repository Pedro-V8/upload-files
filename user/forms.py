from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import Profile


class UserForm(UserCreationForm):
    #email = forms.EmailField(required=True)
    #age = forms.IntegerField(required=True)

    class Meta:
        model = Profile
        fields = ("first_name" , "last_name" , "age" , "username" , "email" , "password1" , "password2" , "is_active")

    '''def save(self, commit=True):
        user = super(UserForm , self).save(commit=False)
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()
        return user'''


