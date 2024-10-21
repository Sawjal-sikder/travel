from .models import CompanyInformation

def com_info(request):
    if request.user.is_authenticated:
        try:
            info = CompanyInformation.objects.get(pk=1)
        except CompanyInformation.DoesNotExist:
            info = None
    else:
        info = None

    return {'info': info}
