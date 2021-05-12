#from .models import *
#from django.contrib import admin


#class TrackInline(admin.TabularInline):
#    model = PlaylistTrack

#class PlaylistAdmin(admin.ModelAdmin):
#    inlines = (TrackInline, )

#admin.site.register(Album)
#admin.site.register(Artist)
#admin.site.register(Customer)
#admin.site.register(Employee)
#admin.site.register(Genre)
#admin.site.register(Invoice)
#admin.site.register(Invoiceline)
#admin.site.register(Mediatype)
#admin.site.register(Playlist, PlaylistAdmin)
#admin.site.register(Track)

from chinook import models as chinook_models
from django.contrib import admin
from django.db.models.base import ModelBase

# Very hacky!
for name, var in chinook_models.__dict__.items():
    if type(var) is ModelBase:
        admin.site.register(var)
