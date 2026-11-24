from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import ProfileUpdateForm

def profile_view(request):
    profile, _ = UserProfile.objects.get_or_create(pk=1)

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=profile)

    return render(request, 'profile_app/profile.html', {
        'profile': profile,
        'form': form,
    })