from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import CreateProductForm, CreateBidForm
from .models import Products, Bidder, BidStatus
from decouple import config
from accounts.models import Account


# Create your views here.

def home_view(request):

	context = {}

	return render(request, "main/index.html", context)



def home_inner_view(request):

	context = {}
	phoneNumber = config('PhoneNumber')
	context['swap'] = "https://api.whatsapp.com/send/?phone=%2B"+phoneNumber+"&text=Hi,+I+want+to+swap+a+device+"
	context['sell'] = "https://api.whatsapp.com/send/?phone=%2B"+phoneNumber+"&text=Hi,+I+want+to+sell+a+device+"
	context['fix'] = "https://api.whatsapp.com/send/?phone=%2B"+phoneNumber+"&text=Hi,+I+want+to+fix+a+device+"

	return render(request, "main/home.html", context)


def phone_view(request):

	context = {}
	phoneNumber = config('PhoneNumber')
	context['phone'] = "https://api.whatsapp.com/send/?phone=%2B"+phoneNumber+"&text=Hi,+I+want+to+make+enquires+for+a+Phone+"

	return render(request, "main/phones.html", context)


def laptop_view(request):

	context = {}
	phoneNumber = config('PhoneNumber')
	context['phone'] = "https://api.whatsapp.com/send/?phone=%2B"+phoneNumber+"&text=Hi,+I+want+to+make+enquires+for+a+Laptop+"

	return render(request, "main/laptops.html", context)



def accessories_view(request):

	context = {}
	phoneNumber = config('PhoneNumber')
	context['phone'] = "https://api.whatsapp.com/send/?phone=%2B"+phoneNumber+"&text=Hi,+I+want+to+an+Accessory+"

	return render(request, "main/accessories.html", context)



def bid_view(request):

	context = {}
	status = BidStatus.objects.all().first()
	user = Account.objects.filter(email=request.user)

	if status.active_bid:
		product = Products.objects.all()
	elif not status.active_bid and user:
		product = Products.objects.all()
		context['adminView'] = True
	else:
		product = None
		
	context['product'] = product


	form = CreateBidForm(request.POST or None, request.FILES or None)
	if request.method == 'POST':   
		if int(request.POST['price']) > int(request.POST['current']):

			item = Products.objects.get(id=request.POST['id'])

			if form.is_valid():
				obj = form.save(commit=False)
				obj.product = item

				item.bidPrice = request.POST['price']
				item.save()
				obj.save()
				form = CreateBidForm()
				context['success'] = "Added successfully"
			else:
				context['error'] = "Error submitting form"
		else:
			context['error'] = "Your price must be higher than current price"
	context['form'] = form

	return render(request, "main/bid.html", context)





@login_required(login_url="/login/")
def add_bid_view(request):

	context = {}
	bidders = Bidder.objects.all()
	context['bidders'] = bidders


	user = Account.objects.get(email=request.user)
	status = BidStatus.objects.all().first()


	form = CreateProductForm(request.POST or None, request.FILES or None)
	if request.method == 'POST':
		if request.POST.get("add-bid"):
			if form.is_valid():
				obj = form.save(commit=False)
				obj.bidPrice = request.POST['price']
				obj.save()
				form = CreateProductForm()
				return redirect("/bid")
			else:
				context['error'] = "Error submitting form"
		
		if request.POST.get("bid-status"):
			status.active_bid = not status.active_bid
			status.save()


		if request.POST.get("delete"):
			bidders.delete()

	context['bidStatus'] = status.active_bid	
	context['product'] = bidders.count()
	context['form'] = form

	return render(request, "main/addbid.html", context)
