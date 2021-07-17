from django.urls import path

from . import views

urlpatterns = [

    path('savepredicted', views.save_predicted_price, name='save_predicted_price'),
    path('predict', views.predict, name='predict'),
    path('', views.make_predictions, name='save'),
]
