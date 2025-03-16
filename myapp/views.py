from django.shortcuts import render, get_object_or_404
from .models import Menu  

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    menu_items = Menu.objects.all()
    return render(request, 'menu.html', {'menu_items': menu_items})

def book(request):
    return render(request, 'book.html')

def display_menu_items(request, pk=None):
    if pk:
        menu_item = get_object_or_404(Menu, pk=pk)
        return render(request, 'menu_item.html', {'menu_item': menu_item})
    else:
        menu_items = Menu.objects.all()  # Show all menu items if no ID
        return render(request, 'menu.html', {'menu_items': menu_items})


def menu_item_detail(request, pk):
    menu_item = get_object_or_404(Menu, pk=pk)
    return render(request, 'menu_item.html', {'menu_item': menu_item}) 
