from django.shortcuts import render


def today(request):
    household = request.user.inhabitant.household
    return render(request, 'today.html', locals())
