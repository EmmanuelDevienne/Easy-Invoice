from django.shortcuts import render
from django.views import View


class Dashboard(View):
    @staticmethod
    def get(request):
        return render(request, 'invoice/dashboard.html')
