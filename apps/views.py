from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import activate
from django.views.generic import TemplateView, ListView, DetailView, FormView

from apps.forms import ContactForm, BookingForm
from apps.models import Packages, Booking


# Create your views here.
class IndexView(ListView):
    model = Packages
    template_name = 'index.html'
    context_object_name = 'package_list'


class AboutView(TemplateView):
    template_name = 'about.html'


class ServicesView(TemplateView):
    template_name = 'service.html'


class PackagesView(ListView):
    template_name = 'blog.html'
    model = Packages
    context_object_name = 'packages'


class PackageDetailView(DetailView):
    template_name = 'single.html'
    model = Packages
    context_object_name = 'package'


def set_language(request):
    next_url = request.GET.get('next', '/')
    lang_code = request.GET.get('language')

    if lang_code and lang_code in dict(settings.LANGUAGES):
        # Strip out the language code from the URL before translating the URL.
        for code, _ in settings.LANGUAGES:
            prefix = f'/{code}/'
            if next_url.startswith(prefix):
                next_url = next_url[len(prefix) - 1:]
                break

        # Activate the selected language
        activate(lang_code)
        # Append the selected language code to the URL
        next_url = f'/{lang_code}{next_url}'

    return HttpResponseRedirect(next_url)


class ContactModelFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        # send_to_email.delay([form.data.get('email')], form.data.get('first_name'))
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class BookingFormView(FormView):
    model = Booking
    template_name = 'booking_form.html'
    form_class = BookingForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['packages'] = Packages.objects.all()
        return context


from django.views.generic import ListView
from .forms import TripSearchForm


class PackageSearchView(ListView):
    model = Packages
    template_name = 'blog.html'
    context_object_name = 'packagings'

    def get_queryset(self):
        queryset = super().get_queryset()
        form = TripSearchForm(self.request.GET or None)

        if form.is_valid():
            destination = form.cleaned_data.get('destination')
            departure_time = form.cleaned_data.get('departure_time')
            return_time = form.cleaned_data.get('return_time')
            duration = form.cleaned_data.get('duration')

            if destination:
                queryset = queryset.filter(name__icontains=destination)
            if departure_time:
                queryset = queryset.filter(departure_time__gte=departure_time)
            if return_time:
                queryset = queryset.filter(return_time__lte=return_time)
            if duration:
                queryset = queryset.filter(duration=duration)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TripSearchForm(self.request.GET or None)
        return context
