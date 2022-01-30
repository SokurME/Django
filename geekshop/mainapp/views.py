from django.shortcuts import render
from django.utils import timezone

# Create your views here.

links_menu = [
        {'url': 'main', 'name': 'домой'},
        {'url': 'products', 'name': 'продукты'},
        {'url': 'contact', 'name': 'контакты'},
]

def main(request):
    return render(request, 'mainapp/index.html', context ={
        'title': 'Магазин',
        'class_name': 'slider',
        'links_menu': links_menu,
        'datetime': timezone.now(),
        'description': "Новый уровень комфорта. Отличные характеристики.",
    })


def products(request):
    return render(request, 'mainapp/products.html', context ={
        'title': 'Каталог',
        'class_name': 'hero-white',
        'links_menu': links_menu,
        'description': ["Расположитесь комфортно" ,
                        "Отличное качество материалов позволит вам это",
                        "Различные цвета",
                        "Высочайший уровень эргономики и прочность."],
    })


def contact(request):
    return render(request, 'mainapp/contact.html', context ={
        'title': 'Контакты',
        'class_name': 'hero',
        'links_menu': links_menu,
        'contacts': ['наши', 'контакты'],
        'phone': '+7-888-888-88889'
    })

