from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.db.models import Q


def home(request):
    books = BookDataModel.objects.all()
    category =BookCategoryModel.objects.all()
    search_data =''
    category_data = None
    sort_data = None
    if request.method=='POST':
        search_data = request.POST.get('search_bar','')
        category_data =request.POST.get('category-select')
        sort_data = request.POST.get('sort-select')

        if category_data and category_data.isdigit():
            category_data = int(category_data)
            books=books.filter(book_category__Category_ID=category_data)

        if sort_data == "small":
            books = books.order_by('book_price')
        else:
            books = books.order_by('-book_price')

        if search_data:
            books = books.filter(Q(book_category__Category_Name__icontains=search_data)
                                 | Q(book_author__Username__icontains=search_data) | Q(book_name__icontains=search_data))

    return render (request,'home.html',{'books':books,'category':category,'search_data':search_data,'category_data':category_data,'sort_data':sort_data})


def login(request):
    if request.method=='POST':
        user_name = request.POST.get('user_email')
        user_pass = request.POST.get('userpass')
        user_data = AuthorDataModel.objects.filter(author_login=user_name,author_password=user_pass).first()
        if user_data is not None:
            request.session['user_id'] = user_data.User_ID
            return redirect('home')
        else:
            return render(request,'login.html')

    return render(request,'login.html')

def details(request,id):
    book_data = BookDataModel.objects.filter(book_id=id)
    user_data = request.session.get('user_id')
    book_obj = BookDataModel.objects.get(book_id=id)
    review_data = ReviewModal.objects.filter(product_id=book_obj)
    if request.method == "POST":
        order_quantity = request.POST.get('order_quantity')
        # product_id = BookDataModel.objects.get(book_id=id)
        if user_data is not None:
            user = AuthorDataModel.objects.get(User_ID=user_data)
        else:
            return redirect('login')
        if 'add_cart' in request.POST:
            cart_obj = AddToCartModel()
            cart_obj.user_id = user
            cart_obj.product_id = book_obj
            cart_obj.cart_quantity = order_quantity
            cart_obj.save()
            return redirect('add_cart')
        elif 'buy_now' in request.POST:
            buy_obj = BuyNowModel()
            buy_obj.user_id = user
            buy_obj.product_id = book_obj
            buy_obj.buy_quantity = order_quantity
            buy_obj.save()
            return redirect('buy_now')
        # else:
        #     return HttpResponse("Invalid Post key")
    else:
        return render(request,'book_details.html',{'book_data':book_data,'review_data':review_data})



def add_cart(request):
    if 'user_id' in request.session:
        user_id = request.session.get('user_id')
        cart_details = AddToCartModel.objects.filter(user_id=user_id)
        return render(request,'add_cart.html',{'cart_details':cart_details})
    else:
        return redirect('login')

def buy_now(request):
    if 'user_id' in request.session:
        user_id = request.session.get('user_id')
        buy_data = BuyNowModel.objects.filter(user_id=user_id)
        return render(request,'buy_now.html',{'buy_data':buy_data})
    else:
        return redirect('login')

def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('home')

def remove(request,id):
    cart_obj = AddToCartModel.objects.get(cart_id=id)
    cart_obj.delete()
    return redirect('add_cart')

def review_part(request,id):
    book_obj = BookDataModel.objects.get(book_id=id)
    user_data = request.session.get('user_id')
    if request.method=='POST':
        review_data = request.POST.get('review-field')
        if user_data is not None:
            user_obj = AuthorDataModel.objects.get(User_ID=user_data)
        else:
            return redirect('login')
        review_obj = ReviewModal()
        review_obj.user_id = user_obj
        review_obj.product_id = book_obj
        review_obj.review_content=review_data
        review_obj.save()

        return redirect('book_data',id=id)


