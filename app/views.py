from django.shortcuts import render

from tablib import Dataset

def simple_upload(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def pdf(request):
    return render(request, "pdf.html")


def certificate(request):
    import pdfkit
    pdfkit.from_url('http://127.0.0.1:8000/app/', 'out.pdf')
    return render(request, "certificate.html")



