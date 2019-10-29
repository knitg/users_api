from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'customer', views.CustomerViewSet)
router.register(r'tailor', views.TailorViewSet)
router.register(r'designer', views.DesignerViewSet)
router.register(r'boutique', views.BoutiqueViewSet)
router.register(r'address', views.AddressViewSet)

urlpatterns = [ 
    path('', include(router.urls)),
]
