from django.shortcuts import render
from django.http import Http404

def get_data():
    return {
        'drugs': [
            {
                'id': 1,
                'name': 'Допамин',
                'concentration': '40 мг/мл',
                'image': 'http://localhost:9000/images/dopamine.png',
                'volume': '5 мл',
                'description': 'Допамин - предшественник норадреналина, стимулирует допаминовые и адренергические рецепторы.'
            },
            {
                'id': 2,
                'name': 'Нитроглицерин',
                'concentration': '1 мг/мл',
                'image': 'http://localhost:9000/images/nitroglic.jpg',
                'volume': '1 мл',
                'description': 'Нитроглицерин - органический нитрат, используется для лечения стенокардии и сердечной недостаточности.'
            },
            {
                'id': 3,
                'name': 'Норадреналин',
                'concentration': '2 мг/мл',
                'image': 'http://localhost:9000/images/Norenadren.png',
                'volume': '4 мл',
                'description': 'Норадреналин - мощный вазоконстриктор, используется при шоке и артериальной гипотензии.'
            },
            {
                'id': 4,
                'name': 'Адреналин',
                'concentration': '1 мг/мл',
                'image': 'http://localhost:9000/images/EpiVial.jpg',
                'volume': '1 мл',
                'description': 'Адреналин - катехоламин широкого спектра действия, используется при анафилактическом шоке.'
            },
            {
                'id': 5,
                'name': 'Добутамин',
                'concentration': '12.5 мг/мл',
                'image': 'http://localhost:9000/images/DOBUTAMINEl.png',
                'volume': '20 мл',
                'description': 'Добутамин - селективный агонист β1-адренорецепторов, кардиотоник при сердечной недостаточности.'
            },
            {
                'id': 6,
                'name': 'Милринон',
                'concentration': '1 мг/мл',
                'image': 'http://localhost:9000/images/Milrinonepackvial.png',
                'volume': '10 мл',
                'description': 'Милринон - ингибитор фосфодиэстеразы III, положительный инотроп и вазодилататор.'
            },
            {
                'id': 7,
                'name': 'Фенилэфрин',
                'concentration': '10 мг/мл',
                'image': 'http://localhost:9000/images/phenylephirine.jpg',
                'volume': '1 мл',
                'description': 'Фенилэфрин - селективный α1-адреномиметик, вызывает вазоконстрикцию при гипотензии.'
            },
            {
                'id': 8,
                'name': 'Вазопрессин',
                'concentration': '20 мг/мл',
                'image': 'http://localhost:9000/images/Vasopresin.png',
                'volume': '1 мл',
                'description': 'Вазопрессин - антидиуретический гормон, мощный вазоконстриктор при рефрактерном шоке.'
            },
            {
                'id': 9,
                'name': 'Левосимендан',
                'concentration': '2.5 мг/мл',
                'image': 'http://localhost:9000/images/levosemindan.jpg',
                'volume': '5 мл',
                'description': 'Левосимендан - кальциевый сенситайзер, инотропный препарат при острой сердечной недостаточности.'
            },
            {
                'id': 10,
                'name': 'Изопреналин',
                'concentration': '0.2 мг/мл',
                'image': 'http://localhost:9000/images/isopreterenol.png',
                'volume': '1 мл',
                'description': 'Изопреналин - неселективный β-адреномиметик, используется при брадикардии и AV-блокадах.'
            }
        ]
    }

def get_cart_data():
    return {
        'cart_items': [
            {
                'id': 2,
                'name': 'Нитроглицерин',
                'concentration': '1 мг/мл',
                'volume': '5 мл',
                'image': 'img/nitroglicerin.png',
            },
            {
                'id': 1,
                'name': 'Допамин',
                'concentration': '40 мг/мл',
                'volume': '2 мл',
                'image': 'img/dopamin.png',
            },
        ]
    }

def index(request):
    data = get_data()
    search_query = request.GET.get('search', '')
    
    if search_query:
        filtered_drugs = []
        for drug in data['drugs']:
            if search_query.lower() in drug['name'].lower():
                filtered_drugs.append(drug)
        data['drugs'] = filtered_drugs
    
    return render(request, 'main.html', {'data': data, 'search_query': search_query})

def drug_detail(request, drug_id):
    data = get_data()
    drug = None
    
    for d in data['drugs']:
        if d['id'] == drug_id:
            drug = d
            break
    
    if drug is None:
        raise Http404("Препарат не найден")
    
    return render(request, 'product.html', {'drug': drug})

def cart(request):
    data = get_cart_data()
    return render(request, 'cart.html', {'data': data})