from django.urls import path, include

from ff_tickets.auth_app.views import SignInView, SignUpView, SignOutView, \
    UserDetailsView, UserEditView, UserDeleteView

urlpatterns = (
    path('login/', SignInView.as_view(), name='login user'),
    path('register/', SignUpView.as_view(), name='register user'),
    path('logout/', SignOutView.as_view(), name='logout user'),
    path('profile/', include([
        path('<int:pk>/', UserDetailsView.as_view(), name='details user'),
        path('<int:pk>/edit/', UserEditView.as_view(), name='edit user'),
        path('<int:pk>/delete/', UserDeleteView.as_view(), name='delete user'),
    ])),
)

from .signals import *
