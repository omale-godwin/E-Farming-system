from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'user', 'list_date', 'price', 'description', 'is_published')
  list_display_links = ('id', 'title')
  list_filter = ('title',)
  
  search_fields = ('title',)
  list_per_page = 25

admin.site.register(Listing, ListingAdmin)
