from django import forms
from friends.models import Follow


class FollowForm(forms.ModelForm):
    class Meta:
        model = Follow
        fields = "__all__"