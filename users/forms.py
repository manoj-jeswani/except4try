from django.contrib.auth import authenticate
from django import forms
from .models import Euser

class EuserRegisterForm(forms.ModelForm):
    class Meta:
        model = Euser
        fields = [
            'username',
            "email",
            "password",
            'confirm_password'
        ]

    username = forms.CharField(label="Handle")
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password =forms.CharField(widget=forms.PasswordInput)
 


    def clean(self, *args, **keyargs):
        email = self.cleaned_data.get("email")
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords must match")

        eqs = Euser.objects.filter(email=email)
        if eqs.exists():
            raise forms.ValidationError("User with this email is already registered !")

   
        uqs = Euser.objects.filter(username=username)
        if uqs.exists():
            raise forms.ValidationError("User with this username is already registered !")

        if len(password) < 4:
            raise forms.ValidationError("Password must contain atleast 4 characters")

        return super(EuserRegisterForm, self).clean(*args, **keyargs)