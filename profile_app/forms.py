from django import forms
from .models import UserProfile

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'bio', 'course', 'location', 'profile_pic']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'fb-input'}),
            'bio': forms.TextInput(attrs={'class': 'fb-input'}),
            'course': forms.TextInput(attrs={'class': 'fb-input'}),
            'location': forms.TextInput(attrs={'class': 'fb-input'}),
            'profile_pic': forms.FileInput(attrs={'class': 'fb-file-input', 'accept': 'image/*'}),
        }