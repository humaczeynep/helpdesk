from django.urls import path
from .import views

urlpatterns = [
    path('ticket-details/<int:pk>/', views.ticket_details, name='ticket-details'),
    path('create-ticket/', views.create_ticket, name='create-ticket'),
    path('update-ticket/<int:pk>/', views.update_ticket, name = 'update-ticket'),
    path('all-tickets/', views.all_tickets, name='all-tickets'),
    path('ticket-queue/', views.ticket_queue, name='ticket-queue'),
    path('accept-ticket/<int:pk>/', views.accept_ticket, name='accept-ticket'),
    path('close-ticket/<int:pk>/', views.close_ticket, name='close-ticket'),
    path('workspace/', views.workspace, name='workspace'),
    path('all-closed-tickets/', views.all_closed_tickets, name='all-closed-tickets')
]
