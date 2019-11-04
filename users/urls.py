from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'customer', views.CustomerViewSet)
router.register(r'tailor', views.TailorViewSet)
router.register(r'maggam-designer', views.MaggamDesignerViewSet)
router.register(r'fashion-designer', views.FashionDesignerViewSet)
router.register(r'boutique', views.BoutiqueViewSet)
router.register(r'address', views.AddressViewSet)

urlpatterns = [ 
    path('', include(router.urls)),
]
