from datetime import date
from datetime import datetime 
from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages


def index(request):
    data = book.objects.all()
    return render(request,"index.html",{'data':data})

def login(request):
    if request.method == "POST":
        fname = request.POST['phone']
        pwd = request.POST['password']
        if fname == "" or pwd == "":
            messages.error(request,"invalid input!")
        else:
            data = users.objects.filter(phone=fname,password=pwd).all()
            # print(data)
            phone=""
            password=""
            for i in data:
                phone=i.phone
                password=i.password
            if phone == "" or password == "":
                messages.error(request,"invalid input!")
                return render(request,"login.html")
            else:
                for i in data :
                    request.session['sid']=i.id
                    request.session['sfname']=i.fname
                    print(request.session.get('sid'))
                    print(request.session.get('fname'))
                return redirect("books")
    return render(request,"login.html")

def signup(request):
    return render(request,"signup.html")

def insert(request):
    x=""
    ck1 = ""
    if request.method == "POST" and request.FILES['image']:
        image = request.FILES['image']
        cpass = request.POST['cpassword']
        data = users()
        data.fname = request.POST['fname']
        data.lname = request.POST['lname']
        data.phone = request.POST['phone']
        data.password = request.POST['password']
        data.gender = request.POST['gender']
        data.image = image
        
        
        if data.fname == "" :
            messages.info(request,"Plz Enter First Name")
        elif data.lname == "":
            messages.warning(request,"Plz Enter last Name")
        elif data.phone == "":
            messages.warning(request,"Plz Enter Phone Number")
        elif data.password == "":
            messages.info(request,"Plz Enter Password")
        elif cpass == "":
            messages.info(request,"Plz Enter Confirm Password")
        elif data.password != cpass:
            messages.error(request,"Both Password Are Not Match")
        else:
            
            ck=users.objects.filter(phone=data.phone).all()
            for i in ck:
                ck1=i.phone
            if ck1 != "":
                messages.error(request,"Alreday Registr Phone Number")
            else:
                x="true"
                messages.success(request,"Successfully Register...")
                data.save()

    return render(request,"signup.html",{'x':x})

def profile(request):
    userId=request.session.get('sid')
    if userId is None:
        return render(request,"login.html")
    else:
        b=fname(request)
        c=photo(request)
        data=users.objects.filter(id=userId).first()

    return render(request,"profile.html",{'b':b,'c':c,'i':data})

def logout(request):
    del request.session['sid']
    del request.session['sfname']
    return render(request,"login.html")

def fname(request):
    userId=request.session.get('sid')
    ab= users.objects.filter(id=userId)
    for i in ab:
        fname=i.fname
    return fname

def photo(request):
    userId=request.session.get('sid')
    ab= users.objects.filter(id=userId)
    for i in ab:
        photo = i.image
    return photo

def books(request):
    userId=request.session.get('sid')
    if userId is None:
        return render(request,"login.html")
    else:
        b=fname(request)
        c=photo(request)
        data = book.objects.all()
    return render(request,"book.html",{'b':b,'c':c,'data':data})

def returnb(request):
    userId=request.session.get('sid')
    if userId is None:
        return render(request,"login.html")
    else:
        b=fname(request)
        c=photo(request)
        lo=histroy.objects.filter(user_id=userId)


    
    return render(request,"returnb.html",{'b':b,'c':c,'x':lo})

def history(request):
    b=fname(request)
    c=photo(request)
    return render(request,"history.html",{'b':b,'c':c})

def book_details(request):
    b=fname(request)
    c=photo(request)
    book_id=request.GET['id']
    bdata = book.objects.filter(id=book_id).all()
    # print(book_id)
    # print(bdata)
    return render(request,"book_details.html",{'b':b,'c':c,'x':bdata})

def rent(request):
    b=fname(request)
    c=photo(request)
    book_id=request.GET['id']
    bdata = book.objects.filter(id=book_id).all().first()
    return render(request,"rent.html",{'b':b,'c':c,'i':bdata})

def rent_update(request):
    book_id1=request.POST['bid']
    pym=request.POST['ptm']
    qty=request.POST['qty']
    print(book_id1)
    print(qty)
    userId=request.session.get('sid')
    bdata=book.objects.filter(id=book_id1).all()
    for i in bdata:
        price = i.price
    
    hs=histroy()
    hs.user_id=userId
    hs.book_id=book_id1
    hs.price=price
    hs.quntity=qty
    hs.rent_date=datetime.now()
    hs.isRenew=False
    hs.pyment = pym
    hs.pyment_Mode="Cash"
    hs.save()
    messages.success(request,"Your Book Order Comfrimed...")
    return render(request,"rent.html")


def policy(request):
    b=fname(request)
    c=photo(request)
    return render(request,"policy.html",{'b':b,'c':c})

def term(request):
    b=fname(request)
    c=photo(request)
    return render(request,"term.html",{'b':b,'c':c})

def refund(request):
    b=fname(request)
    c=photo(request)
    return render(request,"refund.html",{'b':b,'c':c})

def shipping(request):
    b=fname(request)
    c=photo(request)
    return render(request,"shipping.html",{'b':b,'c':c})

def contact(request):
    b=fname(request)
    c=photo(request)
    return render(request,"contact.html",{'b':b,'c':c})

def contact1(request):
    return render(request,"contact1.html")

def about(request):
    return render(request,"about.html")