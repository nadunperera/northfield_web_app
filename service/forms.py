from django import forms
from .models import Service, Asset


class ServiceCreateForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = ['asset', 'name', 'category', 'provider']

    def __init__(self, *args, **kwargs):
        owner = kwargs.pop('owner', None)
        asset_id = kwargs.pop('asset_id', None)
        super().__init__(*args, **kwargs)
        if asset_id:
            self.fields['asset'].queryset = Asset.objects.filter(id=asset_id)
        else:
            self.fields['asset'].queryset = Asset.objects.filter(owner=owner)
