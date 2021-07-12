from django import forms

from .models import Reviews, Rating, RatingStar, FavoriteMovie


class ReviewForm(forms.ModelForm):
    """Форма отзывов"""
    class Meta:
        model = Reviews
        fields = ("name", "email", "text")


class FavForm(forms.ModelForm):
    """Форма fav"""
    class Meta:
        model = FavoriteMovie
        fields = ("movie", "in_fav")


class RatingForm(forms.ModelForm):
    """Форма добавления рейтинга"""
    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Rating
        fields = ("star",)
