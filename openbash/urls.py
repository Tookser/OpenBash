from django.urls import path

from .views import QuoteDetailView, QuoteListView



urlpatterns = [
    path('', QuoteListView.as_view(), name='list'),
    path('quote/<int:pk>', QuoteDetailView.as_view(), name='quote'),
]
