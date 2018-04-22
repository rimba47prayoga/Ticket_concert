from django.shortcuts import render
from music.models import Event, Music, Album
import json
from django.core.serializers.json import DjangoJSONEncoder
from .data_layer.common import decorators
from django.http import HttpResponse

def Home(request):
    return render(request,'index.html')

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
    #return HttpResponse(json.dumps(data,cls=DjangoJSONEncoder),content_type='application/json')

def Album_list(request):
    album = Album.objects.all()
    data = []
    for i in album:
        data.append(i.get_dict())
    return render(request,'Album_list.html',{'album':data})

def Music_list(request):
    music = Music.objects.retrieveData()
    return render(request,'Music_list.html',{'music':music})

def Event_view(request,pk):
    return render(request,'Event_view.html')

def Event_list(request):
    event_all = Event.objects.all()
    event = [i.get_dict_event for i in event_all]
    return render(request,'Event_list.html',{'event':event})
    