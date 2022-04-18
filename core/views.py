from django.shortcuts import render
from django.views.generic import (
	View,
)

class AdministrationHomePageView(View):
	template_name = 'base.html'
	
	def get(self, request):
		context = {
			'title'	:	'Administration Dashboard'
		}
		return render(request, self.template_name, context)