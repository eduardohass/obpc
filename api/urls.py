from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'grupos', views.GrupoViewSet)
router.register(r'pessoas', views.PessoaViewSet)
router.register(r'enderecos', views.EnderecoViewSet)
router.register(r'regionais', views.RegionalViewSet)
router.register(r'logs', views.LogViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
