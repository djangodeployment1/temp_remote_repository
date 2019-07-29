from django.shortcuts import render

def home_page_view(request):
    return render(request,'base_home.html')


def contact_page_view(request):
    return render(request,'base_contact.html')

def services_page_view(request):
    return render(request,'base_service.html')

def feedback_page_view(request):
    return render(request,'base_feedback.html')
