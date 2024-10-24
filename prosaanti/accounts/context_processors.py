from .models import userProfile


def userprofile(request):
    if request.user.is_authenticated:
        try:
            profile = userProfile.objects.get(user=request.user)
        except userProfile.DoesNotExist:
            profile = None
        try:
            clint_count = userProfile.objects.filter(is_new=True).count()
        except userProfile.DoesNotExist:
            clint_count = 22
    else:
        profile = None
        clint_count = 0

    return {'profile': profile, 'clint_count': clint_count}
