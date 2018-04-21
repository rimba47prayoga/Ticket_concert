from django.shortcuts import render
from music.models import Ticket, Music, Album
import json
from django.core.serializers.json import DjangoJSONEncoder
from .data_layer.common import decorators
from django.http import HttpResponse

def Home(request):
    return render(request,'index.html')

@decorators.ajax_required
def get_json_ticket(request):
    ticket_all = Ticket.objects.all()
    data = []
    for i in ticket_all:
        data.append(i.get_dict_ticket())
    return HttpResponse(json.dumps(data,cls=DjangoJSONEncoder),content_type='application/json')

"""{'ticket':'Green_day','ticket_for':['Missing_you','Stay The Night'],'location':'Jakarta','price':'500.000'}"""

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
        data.append({'link_url':i.get_absolute_url(),'nameapp':i.nameapp,'picture':i.picture.name,'descriptions':i.descriptions[:70] + '...'})
    return HttpResponse(json.dumps(data,cls=DjangoJSONEncoder),content_type='application/json')

def Album_view(request,pk):
    obj = Album.objects.filter(idapp=pk).values('nameapp','picture','descriptions')
    data = [i for i in obj]
    return HttpResponse(json.dumps(data,cls=DjangoJSONEncoder),content_type='application/json')