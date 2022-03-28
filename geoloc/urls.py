from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('geolocalizations', views.GeoLocalizationViewSet)


# URLConf
urlpatterns = router.urls
