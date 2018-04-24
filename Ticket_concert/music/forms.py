from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Optional.',widget=forms.TextInput(attrs={
        'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.',widget=forms.TextInput(attrs={
        'class':'form-control','placeholder':'Last Name'}))
    email = forms.EmailField(max_length=254,required=True, help_text='Required. Inform a valid email address.',widget=forms.TextInput(attrs={
        'class':'form-control','placeholder':'Email'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class SignInForm(forms.Form):
    username = forms.CharField(max_length=30,required=True,widget=forms.TextInput(attrs={
        'class':'form-control','placeholder':'User Name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control','placeholder':'Password'}))
    next = forms.CharField(max_length=100,required=False,widget=forms.HiddenInput())

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password is not None:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("User Does Not Exist.")
            if not user.check_password(password):
                raise forms.ValidationError("Password Does not Match.")
            if not user.is_active:
                raise forms.ValidationError("User is not Active.")

        return super(SignInForm, self).clean(*args, **kwargs)