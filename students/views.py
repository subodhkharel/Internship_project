from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student
from .forms import StudentForm

# Create your views here.


class StudentListView(ListView):
    model = Student
    template_name = "student_list.html"
    context_object_name = "students"


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "student_form.html"
    success_url = reverse_lazy("student_list")


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "student_form.html"
    success_url = reverse_lazy("student_list")


class StudentDeleteView(DeleteView):
    model = Student
    template_name = "student_confirm_delete.html"
    success_url = reverse_lazy("student_list")
