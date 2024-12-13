from rest_framework.filters import BaseFilterBackend
from django.db.models import Q

class MatchTypeFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        match_type = request.query_params.get("match_type", "partial")
        search_param = request.query_params.get("search", "").strip()

        # Se houver um parâmetro de busca
        if search_param:
            if match_type == "exact":
                return queryset.filter(Q(title=search_param) | Q(description=search_param))
            elif match_type == "partial":
                return queryset.filter(Q(title__icontains=search_param) | Q(description__icontains=search_param))

        return queryset
