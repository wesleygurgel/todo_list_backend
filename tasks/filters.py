from rest_framework.filters import BaseFilterBackend

class MatchTypeFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        match_type = request.query_params.get("match_type", "partial")
        search_param = request.query_params.get("search", "")

        if search_param:
            if match_type == "exact":
                return queryset.filter(title=search_param)
            elif match_type == "partial":
                return queryset.filter(title__icontains=search_param)

        return queryset
