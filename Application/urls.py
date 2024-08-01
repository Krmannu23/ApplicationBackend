from django.urls import path,include;
from Application import views



urlpatterns = [
    path('identity', views.IdentityList.as_view()),
    path('<int:ik>/', views.IdentityDetails.as_view()),
    path('forms',views.displayForm,name="forms")
]