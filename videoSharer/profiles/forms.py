from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'location', 'image']

    def signup(self, request, user):
        profile = super().save(commit=False)
        profile.user = user

        if not profile.image:
            profile.image = 'uploads/profile_pics/default.jpg'

        profile.save()
