from django.shortcuts import render


def get_menu(request, menu_slug):
    return render(request, 'menu.html', {'menu_slug': menu_slug})
