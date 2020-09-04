from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Images, Money
from .forms import ImageForm, DiscountForm

# View to render main page
def home_view(request):
    queryset = Images.objects.all()
    money = Money.objects.get(id=1)
    form = DiscountForm(request.POST or None, instance=money)

    # Calculate the total with discount applied
    discount_total = float(money.total) * (1 - (float(money.discount) * 0.01))

    # Save the form discount value if valid
    if form.is_valid():
        form.save()
        return redirect(reverse('home'))

    context = {
        "object_list": queryset,
        "money": money,
        "discount_total": discount_total,
        "form": form
    }
    return render(request, "home.html", context)

# View to create new image to sell
def create_view(request):
    form = ImageForm(request.POST, request.FILES)

    if form.is_valid():
        form.save()
        return redirect(reverse('home'))
    
    context = {
        'form': form
    }

    return render(request, "create.html", context)

# View to delete an image from the database
def delete_view(request, id):
    obj = get_object_or_404(Images, id=id)

    if request.method=="POST":
        obj.delete()
        return redirect(reverse('home'))

    context = {
        'object': obj
    }
    return render(request, "delete.html", context)

# View to sell an image and update the money earned
def sell_view(request, id):
    obj = get_object_or_404(Images, id=id)
    money = Money.objects.get(id=1)
    
    # When selling an image, its quantity decreases and earnings increases by the image price
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

# View to reset the earnings and discount values
def reset_view(request):
    money = Money.objects.get(id=1)

    money.total = 0
    money.discount = 0
    money.save()

    context = {
        'money': money
    }

    return render(request, "reset.html", context)