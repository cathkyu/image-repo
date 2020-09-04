from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Images, Money
from .forms import ImageForm

# Create your views here.
def home_view(request):
    queryset = Images.objects.all()
    money = Money.objects.get(id=1)

    discount_total = float(money.total) * (1 - (float(money.discount) * 0.01))

    context = {
        "object_list": queryset,
        "money": money,
        "discount_total": discount_total
    }
    return render(request, "home.html", context)

def create_view(request):
    # form = ImageForm(request.POST or None)
    form = ImageForm(request.POST, request.FILES)

    if form.is_valid():
        form.save()
        return redirect(reverse('home'))
    
    context = {
        'form': form
    }

    return render(request, "create.html", context)

def delete_view(request, id):
    obj = get_object_or_404(Images, id=id)

    if request.method=="POST":
        obj.delete()
        return redirect(reverse('home'))

    context = {
        'object': obj
    }
    return render(request, "delete.html", context)

def sell_view(request, id):
    obj = get_object_or_404(Images, id=id)
    money = Money.objects.get(id=1)
    
    if obj.quantity > 0:
        message = "Sell successful!"
        obj.quantity -= 1
        obj.save()

        money.total += obj.price
        money.save()
    else:
        message = "Sell failed, insufficient quantity."
        
    context = {
        'object': obj,
        'message': message
    }

    return render(request, "sell.html", context)
