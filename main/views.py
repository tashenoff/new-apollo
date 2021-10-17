from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import Feedback
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import Http404
from django.conf import settings
def form(request):

    if request.method == 'POST':
        form = Feedback(request.POST)
        if form.is_valid():
            form.save()
            try:
                subject = 'Заявка с сайта'
                form_data = form.cleaned_data
                print(form_data)
                html_message = render_to_string('main/mail.html', {'form_data': form_data})
                plain_message = strip_tags(html_message)
                from_email = settings.DEFAULT_FROM_EMAIL
                to = settings.RECIPIENTS_EMAIL
                send_mail(subject, plain_message, from_email, to, html_message=html_message)
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

