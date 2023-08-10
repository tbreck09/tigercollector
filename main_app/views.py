from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tiger, Toy
from .forms import FeedingForm


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def tigers_index(request):
    tigers = Tiger.objects.filter(user=request.user)
    return render(request, 'tigers/index.html', {
      'tigers' : tigers  
    })

@login_required
def tigers_detail(request, tiger_id):
    tiger = Tiger.objects.get(id=tiger_id)
    id_list = tiger.toys.all().values_list('id')
    toys_tiger_doesnt_have = Toy.objects.exclude(id__in=id_list)
    feeding_form = FeedingForm()
    return render(request, 'tigers/detail.html', { 'tiger' : tiger, 'feeding_form': feeding_form, 'toys': toys_tiger_doesnt_have })


class TigerCreate(LoginRequiredMixin, CreateView):
    model = Tiger
    fields = ['name', 'species', 'description']
    
   

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TigerUpdate(LoginRequiredMixin, UpdateView):
    model = Tiger
    fields = ['species', 'description',]

class TigerDelete(LoginRequiredMixin, DeleteView):
    model = Tiger
    success_url = '/tigers'

@login_required
def add_feeding(request, tiger_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.tiger_id = tiger_id
        new_feeding.save()
    return redirect('detail', tiger_id=tiger_id)

class ToyList(LoginRequiredMixin, ListView):
    model = Toy

class ToyDetail(LoginRequiredMixin, DetailView):
    model = Toy

class ToyCreate(LoginRequiredMixin, CreateView):
    model = Toy
    fields = '__all__'

class ToyUpdate(LoginRequiredMixin, UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin, DeleteView):
    model = Toy
    success_url = '/toys'

@login_required
def assoc_toy(request, tiger_id, toy_id):
    Tiger.objects.get(id=tiger_id).toys.add(toy_id)
    return redirect('detail', tiger_id=tiger_id)

@login_required
def unassoc_toy(request, tiger_id, toy_id):
    Tiger.objects.get(id=tiger_id).toys.remove(toy_id)
    return redirect('detail', tiger_id=tiger_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)



