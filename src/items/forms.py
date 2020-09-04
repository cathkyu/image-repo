from django import forms
from .models import Images, Money

class ImageForm(forms.ModelForm):

    class Meta:
        model = Images
        fields = [
            'title',
            'price',
            'quantity',
            'image'
        ]

class DiscountForm(forms.ModelForm):

    discount = forms.IntegerField(
        label='Discount (%)'
    )

    class Meta:
        model = Money
        fields = [
            'discount'
        ]
    
    def clean_discount(self, *args, **kwargs):
        discount = self.cleaned_data.get("discount")
        if discount >= 0 and discount <= 100:
            return discount
        else:
            raise forms.ValidationError("Discount must be between 0 and 100%")