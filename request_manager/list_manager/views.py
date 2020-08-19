from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Requests


@login_required(login_url='login')
def home(request):

    data = Requests.objects.filter(user=request.user).order_by('-id')


    context = {'data': data}

    return render(request, 'app/home.html', context)


@login_required(login_url='login')
def newRequests(request):
    if request.method == 'POST':
        user = request.user
        type = request.POST.getlist('check')
        desc = request.POST.get('desc')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pin = request.POST.get('pin')
        country = request.POST.get('country')
        number = request.POST.get('number')
        req = Requests(user=user,type=type, description=desc, city=city,state=state, pin=pin, phone='+' + str(country) + str(number))

        # req.save()
        # return render(request, 'app/requests.html', {'message' : 'New Request Sent Successfully!! '})

        try:
            req.save()
            return render(request, 'app/requests.html', {'message' : 'New Request Sent Successfully!! '})

        except:
            return render(request, 'app/requests.html', {'message': 'Request Failed. '})

    if request.method == 'GET':
        return render(request, 'app/requests.html')

@login_required(login_url='login')
def requestById(request,id):

    data = Requests.objects.get(id=id)


    print(request.user, data.user)

    if str(request.user) == str(data.user):
        return render(request, 'app/requestbyid.html',{'data' : data})
    else:
        return render(request, 'app/requests.html', {'message': 'Something went wrong!!' })
