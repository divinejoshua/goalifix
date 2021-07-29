from django import forms

from .models import Products, Bidder


class CreateProductForm(forms.ModelForm):

	class Meta:
		model = Products
		fields = ['brand', 'device', 'price', 'body', 'thumb']


class CreateBidForm(forms.ModelForm):

	class Meta:
		model = Bidder
		fields = ['name', 'price', 'phone', 'email']
		