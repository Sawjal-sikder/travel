from django.shortcuts import render, get_object_or_404
from .models import CompanyInformation
from accounts.models import userProfile


# Create your views here.
def adminPanel(request):
    return render(request, 'admin.html')


def comInfo(request):
    # Using get_object_or_404 to handle non-existent cases more gracefully
    info = get_object_or_404(CompanyInformation, pk=1)

    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        tax_id = request.POST.get('tax_id')
        email = request.POST.get('email')
        address = request.POST.get('address')
        logo = request.FILES.get('logo')
        icon = request.FILES.get('icon')
        # Update fields
        info.name = name
        info.phone_number = phone_number
        info.tax_id = tax_id
        info.email = email
        info.address = address
        info.logo = logo
        info.icon = icon
        # Save the updated object to the database
        info.save()

    # Pass the company information to the template for display
    context = {
        'info': info,
    }

    return render(request, 'settings/complanyinformation.html', context)


def clintList(request):
    clints = userProfile.objects.filter(is_new=False)
    context = {
        'clints': clints
    }
    return render(request, 'user/user.html', context)
