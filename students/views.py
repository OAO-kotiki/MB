import csv
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets
from django.urls import reverse_lazy

from .models import Student, StudentBulkUpload
from finance.models import Invoice

@login_required
def student_list(request):
  students = Student.objects.all()
  return render(request, 'students/student_list.html', {"students":students})


class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = "students/student_detail.html"

    def get_context_data(self, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        context['Оплата'] = Invoice.objects.filter(Студент=self.object)
        return context


class StudentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Student
    fields = '__all__'
    success_message = "Новый студент добавлен успешно."

    def get_form(self):

        form = super(StudentCreateView, self).get_form()
        form.fields['Дата_поступления'].widget = widgets.DateInput(attrs={'type': 'date'})
        form.fields['Дата_рождения'].widget = widgets.DateInput(attrs={'type': 'date'})
        form.fields['Адрес'].widget = widgets.Textarea(attrs={'rows': 2})
        form.fields['Другое'].widget = widgets.Textarea(attrs={'rows': 2})
        return form


class StudentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Student
    fields = '__all__'
    success_message = "Запись прошла успешно."

    def get_form(self):
        form = super(StudentUpdateView, self).get_form()
        form.fields['Дата_рождения'].widget = widgets.DateInput(attrs={'type': 'date'})
        form.fields['Дата_поступления'].widget = widgets.DateInput(attrs={'type': 'date'})
        form.fields['Адрес'].widget = widgets.Textarea(attrs={'rows': 2})
        form.fields['Другое'].widget = widgets.Textarea(attrs={'rows': 2})
        return form


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('student-list')


class StudentBulkUploadView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = StudentBulkUpload
    template_name = 'students/students_upload.html'
    fields = ['csv_file']
    success_url = '/student/list'
    success_message = 'Студент успешно загружен'

@login_required
def downloadcsv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="student_template.csv"'

    writer = csv.writer(response)
    writer.writerow(['registration_number', 'surname',
                     'firstname', 'other_names', 'gender', 'parent_number', 'address', 'current_class'])

    return response