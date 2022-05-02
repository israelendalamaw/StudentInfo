import django_filters
from django_filters import CharFilter, ChoiceFilter
from .models import Athletes


class AthleteFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains', label='Name')
    sport = CharFilter(field_name='sport', lookup_expr='icontains', label='Sport')
    nationality = CharFilter(field_name='nationality', lookup_expr='icontains', label='Nationality')


    class Meta:
        model = Athletes
        fields = '__all__'

