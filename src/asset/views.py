from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Asset


# Create your views here.
class AssetListView(ListView):
    model = Asset
    context_object_name = 'assets'
    ordering = ['-created']

# @login_required
# def asset_list(request):
#     template_name = 'asset_list.html'
#     context = {'assets': Asset.objects.all(),
#                'page_title': 'All Assets',
#                'asset_link': 'active'}
#     return render(request, template_name, context)
#
@login_required
def asset_detail(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)
    template_name = 'asset/asset_detail.html'
    context = {'asset': asset,
               'page_title': 'Assets | ' + asset.name,
               'asset_link': 'active'}
    return render(request, template_name, context)
