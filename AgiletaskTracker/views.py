from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Card
from django.views.generic import ListView, DetailView, CreateView , UpdateView , DeleteView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse



def home(request):


    context = {'posts': Card.objects.all()
    }

    return render(request,'AgiletaskTracker/home.html',context)
    


class UserTasks(ListView):
    model = Card
    template_name = 'AgiletaskTracker/home.html'
    context_object_name = 'posts'


    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Card.objects.filter(assignee=user).order_by('-date_created')


    
class CardCreateView(LoginRequiredMixin, CreateView):
    model = Card
    template_name = 'AgiletaskTracker/post_form.html'
    fields = ['title', 'status', 'priority', 'assignee']
    # success_url = reverse('tracker-home')

    def form_valid(self, form):
        #form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('tracker-home')

class CardDetailView(DetailView):
    model = Card