from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from task_manager.settings import BASE_REDIRECT_URL

from .components import (
    create_friendship,
    create_friendship_request,
    delete_friendship_objects,
    friendship_exists
)
from .models import FriendshipRequest, User


@login_required
def send_friendship_request(request, user_id):
    from_user = request.user
    to_user = get_object_or_404(User, id=user_id)
    if not friendship_exists(from_user, to_user):
        create_friendship_request(from_user, to_user)
    # TODO: ИЗМЕНИТЬ РЕДИРЕКТ НА ПРОФИЛЬ (ЛИБО ПРОФИЛЬ ПОЛЬЗОВАТЕЛЯ АКТИВНОГО, ЛИБО ПРОФИЛЬ КОГО ДОБАВЛЯЕТ В ДРУЗЬЯ)
    return redirect(BASE_REDIRECT_URL)


@login_required
def process_friendship_request(request, action, user_id):
    from_user = get_object_or_404(User, id=user_id)
    to_user = request.user
    friend_request = get_object_or_404(
        FriendshipRequest,
        from_user=from_user,
        to_user=to_user
    )
    if action == 'accept':
        create_friendship(from_user, to_user)
    friend_request.delete()
    # TODO: ИЗМЕНИТЬ РЕДИРЕКТ НА ПРОФИЛЬ (ЛИБО ПРОФИЛЬ ПОЛЬЗОВАТЕЛЯ АКТИВНОГО, ЛИБО ПРОФИЛЬ КОГО ДОБАВЛЯЕТ В ДРУЗЬЯ)
    return redirect(BASE_REDIRECT_URL)


@login_required
def delete_friendship(request, user_id):
    user = request.user
    friend = get_object_or_404(User, id=user_id)
    delete_friendship_objects(user, friend)
    create_friendship_request(friend, user)
    # TODO: ИЗМЕНИТЬ РЕДИРЕКТ НА ПРОФИЛЬ (ЛИБО ПРОФИЛЬ ПОЛЬЗОВАТЕЛЯ АКТИВНОГО, ЛИБО ПРОФИЛЬ КОГО ДОБАВЛЯЕТ В ДРУЗЬЯ)
    return redirect(BASE_REDIRECT_URL)
