from django.contrib import admin

from .models import Contact

class ListingAdmin(admin.ModelAdmin):
  list_display = ('id', 'fullname', 'contact_date', 'phone', 'subject')
  list_display_links = ('id', 'fullname')
  list_filter = ('fullname',)
  
  search_fields = ('fullname',)
  list_per_page = 25

admin.site.register(Contact, ListingAdmin)
