from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Profile, SocialLinks, User

from friends.models import Friendship, FriendshipRequest


@login_required
def profile_page(request, username):
    template = 'profile/profile.html'
    friendship_request = {
        'exists': False,
        'from_user': None
    }
    friendship = None
    user = request.user
    profile_owner = get_object_or_404(
        User.objects.select_related('profile__sociallinks'),
        username=username
    )
    if profile_owner == user:
        context = {
            'profile_owner': profile_owner,
            'friendship': friendship,
            'friendship_request': friendship_request
        }
        return render(request, template, context)
    friendship = Friendship.objects.filter(
        user=user,
        friend=profile_owner
    ).first()

    if not friendship:
        friendship_request = FriendshipRequest.objects.filter(
            Q(from_user=user, to_user=profile_owner) |
            Q(from_user=profile_owner, to_user=user)
        ).fisrt()
        if friendship_request:
            friendship_request = {
                'exists': True,
                'from_user': friendship_request.from_user
            }
    context = {
        'profile_owner': profile_owner,
        'friendship': friendship,
        'friendship_request': friendship_request
    }
    return render(request, template, context)
