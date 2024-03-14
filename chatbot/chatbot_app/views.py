from urllib import request
from django.shortcuts import render

# Create your views here.
# chatbot/views.py

from django.http import JsonResponse
from chatbot_app.forms import NameForm

from chatbot_app.utils import generate_response

def name_input_view(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            print('Name:', name)  # Print the name in the console
            response = generate_response(name)
            print('response', response)
    else:
        response = 'Welcome!!'
        form = NameForm()
    return render(request, 'name_input.html', {'form': form, 'response': response})

