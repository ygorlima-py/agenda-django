from django.urls import path
from contact.views import index, contact, search

app_name = 'contact'

urlpatterns = [
    # contact(CRUD)
    path('contact/<int:contact_id>/detail', contact, name='contact'),
    
    path('search/', search, name='search'),
    path('', index, name='index'),

]