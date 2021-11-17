from django.shortcuts import render, HttpResponse, Http404
from MainApp import models

author = {'Имя':'Павел','Отчество':'Михайлович','Фамилия':'Захаров','телефон':'8-960-545-86-86','email':'zakharovpm@rambler.ru'}

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 3, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 4, "name": "Картофель фри" ,"quantity":0},
   {"id": 5, "name": "Кепка" ,"quantity":124},
]




def home(request):
    context = {
        "name": "Павел",
        "surname": "Захаров",
        "page_title":"Домашняя страница"
    }
    return render(request,'index.html',context)

def about(request):
    return HttpResponse(f'Имя:<strong>{author["Имя"]}</strong><br>'
                        f'Отчество:<strong>{author["Отчество"]}</strong><br>'
                        f'Фамилия:<strong>{author["Фамилия"]}</strong><br>'
                        f'телефон:<strong>{author["телефон"]}</strong><br>'
                        f'email:<strong>{author["email"]}</strong><br>')

def get_item(request,id):
    
    item = models.Item.objects.get(pk=id)

    try:
        context = {
            "name": item.name,
            "count": item.count,
            "brand": item.brand,
        }
        return render(request, "item.html", context)
    except:
        raise Http404

def get_items(request):
    # _str = "<ol>"
    # for item in items:
    #     _str += f"<li><a href = '/item/{item['id']}/'>{item['name']}</a></li>"
    # _str += "</ol>"
    # return HttpResponse(_str)
    items = models.Item.objects.all()
    context = {"items": items}
    return render(request,"items_list.html",context)


