from django.shortcuts import get_object_or_404
from rest_framework import serializers

from reviews.models import Review, Title


class ReviewsSerializer(serializers.ModelSerializer):
    title = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True
    )    
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    class Meta:
        model = Review
        fields = '__all__'

    def validate_score(self, value):
        if 0 > value > 10:
            raise serializers.ValidationError('Поставьте оценку от 1 до 10')
        return value

    def validate(self, data):
        request = self.context['request']
        author = request.user
        title_id = self.context.get('view').kwargs.get('title_id')
        title = get_object_or_404(Title, pk=title_id)
        if (
            request.method == 'POST'
            and Review.objects.filter(title=title, author=author).exists()
        ):
            raise serializers.ValidationError('Вы уже написали отзыв')
        return data
