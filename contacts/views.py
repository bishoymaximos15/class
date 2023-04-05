from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Contact

# Create your views here.
class ContactList(ListView): 
	model = Contact




class Contactdetail(DetailView ):   
  model = Contact
  

  