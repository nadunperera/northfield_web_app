from django import forms
from .models import Service, Asset


class ServiceCreateForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = ['asset', 'name', 'category', 'provider']

    def __init__(self, *args, **kwargs):
        owner = kwargs.pop('owner', None)
        super().__init__(*args, **kwargs)
        self.fields['asset'].queryset = Asset.objects.filter(owner=owner)
