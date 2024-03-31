from django.urls import path, include
from rest_framework import routers
from api.views import CompanyViewSet, EmployeesViewSet

router = routers.DefaultRouter()
router.register(r'company', CompanyViewSet)
router.register(r'employees', EmployeesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
