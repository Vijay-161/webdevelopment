from django import forms
from orderdetail.models import OrderDetail

class OrderDetailForm(forms.ModelForm):
    class Meta:
        model = OrderDetail

        fields = "__all__"
