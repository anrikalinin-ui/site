from django.shortcuts import render, redirect

from .forms import MessageForm


def contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = MessageForm()
    return render(request, 'contact/contact.html', {'form': form})


def contact_success(request):
    return render(request, 'contact/success.html')
