from django.shortcuts import render, redirect
from .models import Site
from django.views.decorators.cache import never_cache
from django.http import JsonResponse

@never_cache
def index(request):
    site = Site.objects.first()  # Mengambil situs pertama
    return render(request, 'index.html', {'site': site})
    # End of  Selection

def login(request):
    if request.method == 'POST':
        # Logika untuk memproses login
        return redirect('admin_index')
    return render(request, '/login.html')

def logout(request):
    # Logika untuk memproses logout
    return redirect('admin_login')
#===================================================
def tables(request):
    return render(request, 'tables/tables.html')

def icon_menu(request):
    return render(request, 'icon-menu.html')

def sidebar(request):
    return render(request, 'sidebar-style-2.html')

def widgets(request):
    return render(request, 'widgets.html')

def starter_template(request):
    return render(request, 'starter-template.html')

def datatables(request):
    return render(request, 'tables/datatables.html')

def get_site_data(request):
    site = Site.objects.first()
    return JsonResponse({'site_name': site.site_name})