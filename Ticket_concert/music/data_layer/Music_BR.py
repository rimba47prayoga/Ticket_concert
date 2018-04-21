from django.db.models import F, Manager
class Music_BR_Manager(Manager):
    def retrieveData(self):
        data = super(Music_BR_Manager,self).get_queryset()
        return data.annotate(albums=F('album__nameapp')).values('nameapp','albums')