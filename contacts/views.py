from django.shortcuts import render, redirect
from django.views.generic import View
from contacts.forms import ContactForm


class ContactView(View):
    def get(self, request, *args, **kwargs):
        form = ContactForm()
        return render(request, 'contacts/contact.html')

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect('contact')
        return render(request, 'contacts/contact.html', {'form': form})
