from django.shortcuts import render, redirect
from .forms import formClass
from .models import form_table
import csv

# Create your views here.
def home(request):
    return render(request, 'home.html')

def form(request):
    form = formClass()
    form_submitted = False

    if request.method == 'POST' and 'submit' in request.POST:
        form = formClass(request.POST)
        if form.is_valid():
            # Get the submitted form data
            submitted_data = form.cleaned_data

            # Check if identical data already exists in the database
            if form_table.objects.filter(
                id_da_rua=submitted_data['id_da_rua'],
                id_ponto=submitted_data['id_ponto'],
                metragem=submitted_data['metragem'],
                logradouro=submitted_data['logradouro'],
                numero=submitted_data['numero'],
                numero_original=submitted_data['numero_original'],
                data_inicial=submitted_data['data_inicial'],
                data_final=submitted_data['data_final'],
                fonte=submitted_data['fonte'],
                autor_da_alimentacao=submitted_data['autor_da_alimentacao'],
                data=submitted_data['data'],
            ).exists():
                print("Identical data already exists in the database.")
            else:
                form.save()
                print("Form saved successfully!")
                form_submitted = True
                return redirect('form')

        else:
            print(form.errors)

    else:
        print("Form not submitted via POST method")

    context = {'form': form, 'form_submitted': form_submitted}
    return render(request, 'form.html', context)

def empty(request):
    return render(request, 'empty.html')

def table(request):
    forms = form_table.objects.all()  
    
    context = {
        'forms': forms,
    }
    return render(request, 'table.html', context)


from django.http import HttpResponse

def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="table_data.csv"'
    
    writer = csv.writer(response, delimiter=';')
    writer.writerow([
        'ID da Rua', 'ID do Ponto', 'Metragem', 'Logradouro', 'Número', 
        'Número Original', 'Data Inicial', 'Data Final', 'Fonte', 
        'Autor da Alimentação', 'Data'
    ])

    forms = form_table.objects.all() 
    
    for form in forms:
        writer.writerow([
            form.id_da_rua, form.id_ponto, form.metragem, form.logradouro, 
            form.numero, form.numero_original, form.data_inicial, form.data_final, 
            form.fonte, form.autor_da_alimentacao, form.data
        ])
    
    return response

import csv
from io import StringIO
from django.http import JsonResponse
from .models import form_table

import datetime

import logging

import csv
from django.shortcuts import render


import csv
from django.shortcuts import render


import csv
from django.shortcuts import render
from .models import form_table

def upload_csv(request):
    if request.method == 'POST':
        csv_data = request.FILES['csv_file']
        if not csv_data.name.endswith('.csv'):
            return render(request, 'empty.html', {'error': 'Adicione arquivo.'})

        decoded_data = csv_data.read().decode('utf-8')
        csv_reader = csv.reader(decoded_data.splitlines(), delimiter=';') # Use semicolon as the separator
        next(csv_reader)  # Skip header row if it exists

        existing_records = []
        new_records = []

        for i, row in enumerate(csv_reader, start=1):
            id_da_rua = row[0]
            id_ponto = row[1]
            metragem = row[2]
            logradouro = row[3]
            numero = row[4]
            numero_original = row[5]
            data_inicial = row[6]
            data_final = row[7]
            fonte = row[8]
            autor_da_alimentacao = row[9]
            data = row[10]

            # Check if the record already exists in the table
            if form_table.objects.filter(
                id_da_rua=id_da_rua,
                id_ponto=id_ponto,
                metragem=metragem,
                logradouro=logradouro,
                numero=numero,
                numero_original=numero_original,
                data_inicial=data_inicial,
                data_final=data_final,
                fonte=fonte,
                autor_da_alimentacao=autor_da_alimentacao,
                data=data
            ).exists():
                existing_records.append(i)
            else:
                obj = form_table(
                    id_da_rua=id_da_rua,
                    id_ponto=id_ponto,
                    metragem=metragem,
                    logradouro=logradouro,
                    numero=numero,
                    numero_original=numero_original,
                    data_inicial=data_inicial,
                    data_final=data_final,
                    fonte=fonte,
                    autor_da_alimentacao=autor_da_alimentacao,
                    data=data
                )
                obj.save()
                new_records.append(i)


        if existing_records:
            existing_records_msg = ', '.join(f"line {line}" for line in existing_records)
            message = f"The following records already exist in the table: {existing_records_msg}"
            return render(request, 'empty.html', {'message': message})

        return render(request, 'empty.html', {'success': 'Dados enviados'})

    return render(request, 'empty.html')





import csv
from django.shortcuts import render
from .models import MyModel

def upload_csv2(request):
    if request.method == 'POST':
        csv_data = request.FILES['csv_file']
        if not csv_data.name.endswith('.csv'):
            return render(request, 'upload.html', {'error': 'Please upload a CSV file.'})

        decoded_data = csv_data.read().decode('utf-8')
        csv_reader = csv.reader(decoded_data.splitlines(), delimiter=';')  # Use semicolon as the separator
        next(csv_reader)  # Skip header row if it exists

        for row in csv_reader:
            field1 = row[0]
            field2 = row[1]
            # Add more fields as needed

            obj = MyModel(
                field1=field1,
                field2=field2,
                # Assign other fields as necessary
            )

            obj.save()

        return render(request, 'upload.html', {'success': 'Data imported successfully.'})

    return render(request, 'upload.html')




