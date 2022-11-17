from postad.models import *
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Field, Layout
from postad.models import Bookmark


class PostAdCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostAdCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Field("title", css_class="form-control bg-white"),
            Field("price", css_class="form-control bg-white"),
            Field("brand", css_class="form-control bg-white"),
            Field("model", css_class="form-control bg-white"),
            Field("state", css_class="form-control w-100 bg-white"),
            Field("city", css_class="form-control bg-white"),
            Field("purchase_year", css_class="form-control bg-white"),
            Field("category", css_class="form-control w-100 bg-white"),
            Field("condition", css_class="form-control w-100 bg-white"),
            Field("seller_type", css_class="form-control w-100 bg-white"),
            Field("description", css_class="form-control bg-white"),
            Field("image1", css_class="form-control bg-white"),
            Field("image2", css_class="form-control bg-white"),
            Field("image3", css_class="form-control bg-white"),
            Field("image4", css_class="form-control bg-white"),
            Field("image5", css_class="form-control bg-white"),
        )

        self.helper.add_input(Submit("submit", "Submit", css_class="btn btn-primary d-block mt-2"))
    
    class Meta:
        model = PostAD
        fields = [
            "title",
            "description",
            "price",
            "brand",
            "model",
            "purchase_year",
            "state",
            "city",
            "category",
            "condition",
            "seller_type",
            "image1",
            "image2",
            "image3",
            "image4",
            "image5",
        ]
        widgets = {
            "purchase_year": forms.DateInput(attrs={"type": "date"})
        }

class UpdatePostAdCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UpdatePostAdCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Field("title", css_class="form-control bg-white"),
            Field("price", css_class="form-control bg-white"),
            Field("brand", css_class="form-control bg-white"),
            Field("model", css_class="form-control bg-white"),
            Field("state", css_class="form-control w-100 bg-white"),
            Field("city", css_class="form-control bg-white"),
            Field("purchase_year", css_class="form-control bg-white"),
            Field("category", css_class="form-control w-100 bg-white"),
            Field("condition", css_class="form-control w-100 bg-white"),
            Field("seller_type", css_class="form-control w-100 bg-white"),
            Field("description", css_class="form-control bg-white"),
            Field("image1", css_class="form-control bg-white"),
            Field("image2", css_class="form-control bg-white"),
            Field("image3", css_class="form-control bg-white"),
            Field("image4", css_class="form-control bg-white"),
            Field("image5", css_class="form-control bg-white"),
            Field("sold"),
        )

        self.helper.add_input(Submit("submit", "Submit", css_class="btn btn-primary d-block mt-2"))
    
    class Meta:
        model = PostAD
        fields = [
            "title",
            "description",
            "price",
            "brand",
            "model",
            "purchase_year",
            "state",
            "city",
            "category",
            "condition",
            "seller_type",
            "image1",
            "image2",
            "image3",
            "image4",
            "image5",
            "sold",
        ]
        widgets = {
            "purchase_year": forms.DateInput(attrs={"type": "date"})
        }


class BookmarkForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = "__all__"