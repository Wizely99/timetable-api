from timetable.models import Klass
from timetable.serializers import KlassListSerializer
from rest_framework import generics

# from rest_framework.permissions import IsAdminUser

from rest_framework import generics
from django.db.models import Q


class KlassList(generics.ListCreateAPIView):
    queryset = Klass.objects.all()
    serializer_class = KlassListSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get("search", None)

        if search_query:
            queryset = queryset.filter(
                Q(program__icontains=search_query) | Q(code__icontains=search_query)
            )

        return queryset
