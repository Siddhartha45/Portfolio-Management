from django.shortcuts import render

from .models import PortfolioUser


def port(request):
    user = PortfolioUser.objects.get(id=1)
    context = {
        'user': user,
    }
    return render(request, 'index.html', context)