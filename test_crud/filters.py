import django_filters
from django_filters import rest_framework as filters
from .models import person


class PersonFilter(filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = person
        fields = {'first_name', 'last_name'}