from django.contrib import admin
from app1.models import BookInfo, Heroinfo


# Register your models here.

class BookinfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bpub_data']


class HeroinfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'hname', 'hsex', 'hbook']


admin.site.register(BookInfo, BookinfoAdmin)
admin.site.register(Heroinfo, HeroinfoAdmin)
