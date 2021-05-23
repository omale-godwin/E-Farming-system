from django.shortcuts import render, redirect
from .models import Listing
from django.shortcuts import get_object_or_404, render
from django.contrib import messages, auth

# Create your views here.
def searches(request):

#     queryset_list = Listing.objects.order_by('-list_date')

#    # Keywords
#     if 'keywords' in request.GET:
#         keywords = request.GET['keywords']
#     if keywords:
#       queryset_list = queryset_list.filter(description__icontains=keywords)

#     # City
#     if 'city' in request.GET:
#         city = request.GET['city']
#     if city:
#       queryset_list = queryset_list.filter(city__iexact=city)

#     # State
#     if 'state' in request.GET:
#         state = request.GET['state']
#     if state:
#       queryset_list = queryset_list.filter(state__iexact=state)

#     # Bedrooms
#     if 'bedrooms' in request.GET:
        
#         bedrooms = request.GET['bedrooms']
#     if bedrooms:
#         queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

#     # Price
#     if 'price' in request.GET:
#         price = request.GET['price']
#     if price:
#       queryset_list = queryset_list.filter(price__lte=price)

#     context = {
#     'state_choices': 'state_choices',
#     'bedroom_choices': 'bedroom_choices',
#     'price_choices': 'price_choices',
#     'listings': queryset_list,
#     'values': request.GET
#   }
    return render(request, 'listings/searches.html')

def listings(request):
    return render(request, 'listings/listings.html')


def listing(request, listing_id):
  listing = get_object_or_404(Listing, pk=listing_id)

  context = {
    'listing': listing
  }

  return render(request, 'listings/listing.html', context)

def upload(request):
    if request.method == 'POST' and request.FILES['photo_main'] and request.FILES['photo_1']:
        title = request.POST['title']
        price = request.POST['price']
        quanity = request.POST['quantity']
        description = request.POST['description']
        photo_main = request.FILES['photo_main']
        photo_6 = request.FILES['photo_1']
        date = request.POST['date']
        


        listingdata = Listing(title=title, description=description, price=price,
         quantity=quanity, photo_main=photo_main, photo_6=photo_6, list_date=date, user = request.user)
        listingdata.save()
        messages.success(request, 'successfully')
        return redirect('dashboard')
    else:
        print(request.user.username)
        return render(request, 'listings/upload.html')


    return render(request, 'listings/upload.html')


