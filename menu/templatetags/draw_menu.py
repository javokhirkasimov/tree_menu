from django import template
from menu.models import Menu
from django.utils.safestring import mark_safe

register = template.Library()


def generate_html(menu_items):
    # Generates html unordered list for menu items
    html = '<ul>'
    for item in menu_items:
        html += '<li>'
        html += f'<a href="/{item.slug}">{item.name}</a>'
        if item.sub_menu.exists():
            html += generate_html(item.sub_menu.all())
        html += '</li>'
    html += '</ul>'
    return html


@register.simple_tag
def draw_menu(menu_slug):
    menu_items = Menu.objects.filter(slug=menu_slug).select_related('parent')
    return mark_safe(generate_html(menu_items))
