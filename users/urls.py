from django.urls import include, path
from rest_framework import routers
from . import views
from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'address', views.AddressViewSet)
router.register(r'user-types', views.UserTypeViewSet)
router.register(r'upload', views.ImageViewSet, base_name='upload')
router.register(r'user', views.UserViewSet)
router.register(r'customer', views.CustomerViewSet)
router.register(r'vendor-user', views.VendorUserViewSet)

urlpatterns = [ 
    path('', include(router.urls)),
]
