from django.urls import path
from django.db import router
from test_crud.views import testViewset, personViewset, itunesViewset
from rest_framework import routers

app_name = 'test'

router = routers.SimpleRouter()
router.register(r'test', testViewset)
router.register(r'person', personViewset)

urlpatterns = [
    path('itunes-data/', itunesViewset.as_view()),
]

urlpatterns = router.urls + urlpatterns