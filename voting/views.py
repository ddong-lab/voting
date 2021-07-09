from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.template import context
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from .forms import CheckRollForm
from .models import Student, Candidate, Vote
import openpyxl
import json


class StudentsListView(ListView):
    model = Student
    template_name_suffix = '_list'


class CandidatesListView(ListView):
    model = Candidate
    template_name_suffix = '_list'


class StudentAddView(CreateView):
    model = Student
    fields = ['s_grade', 's_class', 's_birth', 's_name']
    success_url = reverse_lazy('stdList')
    template_name_suffix = '_add'


class CandidateAddView(CreateView):
    model = Candidate
    fields = ['c_no', 'c_grade', 'c_class', 'c_name']
    success_url = reverse_lazy('cndList')
    template_name_suffix = '_add'


class StudentEditView(UpdateView):
    model = Student
    fields = ['s_grade', 's_class', 's_birth', 's_name']
    success_url = reverse_lazy('stdList')
    template_name_suffix = '_edit'


class CandidateEditView(UpdateView):
    model = Candidate
    fields = ['c_no', 'c_grade', 'c_class', 'c_name']
    success_url = reverse_lazy('cndList')
    template_name_suffix = '_edit'


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('stdList')
    template_name_suffix = '_delete'


class CandidateDeleteView(DeleteView):
    model = Candidate
    success_url = reverse_lazy('cndList')
    template_name_suffix = '_delete'


class CheckRollFormView(FormView):
    form_class = CheckRollForm
    template_name = 'voting/checkRoll.html'

    def form_valid(self, form):
        return HttpResponseRedirect('/admin/stdList')


def studentsDelete(request):
    if "POST" == request.method:
        Student.objects.all().delete()
        return render(request, 'voting/student_list.html', {})
    else:
        return render(request, 'voting/student_deleteAll.html', {})


def studentsAdd(request):
    if "GET" == request.method:
        return render(request, 'voting/students_add.html', {})
    else:
        excel_file = request.FILES["excel_file"]
        # you may put validations here to check extension or file size
        wb = openpyxl.load_workbook(excel_file)
        # getting a particular sheet by name out of many sheets
        worksheet = wb["Sheet1"]
        print(worksheet)
        # excel_data = list()
        # iterating over the rows and
        # getting value from each cell in row
        cnt = 0
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            # excel_data.append(row_data)
            if cnt != 0:
                birth = row_data[2].replace(".", "")
                birth = birth[2:]
                stdData: Student = Student(s_grade=row_data[0], s_class=row_data[1], s_birth=birth, s_name=row_data[3])
                stdData.save()
            cnt += 1
        return render(request, 'voting/student_list.html', {})
        # return render(request, 'voting/students_add.html', {"excel_data": excel_data})
