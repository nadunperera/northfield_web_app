from django import forms
from .models import Tenant, Asset


class TenantCreateForm(forms.ModelForm):

    class Meta:
        model = Tenant
        fields = ['asset', 'first_name', 'last_name', 'mobile', 'email']

    def __init__(self, *args, **kwargs):
        owner = kwargs.pop('owner', None)
        asset_id = kwargs.pop('asset_id', None)
        super().__init__(*args, **kwargs)
        if asset_id:
            self.fields['asset'].queryset = Asset.objects.filter(id=asset_id)
        else:
            self.fields['asset'].queryset = Asset.objects.filter(owner=owner)
