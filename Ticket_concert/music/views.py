from django.shortcuts import render
from music.models import Event, Music, Album, Cart,Ticket_transaction, Transaction_info
import json
from django.core.serializers.json import DjangoJSONEncoder
from .data_layer.common import decorators
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from oauth2_provider.views.generic import ProtectedResourceView
from django.contrib.auth.models import User
from django.db.models import F, Sum
from django.db import transaction
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import SignUpForm, SignInForm, Transaction_InfoForm

def Home(request):
    data_album = Album.objects.all()[:5]
    album = [i.get_dict() for i in data_album]
    music = Music.objects.retrieveData()[:4]
    event_separate = Event.objects.all()[:4]
    event = []
    for i in event_separate:
        event.append(i.get_dict_event())
    return render(request,'index.html',{'album':album,
                                        'music':music,
                                        'event':event})

@decorators.ajax_required
def get_json_event(request):
    event_all = Event.objects.all()
    data = []
    for i in event_all:
        data.append(i.get_dict_event())
    return HttpResponse(json.dumps(data,cls=DjangoJSONEncoder),content_type='application/json')

"""{'event':'Green_day','event_for':['Missing_you','Stay The Night'],'location':'Jakarta','price':'500.000'}"""

@decorators.ajax_required
def get_json_music(request):
    music_all = Music.objects.retrieveData()
    data = [i for i in music_all]
    return HttpResponse(json.dumps(data,cls=DjangoJSONEncoder),content_type='application/json')

@decorators.ajax_required
def get_json_album(request):
    album_all = Album.objects.all()
    data = []
    for i in album_all:
        data.append(i.get_dict())
    return HttpResponse(json.dumps(data,cls=DjangoJSONEncoder),content_type='application/json')

#untuk tampilkan per album
def Album_view(request,pk):
    obj = Album.objects.only('nameapp','genre','release_date','picture','descriptions').get(idapp=pk)#.values('nameapp','picture','descriptions')
    related_music = obj.music_set.all()
    #data = [i for i in obj]
    template = 'Album_view_render.html'
    if request.is_ajax():
        template = 'Album_view_ajax.html'
    return render(request,template,{'obj':obj,'related_music':related_music})

def Album_list(request):
    album = Album.objects.all()
    data = []
    for i in album:
        data.append(i.get_dict())
    return render(request,'Album_list.html',{'album':data})

from django.contrib.auth.decorators import login_required


def Music_list(request):
    music_list = Music.objects.retrieveData()
    paginator = Paginator(music_list, 10)
    page = request.GET.get('page')
    music = paginator.get_page(page)
    return render(request,'Music_list.html',{'music':music})

def Event_view(request,pk):
    return render(request,'Event_view.html')

def Event_list(request):
    event_all = Event.objects.all()
    event = []
    user = None
    if request.user.is_authenticated:
        user = request.user.id
    for i in event_all:
        event.append(i.get_dict_event(user))
    return render(request,'Event_list.html',{'event':event})


def GD_signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            User.objects.create_user(first_name=form.cleaned_data['first_name'],
                                    last_name=form.cleaned_data.get('last_name'),
                                    username=username,
                                    email=email,
                                    password=form.cleaned_data['password1'])
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('not valid', status=400)
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def GD_signup_check_exists(request):
    if request.method == 'GET':
        username = request.GET['username']
        email = request.GET['email']
        exists_username = User.objects.filter(username=username).exists()
        exists_email = User.objects.filter(email=email).exists()
        if exists_username or exists_email:
            if exists_username:
                message = 'username already exists'
            elif exists_email:
                message = 'email already exists'
            return HttpResponse(json.dumps({'message':message}),content_type='application/json')
        else:
            return HttpResponse(json.dumps({'message':'success'}),content_type='application/json')

def GD_signin(request):
    if request.user.is_authenticated:
        next = request.GET.get('next')
        if next is not None:
            return redirect(next)
        else:
            if request.is_ajax():
                return HttpResponse(json.dumps({'message':'home'}),status=200,content_type='application/json')
            return redirect('home')
    else:
        if request.method == 'POST':
            form = SignInForm(request.POST or None)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(username=username, password=password) 
                login(request, user)
                next_action = form.cleaned_data.get('next')
                if next_action is not None and next_action != '':
                    return redirect(next_action)
                else :
                    return redirect('home')
            else:
                return HttpResponse('Form not valid',status=400)
        else:
            if request.method == 'GET':
                form = SignInForm()
                next = request.GET.get('next')
                form.fields['next'].initial = next
                template_name = 'SignIn_render.html'
                if request.is_ajax():
                    template_name = 'SignIn_ajax.html'
                return render(request, template_name, {"form":form})


class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')

def GD_get_user_profile(request,username):
    if request.user.is_authenticated:
        user_logged_on = request.user.username
        user = User.objects.filter(username=username)
        if user.exists():
            user = user.values('first_name','last_name','username','email')
        else:
            return HttpResponse('<h1>404 Not Found</h1>',status=404)
        if user_logged_on != user[0]['username']:
            return HttpResponseForbidden('<h1>403 Forbidden</h1>')
        else:
            return render(request,'User_Profile.html',{'user':user})
    else:
        return HttpResponseForbidden('<h1>403 Forbidden</h1>')

def GD_Change_User_Picture(request):
    print(request.FILES)
    return HttpResponse(request)

def GD_signout(request): # logs out the logged in users
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        logout(request)
        return redirect("home")

def getForm_data(request,form):
    clData = form.cleaned_data
    return {
        'user':User.objects.get(id=request.user.id),
        'ticket':Event.objects.get(idapp=clData['ticket_idapp']),
        'quantity':clData['quantity'],
        'no_telp':clData['no_telp'],
        'province':clData['province'],
        'code_pos':clData['code_pos'],
        'city':clData['city'],
        'address':clData['address']
        }

def GD_TransactionInfo_add(request):
    form = Transaction_InfoForm(request.POST)
    if form.is_valid():
        data = getForm_data(request,form)
        print('form valid')
        trans = Transaction_info.objects.create(user=data['user'],
                                            no_telp=data['no_telp'],province=data['province'],city=data['city'],
                                            code_pos=data['code_pos'],address=data['address'])
        return HttpResponse(json.dumps({'message':'success'}),content_type='application/json')

def GD_TransactionInfo(request):
    idapp_ticket = request.GET['idapp']
    form = Transaction_InfoForm()
    context = {}
    transaction_data = Transaction_info.objects.values('idapp','province','city','code_pos','address').filter(user=request.user.id)
    if transaction_data.exists():
        context['transaction_data'] = transaction_data
        form.display = 'none'
    context['form'] = form
    form.fields['ticket_idapp'].initial = idapp_ticket
    return render(request,'Transaction_info_form.html',context)


def GD_Cart_add(request):
    if request.method == 'POST':
        ticket_id = request.POST['ticket_idapp']
        username = request.user.username
        user = User.objects.get(username=username)
        ticket = Event.objects.get(idapp=ticket_id)
        cart = Cart.objects.create(ticket=ticket,user=user,quantity=request.POST['quantity'])
        return HttpResponse(json.dumps({'message':'success','idapp':ticket_id}),content_type='application/json')

def GD_Cart_edit(request):
    if request.method == 'POST':
        idapp = request.POST['idapp']
        quantity = request.POST['quantity']
        cart = Cart.objects.get(idapp=idapp)
        cart.quantity = int(quantity)
        cart.save()
        data = cart.get_dict()
        return HttpResponse(json.dumps({'message':'success',
                                        'quantity':cart.quantity,
                                        'price':data['price'],
                                        'total_price':data['total_price']}),content_type='application/json')

def GD_Cart_remove(request):
    if request.method == 'POST':
        idapp = request.POST['idapp']
        Cart.objects.filter(idapp=idapp).delete()
        return HttpResponse(json.dumps({'message':'success'}),content_type='application/json')


@login_required
def GD_Cart(request):
    cart_data = Cart.objects.filter(user=request.user.id)
    cart = [i.get_dict() for i in cart_data]
    return render(request,'Cart_list.html',{'cart':cart})


def GD_Checkout_list(request):
    ticket_data = Cart.objects.filter(user=request.user.id)
    ticket = [i.get_checkout_info() for i in ticket_data]
    return render(request,'Checkout_list.html',{'ticket':ticket})


def transaction_add(user,idapp_ticket,quantity,info):
    ticket=Event.objects.get(idapp=idapp_ticket)
    ticket.total_ticket = ticket.total_ticket - int(quantity)
    ticket.save()
    total_purchase = int(quantity)*int(ticket.price)
    Ticket_transaction.objects.create(user=user,
                                      ticket=ticket,
                                      quantity=quantity,
                                      info=info,
                                      total_purchase=total_purchase)

def GD_Checkout_confirm(request):
    if request.method == 'GET':
        address = Transaction_info.objects.filter(user=request.user.id).values('idapp','province','city','code_pos','address')
        return render(request,'Checkout_confirm_address.html',{'address':address})
    elif request.method == 'POST':
        idapp = request.POST['idapp'] #idapp for transaction info
        idapp_cart = request.POST['idapp_cart']
        idapp_ticket = request.POST['idapp_ticket']
        quantity = request.POST['quantity']
        user = User.objects.get(id=request.user.id)
        info = Transaction_info.objects.get(idapp=idapp)
        with transaction.atomic():
            if ',' in idapp_ticket:
                idapp_ticket = idapp_ticket.split(',')
                quantity = quantity.split(',')
                for i in range(len(idapp_ticket)):
                    transaction_add(user,idapp_ticket[i],quantity[i],info)
                idapp_cart = idapp_cart.split(',')
                Cart.objects.filter(idapp__in=idapp_cart).delete()
            else:
                transaction_add(user,idapp_ticket,quantity,info)
                Cart.objects.filter(idapp=idapp_cart).delete()
        return HttpResponse(json.dumps({'message':'success','idapp':idapp_cart}),content_type='application/json')
        