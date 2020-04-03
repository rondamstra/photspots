from django.shortcuts import render
from django.views.generic import (View, TemplateView,
                                ListView, DetailView,
                                CreateView, UpdateView,
                                DeleteView)

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'