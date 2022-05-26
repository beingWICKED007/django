from email.message import EmailMessage
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages 
from django.db.models import Q
from django.views.generic import View

class BaseView(View):
    views = {}

# Create your views here.

class HomeView(BaseView):

	def get(self,request):
		
		self.views['category'] = HomeCategories.objects.all()
		self.views['product'] = HomeProduct.objects.all()

		return render(request,'index.html',self.views)



from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def product(request):
    categories = Category.objects.all()
    price = Price.objects.all()
    color = Color.objects.all()
    size = Size.objects.all()


    # variable name = request.GET.get('link_name')

    # if 

   
    CATID = request.GET.get('categories')
    PRICE = request.GET.get('price')
    COLOR = request.GET.get('color')
    SIZE = request.GET.get('size')
     

    if CATID:
        product = Product.objects.filter(categories=CATID)

    elif PRICE:
        product = Product.objects.filter(filter_price=PRICE)

    elif COLOR:
        product = Product.objects.filter(color=COLOR)

    elif SIZE:
        product = Product.objects.filter(size=SIZE)

    else:
        product = Product.objects.filter(status='Publish').order_by('-id')
     


    context = {
        'categories': categories,
        'price': price,
        'color':color,
        'size':size,
        'product':product,

    }

    return render(request,'product.html',context)
    



import random



# def signup(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         confirm_password = request.POST['confirm_password']


#         if password == confirm_password:
#             randomlist = random.sample(range(1000, 9999), 1)

#             if User.objects.filter(username = username).exists():
#                 messages.error(request,'The username is already used')
#                 return redirect('/signup')
                
#             elif User.objects.filter(email = email).exists():
#                 messages.error(request,'The email is already taken')
#                 return redirect('/signup')

#             else:
#                 user = User.objects.create_user(
#                     username = username,
#                     email = email,
#                     password = password,
#                 )
#                 user.save()

#                 User.objects.filter(username = username).update(is_active = False)

#                 code = Otp.objects.create(
# 					user = username,
# 					token = randomlist[0]
# 					)
# 				code.save()

#                 email = EmailMessage(
# 				    'Email verification code',
# 				    f'Please enter email verification code {randomlist[0]}',
# 				    'c6d2700b477494',
# 				    [email]
# 				    )
# 				email.send()

#                 messages.error(request,'The otp is sent to your email.')
# 				return redirect('/verify/')

#         else:
#             messages.error(request,'The password does not match')
#             return redirect('/signup/')
 
#     return render(request,'registration/register.html')








def signup(request):
	if request.method == "POST":
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		confirm_password = request.POST['confirm_password']

		if password == confirm_password:
			randomlist = random.sample(range(1000, 9999), 1)

			if User.objects.filter(username = username).exists():
				messages.error(request,'The username is already taken')
				return redirect('/signup')

			elif User.objects.filter(email = email).exists():
				messages.error(request,'The email is already taken')
				return redirect('/signup')
			else:
				user = User.objects.create_user(
					username = username,
					email = email,
					password = password
					)
				user.save()

				User.objects.filter(username = username).update(is_active = False)

				code = Otp.objects.create(
					user = username,
					code = randomlist[0]
					)
				code.save()

				email = EmailMessage(
				    'Email verification code',
				    f'Please enter email verification code {randomlist[0]}',
				    'c6d2700b477494',
				    [email]
				    )
				email.send()
				messages.error(request,'The otp is sent to your email.')
				return redirect('/otp/')
		else:
			messages.error(request,'The password does not match')
			return render(request,'registration/register.html')
	return render(request,'registration/register.html')


def otp(request):
    if request.method == 'POST':
        username = request.POST['username']
        code = request.POST['code']

        if Otp.objects.filter(code=code,user=username).exists():
            User.objects.filter(username = username).update(is_active = True)
            return redirect('/product/')

    return render(request,'registration/otp.html')






def login(request):

    return render(request,'registration/login.html')



from django.contrib.auth.decorators import login_required
@login_required
def cart(request,slug):
	if Cart.objects.filter(slug = slug,user=request.user.username,checkout = False).exists():
		quantity = Cart.objects.get(slug = slug,user=request.user.username,checkout = False).quantity
		price = Product.objects.get(slug = slug).price
		discounted_price = Product.objects.get(slug = slug).discounted_price
		quantity = quantity +1
		if discounted_price >0:
			original_price = discounted_price
			total = original_price*quantity
		else:
			total = price*quantity

		
		Cart.objects.filter(slug = slug,user=request.user.username,checkout = False).update(quantity = quantity,total = total)

	else:
		username = request.user.username
		price = Product.objects.get(slug = slug).price
		discounted_price = Product.objects.get(slug = slug).discounted_price
		if discounted_price >0:
			original_price = discounted_price
		else:
			original_price = price
		data = Cart.objects.create(
			user = username,
			slug = slug,
			items = Product.objects.filter(slug = slug)[0],
			total = original_price
			)
		data.save()

	return redirect('/cart')


def deletecart(request,slug):
	if Cart.objects.filter(slug = slug,user=request.user.username,checkout = False).exists():
		Cart.objects.filter(slug = slug,user=request.user.username,checkout = False).delete()

	return redirect('/cart')

def decreasecart(request,slug):
	if Cart.objects.filter(slug = slug,user=request.user.username,checkout = False).exists():
		quantity = Cart.objects.get(slug = slug,user=request.user.username,checkout = False).quantity
		if quantity >1:
			quantity = quantity -1
			Cart.objects.filter(slug = slug,user=request.user.username,checkout = False).update(quantity = quantity)
	return redirect('/cart')


 
def cart(request):

    cart_product = Cart.objects.filter(user=request.user.username,checkout = False)

    context = {
        'cart_product':cart_product
    }

    return render(request,'cart/cart-detail.html',context)

from django.core.mail import EmailMessage
from django.contrib import messages
 
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        data = Contact.objects.create (name = name,email = email,message = message,)
        data.save()

        email = EmailMessage(
            'Hello',
            'Hello thanks for the messaging us. We will get follow back to you!',
            'rdhimal229@gmail.com',
            [email],
            )
        email.send()
        return redirect('/')

    return render(request,'contact.html')



# def search(request):

#     if request.method == 'GET':
#         query = request.GET['query']

#         lookups = Q(name__icontains = query) | Q(description___icontains = query)
#         product = Product.objects.filter(lookups).distinct

#         context = {
#             'product':product
#         }


#     return render(request,'search.html',context)





class SearchView(BaseView):
    def get(self,request):
        self.views['categories'] = Category.objects.all()
        self.views['price'] = Price.objects.all()
        self.views['color'] = Color.objects.all()

        if request.method == 'GET':
            query = request.GET['query']

            lookups = Q(name__icontains = query) | Q(description__icontains = query)
            self.views['product'] = Product.objects.filter(lookups).distinct
        
        return render(request,'search.html',self.views)




class TestView(BaseView):
    def get(self,request):
        return render (request,'test.html')





def shop_detail(request):
    return render(request,'shop-details.html')










 

