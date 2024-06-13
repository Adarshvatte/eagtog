from django.shortcuts import render, redirect
from store.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as django_login
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from decimal import Decimal
from django.contrib import messages
from django.core.mail import send_mail
from django.db.models import Sum
from datetime import datetime, timedelta

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))


def home(request):
    cat_items = CatagoryItems.objects.all()
    products = Product.objects.all()
    categories = Category.objects.all()
    data = Review.objects.all()
    context = {
        "items" : cat_items,
        "products":products,
        "categories" :categories,
        "data" : data
    }
    return render(request, "index.html", context)

def base(request):
    return render(request, "base.html")

def features(request):
    return render(request, "features.html")

def featureFresh(request):
    return render(request, "freshAndOrg.html")

def freeDel(request):
    return render(request, "free.html")

def easyPay(request):
    return render(request, "easyPayment.html")

def categories(request):
    cat_items = CatagoryItems.objects.all()
    context = {
        "items" : cat_items
    }
    return render(request, "categories.html", context)

def product(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        "products":products,
        "categories" :categories
    }
    return render(request, "product.html", context)
    
def Search(request):
    query = request.GET.get("query")
    products = Product.objects.filter(name__icontains = query)
    context = {
        "products":products,
    }
    return render(request, "search.html", context)



def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")

        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "Username already exists")
            return render(request, "register.html")
        
        if pass1 != pass2:
            messages.error(request, "Passwords do not match. Please enter the same password.")
            return render(request, "register.html")

        customer = User.objects.create_user(username, email, pass1)
        customer.first_name = firstName
        customer.last_name = lastName
        customer.save()

        send_mail(
            subject="Welcome to EatOG - Your Source for Organic Goodness!",
            message=f"Dear {firstName},\n\nWelcome to EatOG, your ultimate destination for fresh, organic, and delicious food! We are thrilled to have you join our community of health-conscious individuals who value the goodness of nature's bounty.\n\nAt EatOG, we are committed to providing you with the finest selection of organic products, sourced directly from trusted farmers and producers. From vibrant fruits and vegetables to wholesome grains and pantry essentials, we've got everything you need to nourish your body and delight your taste buds.\n\nAs a registered member of EatOG, you'll enjoy exclusive access to special offers, exciting promotions, and personalized recommendations tailored to your preferences.\n\nWhether you're looking for a quick snack, planning a nutritious meal, or exploring new culinary adventures, we're here to inspire and support your journey towards a healthier lifestyle.\n\nThank you for choosing EatOG as your go-to destination for all things organic. We can't wait to embark on this flavorful and nutritious journey with you!\n\nWarm regards,\nThe EatOG Team",
            from_email="eatogfoods@gmail.com",
            recipient_list=[email],
            fail_silently=False,
        )

        return redirect("login")
    
    return render(request, "register.html")

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            django_login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login credentials'})
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth_logout(request)
    return redirect("home")

@login_required(login_url="/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required(login_url="/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/login/")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')


def Checkout(request):
    amount_str = request.POST.get("amount")
    amount_flo = float(amount_str)
    amount_dec = Decimal(amount_flo).quantize(Decimal('1'))
    amount = int(amount_dec)
    payment = client.order.create({
        "amount": amount * 100,  
        "currency": "INR",
        "payment_capture": "1"
    })
    order_id = payment["id"]
    context = {
        "order_id": order_id,
        "payment": payment
    }
    return render(request, "checkout.html", context)

def placeorder(request):
    if request.method == "POST":
        cart = request.session.get('cart')
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(id = uid)
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        country = request.POST.get("country")
        address = request.POST.get("address")
        date = request.POST.get("date")
        state = request.POST.get("state")
        city = request.POST.get("city")
        zipcode = request.POST.get("zipcode")
        total_amount = request.POST.get("total_amount")
        payment_method = request.POST.get("payment_method")
        order_id = request.POST.get("order_id")
        payment = request.POST.get("payment")
        context = {
            "order_id":order_id,
        }

        order = Order(
            user = user,
            first_name = first_name,
            last_name = last_name,
            phone = phone,
            email = email,
            country = country,
            address = address,
            state = state,
            city = city,
            zipcode = zipcode,
            total_amount = total_amount,
            payment_id = order_id,
            payment_method = payment_method,
            date = date
        )
        order.save()
        total = 0
        for i in cart:
            a = float(cart[i]['price'])
            b = int(cart[i]['quantity'])
            total = a * b
            item = OrderItem(
                order = order,
                product = cart[i]['name'],
                image = cart[i]['image'],
                price = cart[i]['price'],
                quantity = cart[i]['quantity'],
                total = total,
            )
            item.save()

    return render(request, "place_order.html", context)

@csrf_exempt
def thankYou(request):
    # cart = Cart(request)
    # cart.clear()
    if request.method == "POST":
        razorpay_order_id = request.POST.get("razorpay_order_id")
        user_order = Order.objects.filter(payment_id=razorpay_order_id).first()
        if user_order:
            user_order.paid = True
            user_order.save()

            send_mail(
                subject="Order Confirmation - EatOG",
                message=f"Dear {user_order.first_name},\n\nThank you for your order on EatOG. Your order with ID {user_order.id} has been successfully completed.\n\nWe appreciate your business and hope you enjoy your organic products!\n\nWarm regards,\nThe EatOG Team",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user_order.email],
                fail_silently=False,
            )
        else:
            print("Order with payment ID '{}' not found.".format(razorpay_order_id))


    return render(request, "thankyou.html")


def review(request):
    if request.method == "POST":
        image = request.FILES.get("image")
        review_text = request.POST.get("review")
        name = request.POST.get("name")
        rating = request.POST.get("rating")

        Review.objects.create(
            image=image,
            comment=review_text,
            name=name,
            rate=rating
        )
    data = Review.objects.all()
    context = {
        "data" : data
    }
    
    return render(request, "review.html", context)

def blogVege(request):
    return render(request, "blogVege.html")

def blogFruit(request):
    return render(request, "blogFruit.html")

def blogDairy(request):
    return render(request, "blogDairy.html")

def blog(request):
    return render(request, "blog.html")

def forgotPass(request):
    return render(request, "forgotpass.html")


def order_status(request):
    user_orders = Order.objects.filter(user=request.user)
    for order in user_orders:
        order_items = OrderItem.objects.filter(order=order)
        order.order_items = order_items

    context = {
        'orders': user_orders
    }

    return render(request, 'order_status.html', context)

def generate_sales_report(request, period='monthly'):
    today = datetime.today()
    if period == 'monthly':
        start_date = today.replace(day=1)
        end_date = today.replace(day=1, month=today.month + 1) - timedelta(days=1)
    elif period == 'quarterly':
        start_date = today.replace(day=1, month=((today.month - 1) // 3) * 3 + 1)
        end_date = start_date.replace(month=start_date.month + 3) - timedelta(days=1)
    elif period == 'daily':
        start_date = today
        end_date = today

    sales_data = OrderItem.objects.filter(order__date__range=[start_date, end_date]) \
        .values('product', 'quantity', 'total', 'order__date').annotate(total_sales=Sum('total')).order_by('-total_sales')

    context = {
        'sales_data': sales_data,
        'period': period.capitalize()
    }
    return render(request, 'sales_report.html', context)