from django.db.models import Q
from django.shortcuts import get_object_or_404

from .models import Friendship, FriendshipRequest, User


def friendship_exists(
        from_user: User,
        to_user: User
) -> bool:
    is_friendship_exists = Friendship.objects.filter(
        Q(user=from_user, friend=to_user) |
        Q(user=to_user, friend=from_user)
    ).exists()
    return is_friendship_exists


def friendship_request_exists(
        from_user: User,
        to_user: User
) -> bool:
    is_request_exists = FriendshipRequest.objects.filter(
        Q(from_user=from_user, to_user=to_user) |
        Q(from_user=to_user, to_user=from_user)
    ).exists()
    return is_request_exists


def create_friendship_request(
        from_user: User,
        to_user: User
) -> None:
    user_the_same = from_user == to_user
    if (
        not friendship_request_exists(from_user, to_user)
        and not user_the_same
    ):
        FriendshipRequest.objects.create(
            from_user=from_user,
            to_user=to_user
        )


def create_friendship(
        from_user: User,
        to_user: User
) -> None:
    Friendship.objects.create(
        user=from_user,
        friend=to_user
    )
    Friendship.objects.create(
        user=to_user,
        friend=from_user
    )


def delete_friendship_objects(
        user: User,
        friend: User
) -> None:
    friendship = get_object_or_404(
        Friendship,
        user=user,
        friend=friend
    )
    friendship.delete()
    mirrored_friendship = get_object_or_404(
        Friendship,
        user=friend,
        friend=user
    )
    mirrored_friendship.delete()
