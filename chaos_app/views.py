from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic 

from chaos_app.models import Person, Location, Relation


class HomeView(generic.TemplateView):
    template_name = 'home.html'


class PersonalNetView(generic.DetailView):
    model = Person
    template_name = 'net.html'

    def get_context_data(self, **kwargs):
        context = super(PersonalNetView, self).get_context_data(**kwargs)
        # Get the Person object
        person_obj = self.get_object()
        
        friends = person_obj.get_friends()
        bff = person_obj.get_bff()                                    

        context['friends'] = friends
        context['bff'] = bff
        
        # Final Exam mod here ...
        context['oldest'] = None # Replace None with data ???Hint look at the method for Person called get_oldest_friend
        return context


class NetView(generic.ListView):
    model = Person
    template_name = 'people.html'


