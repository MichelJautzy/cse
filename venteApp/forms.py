from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class SignUpForm(UserCreationForm):
    address = forms.CharField(max_length=500, required=False, widget=forms.Textarea)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'address')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        user.userprofile.address = self.cleaned_data.get('address')
        user.userprofile.save()
        return user

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('address',)