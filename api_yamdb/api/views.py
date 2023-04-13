from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from api.serializers import ReviewsSerializer
from api.permissions import AdminAuthorModeratorOrReadOnly
from reviews.models import Title

class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewsSerializer
    permission_classes = (AdminAuthorModeratorOrReadOnly,)

    def get_queryset(self):
        title = get_object_or_404(
            Title,
            id=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(
            Title,
            id=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)
