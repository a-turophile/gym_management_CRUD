from django.shortcuts import render, redirect
from .forms import gymForm
from .models import gym
from django.views.generic import ListView, DetailView, UpdateView
'''
# Create your views here.
class Member_list(ListView):
    model = gym
    template_name = 'list.html'

class Member_register(UpdateView):
    model = gym
    template_name = 'register.html' '''

def member_list(request):
    context = {'members_list': gym.objects.all()}
    return render(request, "list.html", context)


def register(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = gymForm()
        else:
            member = gym.objects.get(pk=id)
            form = gymForm(instance=member)
        return render(request, "register.html", {'form': form})
    else:
        if id == 0:
            form = gymForm(request.POST, request.FILES)
        else:
            member = gym.objects.get(pk=id)
            form = gymForm(request.POST, request.FILES, instance = member)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

        return redirect('/list/')

def member_delete(request,id):
    member = gym.objects.get(pk=id)
    member.delete()
    return redirect('/list/')


