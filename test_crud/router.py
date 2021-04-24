from django.db import router
from test_crud.views import testViewset
from rest_framework import routers

app_name = 'test'

router = routers.SimpleRouter()
router.register(r'test', testViewset)

urlpatterns = [
]

urlpatterns = router.urls + urlpatterns