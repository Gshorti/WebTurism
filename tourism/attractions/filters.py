from rest_framework import filters


class TagFilterBackend(filters.BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """
    def filter_queryset(self, request, queryset, view):
        tags = request.GET["tags"]
        tags = tags.split(",")

        return queryset.filter(owner=request.user)