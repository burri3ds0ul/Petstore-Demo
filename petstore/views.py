from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import PostPet
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    return render(request, 'petstore/home.html')


def about(request):
    context = {
        'petstores' : PostPet.objects
    }
    
    return render(request, 'petstore/about.html', context)

class PostPetListView(ListView):
    model = PostPet
    template_name = 'petstore/about.html'
    context_object_name = 'petstores'
    ordering = ['-pet_DOB']
    paginate_by = 3

class UserPostPetListView(ListView):
    model = PostPet
    template_name = 'petstore/user_posts.html'
    context_object_name = 'petstores'
    ordering = ['-pet_DOB']
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return PostPet.objects.filter(poster=user).order_by('-pet_DOB')
    

class PostPetDetailView(DetailView):
    model = PostPet


class PostPetCreateView(LoginRequiredMixin, CreateView):
    model = PostPet
    fields = ['pet', 'pet_name', 'pet_gender', 'pet_breed', 'pet_color', 'pet_detail', 'pet_DOB', 'image']

    def form_valid(self, form):
        form.instance.poster = self.request.user
        return super().form_valid(form)

class PostPetUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PostPet
    fields = ['pet', 'pet_name', 'pet_gender', 'pet_breed', 'pet_color', 'pet_detail', 'pet_DOB', 'image']

    def form_valid(self, form):
        form.instance.poster = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        petstores = self.get_object()
        if self.request.user == petstores.poster:
            return True
        return False

class PostPetDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PostPet
    success_url = '/'

    def test_func(self):
        petstores = self.get_object()
        if self.request.user == petstores.poster:
            return True
        return False
        

def contact(request):
    if request.method == 'POST':
        message_name = request.POST['name'] 
        message_email = request.POST['email']
        message_subject = request.POST['subject']
        message = request.POST['message']
        send_mail(message_email, 
        message, 
        settings.EMAIL_HOST_USER, 
        ['nabinkhanal128@gmail.com'], 
        fail_silently=False)
        return render(request, 'petstore/contact.html', {'message':message_subject})

    else:
        return render(request, 'petstore/contact.html')

