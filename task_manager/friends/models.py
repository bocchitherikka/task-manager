from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Friendship(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='friends'
    )
    friend = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='friended'
    )

    class Meta:
        indexes = [
            models.Index(fields=['user', 'friend'])
        ]


class FriendshipRequest(models.Model):
    from_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_requests'
    )
    to_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='to_user_requests'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["from_user", "to_user"],
                name="unique_friendship_request"
            )
        ]
