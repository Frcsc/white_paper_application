from django.conf import settings
from django.core.mail import send_mail
from django.views.generic import DetailView, FormView, ListView, TemplateView
from django.db.models import Q

from cms.form import ContactForm
from cms.models import VISIBILITY, PeopleModel, PropertyListModel


class HomePageView(TemplateView):
    template_name = "home.html"

    people = PeopleModel

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["listings"] = PropertyListModel.objects.filter(
            show_on_home_page=VISIBILITY.SHOW_ON_HOME_PAGE
        )[:4]
        context["people"] = PeopleModel.objects.all()
        return context


class PropertyListPageListView(ListView):
    model = PropertyListModel
    template_name = "properties.html"

    def get_queryset(self, *args, **kwargs):
        type_of_property = self.request.GET.get('type_of_property', '')
        type_of_offer = self.request.GET.get('type_of_offer', '')
            
        if not self.request.GET:
            return self.model.objects.all()
        
        else:
            search = self.model.objects.filter(
                Q(type_of_property=type_of_property) &
                Q(type_of_offer=type_of_offer) 
            )
            return search




class PropertyListPageDetailView(DetailView):
    template_name = "property_details.html"
    model = PropertyListModel
    context_object_name = "current_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_list_model"] = self.model.objects.filter(pk=self.kwargs["pk"])
        return context


class ContactUsView(FormView):
    form_class = ContactForm
    template_name = "contact.html"
    success_url = "/contact"

    def form_valid(self, form):
        data = {
            "name": form.cleaned_data.get("your_name"),
            "email": form.cleaned_data.get("email"),
            "mobile_number": form.cleaned_data.get("mobile_number"),
            "type_of_enquiry": form.cleaned_data.get("type_of_enquiry"),
            "enquirer_message": form.cleaned_data.get("message"),
        }

        subject = f"Enquiry from {data['name']}"
        content = f"""
        Name: {data['name']}\n
        Email: {data['email']}\n
        Mobile Number: {data['mobile_number']}\n
        Type of Enquiry: {data['type_of_enquiry']}\n
        Message: {data['enquirer_message']}\n
        """

        send_mail(
            subject=subject,
            message=content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[data["email"], "bayati@yourdomain.com"],
            fail_silently=False,  # Set to True for production
        )

        return super().form_valid(form)


class ComingSoonView(TemplateView):
    template_name = "coming-soon.html"


class SellView(TemplateView):
    template_name = "sell.html"
