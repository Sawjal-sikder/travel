from .models import userProfile


def userprofile(request):
    if request.user.is_authenticated:
        try:
            profile = userProfile.objects.get(user=request.user)
        except userProfile.DoesNotExist:
            profile = None
    else:
        profile = None

    return {'profile': profile}
