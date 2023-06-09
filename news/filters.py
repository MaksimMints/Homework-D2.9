from django_filters import FilterSet
from django.forms import DateInput
from .models import Post
import django_filters

class PostFilter(FilterSet):

    title = django_filters.CharFilter(lookup_expr='icontains', label='Title')

    dateCreateAfter = django_filters.DateFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        label='Date Creation after',
        widget=DateInput(
            format='%Y-%m-%dT',
            attrs={'type': 'date'}
        )
    )

    class Meta:
        model = Post
        fields = ['categoryType', ]