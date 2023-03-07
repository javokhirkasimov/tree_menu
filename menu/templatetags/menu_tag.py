from django import template
from ..models import MenuElements

register = template.Library()


@register.inclusion_tag('tree_view_render.html')
def draw_menu(menu_name):
    obj = MenuElements.objects.filter(menu__name=menu_name, parent=None)
    if obj:
        return {'menu_name': menu_name, 'menu_elements': obj}
    return {"menu_name": menu_name, "menu_elements": None}
