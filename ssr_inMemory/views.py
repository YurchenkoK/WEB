from django.shortcuts import render
from .static.static_data import drugs_data, estimation_data

CURRENT_USER_ID = 1

def get_data():
    drugs = []
    for drug in drugs_data:
        drugs.append({
            'id': drug[0],
            'name': drug[1],
            'description': drug[2],
            'image': drug[3],
            'concentration': f'{drug[4]} мг/мл',
            'volume': f'{drug[5]} мл',
            'min_dose': drug[6],
            'max_dose': drug[7],
        })
    
    return {'drugs': drugs}

def get_estimation_data():
    estimation_items = []
    
    user_drugs = [item for item in estimation_data if item[0] == CURRENT_USER_ID]
    
    for user_drug in user_drugs:
        drug_id = user_drug[1]
        
        for drug in drugs_data:
            if drug[0] == drug_id:
                estimation_items.append({
                    'id': drug[0],
                    'name': drug[1],
                    'concentration': f'{drug[4]} мг/мл',
                    'volume': f'{drug[5]} мл',
                    'image': drug[3],
                    'min_dose': drug[6],
                    'max_dose': drug[7],
                })
                break
    
    return {'estimation_items': estimation_items}

def index(request):
    data = get_data()
    search_query = request.GET.get('search', '')
    
    if search_query:
        filtered_drugs = []
        for drug in data['drugs']:
            if search_query.lower() in drug['name'].lower():
                filtered_drugs.append(drug)
        data['drugs'] = filtered_drugs
    
    estimation_count = len([item for item in estimation_data if item[0] == CURRENT_USER_ID])
    data['estimation_count'] = estimation_count
    
    return render(request, 'main.html', {'data': data, 'search_query': search_query})

def vasoactive_drug_detail(request, drug_id):
    data = get_data()
    drug = None
    
    for d in data['drugs']:
        if d['id'] == drug_id:
            drug = d
            break
    
    estimation_count = len([item for item in estimation_data if item[0] == CURRENT_USER_ID])
    
    return render(request, 'vasoactive_drug.html', {'drug': drug, 'estimation_count': estimation_count})

def estimation_infusion_speed(request):
    data = get_estimation_data()
    
    estimation_params = {
        'ampoules': 3,
        'solvent_volume': 250,
        'patient_weight': 70,
    }
    
    data['estimation_params'] = estimation_params
    return render(request, 'estimation_infusion_speed.html', {'data': data})