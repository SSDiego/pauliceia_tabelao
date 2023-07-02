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
                logradouro=submitted_data['logradouro'],
                livro_emplacamento=submitted_data['livro_emplacamento'],
                responsavel=submitted_data['responsavel'],
                dt_realizacao=submitted_data['dt_realizacao'],
                observacao=submitted_data['observacao'],
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
    writer.writerow(['Logradouro', 'Livro de Emplacamento', 'Responsável', 'Data de Realização', 'Observações'])

    forms = form_table.objects.all() 
    
    for form in forms:
        writer.writerow([form.logradouro, form.livro_emplacamento, form.responsavel, form.dt_realizacao, form.observacao])
    
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
            logradouro = row[0]
            livro_emplacamento = row[1]
            responsavel = row[2]
            dt_realizacao = row[3]
            observacao = row[4]

            # Check if the record already exists in the table
            if form_table.objects.filter(logradouro=logradouro, livro_emplacamento=livro_emplacamento, responsavel=responsavel, dt_realizacao=dt_realizacao, observacao=observacao).exists():
                existing_records.append(i)
            else:
                obj = form_table(
                    logradouro=logradouro,
                    livro_emplacamento=livro_emplacamento,
                    responsavel=responsavel,
                    dt_realizacao=dt_realizacao,
                    observacao=observacao
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




