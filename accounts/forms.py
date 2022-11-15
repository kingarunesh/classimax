from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Field, Layout
from django.contrib.auth import get_user_model
User = get_user_model()


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    username = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta(UserCreationForm):
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")



class UserProfileUpdate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserProfileUpdate, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Field("username", css_class="form-control bg-white"),
            Field("first_name", css_class="form-control bg-white"),
            Field("last_name", css_class="form-control bg-white"),
            Field("email", css_class="form-control bg-white"),
            Field("phone", css_class="form-control bg-white"),
            Field("about", css_class="form-control bg-white"),
            Field("dob", css_class="form-control bg-white"),
            Field("gender", css_class="form-control w-100 bg-white"),
            Field("image", css_class="form-control bg-white"),
        )

        self.helper.add_input(Submit("submit", "Submit", css_class="btn btn-primary d-block mt-2"))
    
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "phone",
            "about",
            "dob",
            "gender",
            "image"  
        ]
        widgets = {
            "dob": forms.DateInput(attrs={"type": "date"})
        }