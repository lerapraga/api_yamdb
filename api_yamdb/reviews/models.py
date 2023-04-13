from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from users.models import User


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение'
    )
    text = models.CharField(max_length=200)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
    )
    score = models.IntegerField(
        validators=(MinValueValidator(1), MaxValueValidator(10)),
        verbose_name='Оценка',
    )

    class Meta:
        verbose_name = 'Отзыв'
        ordering = ('pub_date',)
        constraints = [
            models.UniqueConstraint(
                fields=('title', 'author', ), name='unique_review')]

    def __str__(self):
        return self.text
