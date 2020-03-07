from django.urls import path, include
from accounts.views import SignUpView, Foundation, update_profile, AboutUs, Homepage, Ferrari, login_view_profile, ConfirmPage, Bugatti, McLaren, Lamborghini


urlpatterns = [
    path('', Homepage.as_view(), name='home-page'),
    path('sign_up/', SignUpView.as_view(), name='signup-page'),
    path('foundation/', Foundation.as_view(), name="foundation-page"),
    path('get_ride/', update_profile, name='get-ride-page'),
    path('ferrari/', Ferrari.as_view(), name='get-rides-page'),
    path('bugatti/', Bugatti.as_view(), name='get-bugatti-page'),
    path('mclaren/', McLaren.as_view(), name='get-mclaren-page'),
    path('lamborghini/', Lamborghini.as_view(), name='get-lamborghini-page'),
    path('about_us/', AboutUs.as_view(), name='about-us-page'),
    path('profile/', login_view_profile, name='account-page'), 
    path('confirm/', ConfirmPage.as_view(), name='confirm-page')

]