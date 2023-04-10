from django.shortcuts import render
from yn_museum.models import Order, Visitor


def Tatalshow(request):
    if request.method == "GET":
        Order_count = Order.objects.count()
        Visitor_count = Visitor.objects.count()
        context = {'Order_count': Order_count, 'Visitor_count': Visitor_count}
        return render(request, 'Total.html', context)
# Create your views here.
