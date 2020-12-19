from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView
from collection import views
from collection.backends import MyRegistrationView
from django.contrib.auth.views import(
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    path('',views.pie_chart, name='home'),
    path('lograting/',views.add_rating,name='lograting'),
    path('logshtetl/',views.add_shtetl,name='logshtetl'),
    path('shtetlwins/',views.shtetl_record, name='shtetl'),
    path('things/', RedirectView.as_view(pattern_name='browse', permanent=True)),
    path('things/<slug>/', views.thing_detail, name='thing_detail'),
    path('things/<slug>/edit/', views.edit_thing, name='edit_thing'),
    path('browse/', RedirectView.as_view(pattern_name='browse', permanent=True)),
    path('browse/name/',views.browse_by_name, name='browse'),
    path('browse/name/<initials>/',views.browse_by_name, name='browse_by_name'),
    path('accounts/register/', MyRegistrationView.as_view(), name='registration_register'),
    path('accounts/create_thing/', views.create_thing, name='registration_create_thing'),
    path('accounts/password/reset/',PasswordResetView.as_view(),name="password_reset"),
    path('accounts/password/reset/done/',PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('accounts/password/reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('accounts/password/done',PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    path('accounts/', include('registration.backends.simple.urls')),
    path('admin/', admin.site.urls),
]
