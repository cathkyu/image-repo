from django import forms
from .models import Images, Money

# Image form to handle creating a new image object, saves to db
class ImageForm(forms.ModelForm):

    class Meta:
        model = Images
        fields = [
            'title',
            'price',
            'quantity',
            'image'
        ]

# Discount form to handle editing the discount value 
class DiscountForm(forms.ModelForm):

    discount = forms.IntegerField(
        label='Discount (%)'
    )

    class Meta:
        model = Money
        fields = [
            'discount'
        ]
    
    # function to ensure discount is a valid value
    def clean_discount(self, *args, **kwargs):
        discount = self.cleaned_data.get("discount")
        if discount >= 0 and discount <= 100:
            return discount
        else:
            raise forms.ValidationError("Discount must be between 0 and 100%")