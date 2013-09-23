#from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from restaurants import models, forms


def home(request):
    return render(request, 'home.html', {'title': 'home'})


def contact(request):
    '''Page stating our contact information'''
    return render(request, 'contact.html', {'title': 'contact'})


def restaurant_list(request):
    context = {'title': 'Restaurants',
                    'restaurants': models.Restaurant.objects.all()
                    }
    return render(request, 'restaurant_list.html', context)


def restaurant_details(request, pk):
    restaurant =  get_object_or_404(models.Restaurant, pk=pk)
    context = {
        'title': 'Restaurant Detail',
        'restaurant': restaurant,
        'reviews': restaurant.review_set.all()
    }
    return render(request, 'restaurant_detail.html', context)


def write_review(request, pk):
    restaurant =  get_object_or_404(models.Restaurant, pk=pk)
    if request.method == 'GET':
        form = forms.ReviewForm()
    else:
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.restaurant = restaurant
            review.save()
            return redirect('restaurant_detail', restaurant.pk)
    return render(request, 'write_review.html', {
            'title': 'Restaurant Detail',
            'restaurant': restaurant,
            'form': forms.ReviewForm()
        })
