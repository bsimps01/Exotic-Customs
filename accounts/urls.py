from django.urls import path, include
from accounts.views import SignUpView, Foundation, update_profile, ProfilesListView, Homepage, Ferrari, login_view_profile, ConfirmPage


urlpatterns = [
    path('', Homepage.as_view(), name='home-page'),
    path('sign_up/', SignUpView.as_view(), name='signup-page'),
    path('foundation/', Foundation.as_view(), name="foundation-page"),
    path('get_ride/', update_profile, name='get-ride-page'),
    path('ferrari/', Ferrari.as_view(), name='get-rides-page'),
    path('all_rides/', ProfilesListView.as_view(), name='list-rides-page'),
    path('profile/', login_view_profile, name='account-page'), 
    path('confirm/', ConfirmPage.as_view(), name='confirm-page')

]