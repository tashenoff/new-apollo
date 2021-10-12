from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import Feedback
from django.core.mail import send_mail
from django.http import Http404
from django.conf import settings
def form(request):

    if request.method == 'POST':
        form = Feedback(request.POST)
        if form.is_valid():
            form.save()
            try:
                send_mail('Заявка с сайта', 'Вам пришло письмо, от имя: {0},\n номер: {1}  '.format(form.cleaned_data['firstName'], form.cleaned_data['phone']), 
                settings.DEFAULT_FROM_EMAIL, settings.RECIPIENTS_EMAIL, fail_silently=False)
            except Exception as err:
                raise Http404("Ошибка", err)
            return redirect('main:thanks')
    else:
        form = Feedback()
    
    return render(request, 'main/form.html', {'form' : form})


def index(request):
    return render(request, 'main/index.html')

def thanksForm(request):
    return render(request, 'main/thanks.html')

# def feedback(request):
#     return render(request, 'main/feedback.html')

