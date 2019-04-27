from django import forms
from .models import Tenant, Asset


class TenantCreateForm(forms.ModelForm):

    class Meta:
        model = Tenant
        fields = ['asset', 'first_name', 'last_name', 'mobile', 'email']

    def __init__(self, *args, **kwargs):
        owner = kwargs.pop('owner', None)
        super().__init__(*args, **kwargs)
        self.fields['asset'].queryset = Asset.objects.filter(owner=owner)
