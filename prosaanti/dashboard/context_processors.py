from .models import CompanyInformation


def com_info(request):
    try:
        info = CompanyInformation.objects.get(pk=1)
    except CompanyInformation.DoesNotExist:
        info = None

    return {'info': info}
