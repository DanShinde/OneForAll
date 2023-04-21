import pandas as pd
from io import BytesIO
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .funs import create_text_lists, createSCL, read_excel_file, create_text_lists8
from django.template.context_processors import csrf
from django.middleware.csrf import get_token
from django.contrib.auth.decorators import login_required


ALLOWED_EXTENSIONS = set(['xlsx'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def homeIO(request):
    return render(request, 'textgen/upload.html')


@login_required(login_url="/login")
def upload(request):
    context = {}
    if request.method == 'POST':
        file = request.FILES.get('file')
        type = int(request.POST.get('option'))
        if not file:
            messages.error(request, 'No file was uploaded')
            return render(request, 'textgen/upload.html', context= context)

        if not allowed_file(file.name):
            messages.error(request, 'File type is invalid, upload .xlsx file')
            return render(request, 'textgen/upload.html', context= context)

        data, sheet_names = read_excel_file(file)
        output = create_text_lists(data, type, sheet_names)
        xlsx_data = output.getvalue()
        file_name = "Test.xlsx"
        response = HttpResponse(xlsx_data, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        messages.success(request, 'File is accepted')
        return response


    context['csrf_token'] = get_token(request)
    return render(request, 'textgen/upload.html', context= context)


def upload8(request):
    context = {}
    context.update(csrf(request))
    if request.method == 'POST':
        file = request.FILES.get('file')
        type = int(request.POST.get('option'))
        if not file:
            messages.error(request, 'No file was uploaded')
            return render(request, 'textgen/upload.html', context= context)

        if not allowed_file(file.name):
            messages.error(request, 'File type is invalid, upload .xlsx file')
            return render(request, 'textgen/upload.html', context= context)

        raw = pd.ExcelFile(file)
        data, sheet_names = read_excel_file(raw)
        output = create_text_lists8(data, type, sheet_names)
        xlsx_data = output.getvalue()
        file_name = "Test.xlsx"
        response = HttpResponse(xlsx_data, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        messages.success(request, 'File is accepted')
        return response

    return render(request, 'textgen/upload.html', context=context)

def io_mapping(request):
    QBytes = request.POST.get('QBytes')
    SCLdata = createSCL(5, QBytes, 10)
    textData = SCLdata.getvalue()
    file_name = "SCL.txt"
    response = HttpResponse(textData, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    return response

def server_error(request):
    message = "An error has occurred"
    return render(request, 'textgen/Error.html', {'error': message})
