from urllib import request
from django.shortcuts import render

# Create your views here.
# chatbot/views.py

from django.http import JsonResponse

from    chatbot_app.utils import generate_response

def chatbot_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')  # Assuming user input is sent via POST request
        # print('request', request.POST)
        # print('output', user_input)
        response = generate_response(user_input)  # Call your existing chatbot logic to generate a response
        # response = 'Hi Arsath'
        return JsonResponse({'response': response})  # Return the response as JSON
    else:
        return render(request, 'chatbot_ui.html')  # Return an error response for non-POST requests
    
def pdf_view(request):
    return render(request, 'pdf_view.html')
