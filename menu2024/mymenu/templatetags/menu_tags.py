from django import template
from mymenu.models import *

register = template.Library()




@register.inclusion_tag('mymenu/dr_menu.html')
def draw_menu(menuName=None, item_slug=None):
    if item_slug:
        selitem = MenuItems.objects.filter(slug=item_slug)[0]
        counter = 1


        menu = Menu.objects.filter(title=menuName)[0]


        itms = menu.Items.all().select_related('ancestor')


        # counter = 1
        for i in itms:
            setattr(i,'counter', counter)
            counter += 1
            if selitem.slug == i.slug:
                setattr(selitem,'numba', counter)
                #добавляю выбранному элементу свойство намба, чтобы в шаблоне от него отталкиваясь,открывать все вышеоткрытые и одну нижнюю(такое задание)вкладки



        return {'menu':menu, 'cat_selected':item_slug, 'selitem':selitem, 'itms':itms}



    #для неразвернутого меню(главной страницы)
    menu = Menu.objects.filter(title=menuName).prefetch_related("Items")[0]

    #получаю список элементов чтобы не дублировать запрос в шаблоне
    itemlist = [item for item in menu if item.isroot]

    return {'menu':menu, 'cat_selected': item_slug, 'itemlist': itemlist}
