from rest_framework.serializers import ModelSerializer

from movies.models import FavoriteMovie


class UserMovieRelationSerializer(ModelSerializer):
    class Meta:
        model = FavoriteMovie
        fields = ('movie', 'in_fav')