from django import forms
from . models import Detail


class Detail_form(forms.ModelForm):
    class Meta:
        model = Detail
        field = "__all__"
