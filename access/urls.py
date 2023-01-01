from django.urls import path
from .views import( RegisterPage, LandingPage, LoginPage, LogoutPage,
                    ResetPasswordPage, ChangePasswordPage)

urlpatterns = [
    path('success/', LandingPage.as_view(), name='success'),
    path('login/', LoginPage.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('logout/', LogoutPage.as_view(), name='logout'),
    path('resetpassword/', ResetPasswordPage.as_view(), name='resetpassword'),
    path('changepassword/', ChangePasswordPage.as_view(), name='changepassword') # requires login access





]
