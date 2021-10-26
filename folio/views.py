from django.shortcuts import render
from folio.models import Folio



def folio(request):
    model = Folio
    folio = Folio.objects.all()
    context = {'folios': folio}
    return render(request,'folio/index.html',context)

