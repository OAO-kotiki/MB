from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages

from .models import SiteConfig, AcademicSession, AcademicTerm, StudentClass, Subject
from .forms import SiteConfigForm, AcademicTermForm, AcademicSessionForm, StudentClassForm, SubjectForm, CurrentSessionForm


@login_required
def index_view(request):
  return render(request, 'corecode/index.html')

@login_required
def academic_terms_view(request):

  if request.method == 'POST':
    form = AcademicTermForm(request.POST)
    if form.is_valid() and form.has_changed():
      form.save()
      messages.success(request, 'Семестр успешно сохранен')
      return HttpResponseRedirect('Семестр')
  else:
    form = AcademicTermForm(queryset=AcademicTerm.objects.all())

  context = {"formset": form, "title": "Семестр"}
  return render(request, 'corecode/mgt_form.html', context)

@login_required
def academic_sessions_view(request):

  if request.method == 'POST':
    form = AcademicSessionForm(request.POST)
    if form.is_valid() and form.has_changed():
      form.save()
      messages.success(request, 'Сессия успешно сохранена')
      return HttpResponseRedirect('Сессия')
  else:
    form = AcademicSessionForm(queryset=AcademicSession.objects.all())

  context = {"formset": form, "title": "Сессия"}
  return render(request, 'corecode/mgt_form.html', context)

@login_required
def student_classes_view(request):

  if request.method == 'POST':
    form = StudentClassForm(request.POST)
    if form.is_valid() and form.has_changed():
      form.save()
      messages.success(request, 'Группа успешно сохранена')
      return HttpResponseRedirect('Группы')

  else:
    form = StudentClassForm(queryset=StudentClass.objects.all())

  context = {"formset": form, "title": "Группы"}
  return render(request, 'corecode/mgt_form.html', context)

@login_required
def subject_view(request):

  if request.method == 'POST':
    form = SubjectForm(request.POST)

    if form.is_valid() and form.has_changed():
      form.save()
      messages.success(request, 'Предмет успешно сохранён')
      return HttpResponseRedirect('Предметы')

  else:
    form = SubjectForm(queryset=Subject.objects.all())

  context = {"formset": form, "title": "Предметы"}
  return render(request, 'corecode/mgt_form.html', context)

@login_required
def current_session_view(request):

  if request.method == 'POST':
    form = CurrentSessionForm(request.POST)
    if form.is_valid():
      session = form.cleaned_data['current_session']
      term = form.cleaned_data['current_term']
      AcademicSession.objects.filter(name=session).update(current=True)
      AcademicSession.objects.exclude(name=session).update(current=False)
      AcademicTerm.objects.filter(name=term).update(current=True)
      AcademicTerm.objects.exclude(name=term).update(current=False)

  else:
    form = CurrentSessionForm(initial={
      "current_session": AcademicSession.objects.get(current=True),
      "current_term": AcademicTerm.objects.get(current=True)
    })


  return render(request, 'corecode/current_session.html', {"form":form})

@login_required
def developer(request):
  return render(request, 'corecode/developer.html')
