from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

# Create your views here.


class HomeView(TemplateView):
	template_name = 'home.html'

	def get_context_data(self, *args, **kwargs):
		context = {
					'companyName': 'Farm Fresh'}
		return context