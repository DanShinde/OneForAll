import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ExcelUploadForm, TaskForm
import pandas as pd
import numpy as np
from .models import Task
from django.db import transaction
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required('planner.change_task', raise_exception=True)
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'planner/task_list.html', {'tasks': tasks})


@login_required
@permission_required('planner.change_task', raise_exception=True)
def task_edit(request, task_id):
    task = get_object_or_404(Task, task_id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('task_list'))
    else:
        form = TaskForm(instance=task)
    return render(request, 'planner/task_edit.html', {'form': form})

def upload_excel(request):
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['excel_file']
            try:
                df = pd.read_excel(excel_file)
                df['Created Date'] = pd.to_datetime(df['Created Date'], format='%m/%d/%Y', errors='coerce')
                df['Start Date'] = pd.to_datetime(df['Start Date'], format='%m/%d/%Y', errors='coerce')
                df['Due Date'] = pd.to_datetime(df['Due Date'], format='%m/%d/%Y', errors='coerce')
                df['Completed Date'] = pd.to_datetime(df['Completed Date'], format='%m/%d/%Y', errors='coerce')
                #print(df['Start Date'])
                df['Created Date'] = df['Created Date'].fillna(pd.NaT)    
                df['Start Date'] = df['Start Date'].fillna(pd.NaT)   
                df['Due Date'] = df['Due Date'].fillna(pd.NaT)   
                df['Completed Date'] = df['Completed Date'].fillna(pd.NaT)            
                #print(df['Start Date'])
                df = df.replace({np.nan: None})
                validate_excel_data(df)
                task_list = []
                for index, row in df.iterrows():
                    task = Task(
                        task_id=row['Task ID'],
                        task_name=row['Task Name'],
                        bucket_name=row['Bucket Name'],
                        progress=row['Progress'],
                        priority=row['Priority'],
                        assigned_to=row['Assigned To'],
                        created_by=row['Created By'],
                        created_date=row['Created Date'],
                        start_date=row['Start Date'],
                        due_date=row['Due Date'],
                        is_recurring=row['Is Recurring'],
                        late=row['Late'],
                        completed_date=row['Completed Date'],
                        completed_by=row['Completed By'],
                        completed_checklist_items=row['Completed Checklist Items'],
                        checklist_items=row['Checklist Items'],
                        labels=row['Labels'],
                        description=row['Description'],
                    )
                    task_list.append(task)
                with transaction.atomic():
                    Task.objects.bulk_create(task_list)
                return HttpResponseRedirect(reverse('upload_success'))
            except Exception as e:
                form.add_error('excel_file', str(e))
    else:
        form = ExcelUploadForm()
    return render(request, 'planner/upload_excel.html', {'form': form})


def upload_success(request):
    return render(request, 'planner/upload_success.html')



def validate_excel_data(df):
    required_columns = ['Task ID', 'Task Name', 'Bucket Name', 'Progress', 'Priority', 'Assigned To', 'Created By', 'Created Date', 'Due Date']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing columns in Excel file: {', '.join(missing_columns)}")
    # Check if task_id is unique
    existing_task_ids = Task.objects.values_list('task_id', flat=True)
    if df['Task ID'].isin(existing_task_ids).any():
        raise ValueError('One or more task IDs in the uploaded excel file already exist in the database')
    return True

        
"""def validate_excel_data(df):
    # Check if all required columns are present
    required_columns = [        'Task ID',
        'Task Name',
        'Bucket Name',
        'Progress',
        'Priority',
        'Assigned To',
        'Created By',
        'Created Date',
        ]
    if not all(col in df.columns for col in required_columns):
        raise ValueError('The uploaded excel file is missing some required columns')

    # Check if task_id is unique
    existing_task_ids = Task.objects.values_list('task_id', flat=True)
    if df['task_id'].isin(existing_task_ids).any():
        raise ValueError('One or more task IDs in the uploaded excel file already exist in the database')"""