# fetcher/forms.py
from django import forms


class URLForm(forms.Form):
    url = forms.URLField(
        label="Enter a URL",
        widget=forms.URLInput(attrs={"placeholder": "https://example.com"}),
    )


class ContributionForm(forms.Form):
    heading = forms.CharField(
        label="Heading",
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Enter the main heading"}),
    )
    subheading = forms.CharField(
        label="Subheading",
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Enter the subheading"}),
    )
    reference_text = forms.CharField(
        label="Reference Text",
        required=True,
        widget=forms.Textarea(attrs={"placeholder": "Enter reference text here..."}),
    )
