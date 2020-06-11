from django import forms
from blog.models import *


class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    phone = forms.RegexField(required=False, regex='^[6-9]\d{9}$')

    def clean(self):
        cleaned_data = super().clean()
        # print(cleaned_data)

        if not (cleaned_data.get('email') or cleaned_data.get('phone')):
            raise forms.ValidationError('Please Enter either email or phone!', code='invalid')


    def clean_email(self):
       data = self.cleaned_data['email']
       if '@' not in data:
           raise forms.ValidationError('invalid domain', code='invalid')



class RegisterForm(forms.Form):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=32, min_length=8, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=32, min_length=8, widget=forms.PasswordInput)
    gender = forms.ChoiceField(choices= GENDER_CHOICES)

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get(('confirm_password'))

        # if password and confirm_password:

        if password != confirm_password:
            raise forms.ValidationError('Password not matched!!!')

class PostForm(forms.ModelForm):
    # content = forms.CharField()
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'status', 'image']
        # we can use : __all__ but it's not prefered way

