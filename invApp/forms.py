from django import forms

from .models import Product

class ProductForm(forms.Form):
    class Meta:
        models = Product
        fields = "__all__"

        labels = {
            "productId": "ProductId",
            "name" : "Name",
            "sku": "SKU",
            "price" : "Price",
            "quantity": "Quantity",
            "supplier": "Supplier"
        }

        widgets = {
            "productId": forms.NumberInput(attrs={"placeholder":"e.g. 1", "class":"form-control"}),
            "name" : forms.TextInput(attrs={"placeholder":"e.g. shirt", "class":"form-control"}),
            "sku": forms.TextInput(attrs={"placeholder":"XXX", "class":"form-control"}),
            "price": forms.NumberInput(attrs={"placeholder":"e.g. 5.99", "class":"form-control"}),
            "quantity": forms.NumberInput(attrs={"placeholder":"e.g. 6", "class":"form-control"}),
            "supplier": forms.TextInput(attrs={"placeholder":"JohnDeere", "class":"form-control"})
        }
