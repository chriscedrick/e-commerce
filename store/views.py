from itertools import product
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from store.form import ContactForm,CommentSection
from .models import *

# Create your views here.

def home(request):
    trending_products = Product.objects.filter(trending=1)
    products = Product.objects.filter(status=0)
    context = {'trending_products' :trending_products , 'products' :products}
    return render(request, 'store/index.html', context)

def collections(request):
    category = Category.objects.filter(status=0)
    context ={'category' :category}
    return render(request, 'store/collections.html', context)

def collectionsview(request, slug):
    if(Category.objects.filter(slug=slug, status=0)):
        products = Product.objects.filter(category__slug=slug)
        category_name = Category.objects.filter(slug=slug).first()
        context = {'products' :products, 'category_name' :category_name }
        return render(request, 'store/products/index.html', context)
    else:
        messages.warning(request, "No such category found")
        return redirect('collections')

def productview(request, cate_slug, prod_slug, prod_id):
    if(Category.objects.filter(slug=cate_slug, status=0)):
        if(Product.objects.filter(slug=prod_slug, status=0)):
            products = Product.objects.filter(slug=prod_slug, status=0).first
            comment = Comment.objects.filter(product_id=prod_id)
            context = {'products' :products , 'comment':comment}
        else:
            messages.error(request, "No such product found")
            return redirect('collections')
    else:
        messages.error(request, "No such category found")
        return redirect('collections')
    if request.method == 'POST':
        commentSection = CommentSection(request.POST)
        if commentSection.is_valid:
            commentSection.save()
            product = commentSection.cleaned_data.get('product')
        else:
            commentSection = CommentSection()
    return render(request, 'store/products/view.html', context)

def productlistAjax(request):
    products = Product.objects.filter(status=0).values_list('name', flat=True)
    productslist = list(products)
    
    return JsonResponse(productslist, safe=False)

def searchproduct(request):
    if request.method == 'POST':
        searchedterm = request.POST.get('productsearch')
        if searchedterm == "":
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            product = Product.objects.filter(name__contains=searchedterm).first()
            
            if product:
                return redirect('collections/'+product.category.slug+'/'+product.slug+'/'+str(product.id))
            else:
                messages.info(request, "No product matched your search")
                return redirect(request.META.get('HTTP_REFERER'))
            
    return redirect(request.META.get('HTTP_REFERER'))

def contact(request):
    if request.method == 'POST':
        contactForm = ContactForm(request.POST)
        if contactForm.is_valid:
            contactForm.save()
            fname = contactForm.cleaned_data.get('fname')
            return redirect(contact)
        else:
            contactForm = ContactForm()
    return render(request, 'store/contact.html')

def about(request):
    return render(request, 'store/about.html')

def privacy(request):
    return render(request, 'store/privacy.html')

def terms(request):
    return render(request, 'store/terms.html')