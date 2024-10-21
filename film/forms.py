from django import forms
from .models import Review

dropdown_options = (("all", "See all"), ("film", "Films"), ("category", "Categories"), ("director", "Directors"))

class WriteReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("title", "content", "rating")

class SearchForm(forms.Form):
    q = forms.CharField()
    dropdown = forms.ChoiceField(choices=dropdown_options)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["dropdown"].required = False
        