from django.urls import include, path
from rest_framework import routers
from . import views
from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'customer', views.CustomerViewSet)
router.register(r'tailor', views.TailorViewSet)
router.register(r'master', views.MasterViewSet)
router.register(r'maggam-designer', views.MaggamDesignerViewSet)
router.register(r'fashion-designer', views.FashionDesignerViewSet)
router.register(r'boutique', views.BoutiqueViewSet)
router.register(r'address', views.AddressViewSet)
# router.register(r'fileupload', views.FileView.as_view(), base_name='fileupload')
router.register(r'upload', views.ImageViewSet, base_name='upload')

urlpatterns = [ 
    path('', include(router.urls)),
    # url(r'^upload/$', views.FileView.as_view(), name='file-upload'),

]
