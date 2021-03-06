from django.shortcuts import render
from .forms import *
from .models import *
from django.views.generic import CreateView, ListView, TemplateView
from .choices import price_choices, bedroom_choices, state_choices
from django.core.paginator import Paginator
from django.http import HttpResponse

# from itertools import chain

# def search(request):
#     queryset_catalogue = Catalogue.objects.order_by('-catalogue_date')
#
#     # Keywords
#     if 'keywords' in request.GET:
#         keywords = request.GET['keywords']
#         if keywords:
#             queryset_catalogue = queryset_catalogue.filter(description__icontains=keywords)
#
#     # City
#     if 'city' in request.GET:
#         city = request.GET['city']
#         if city:
#             queryset_catalogue = queryset_catalogue.filter(city__iexact=city)
#
#     # State
#     if 'state' in request.GET:
#         state = request.GET['state']
#         if state:
#             queryset_catalogue = queryset_catalogue.filter(state__iexact=state)
#
#     # Bedrooms
#     if 'bedrooms' in request.GET:
#         bedrooms = request.GET['bedrooms']
#         if bedrooms:
#             queryset_catalogue = queryset_catalogue.filter(bedrooms__lte=bedrooms)
#
#     # Price
#     if 'price' in request.GET:
#         price = request.GET['price']
#         if price:
#             queryset_catalogue = queryset_catalogue.filter(price__lte=price)
#
#     context = {
#         'state_choices': state_choices,
#         'bedroom_choices': bedroom_choices,
#         'price_choices': price_choices,
#         'catalogues': queryset_catalogue,
#         'values': request.GET
#     }
#     return render(request, 'catalogues/search.html', context)


# def index(request):
#     context = {
#         'state_choices': state_choices,
#         'bedroom_choices': bedroom_choices,
#         'price_choices': price_choices,
#     }
#     return render(request, 'index.html', context)


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        properties_view = Catalogue.objects.order_by('-catalogue_date')
        context = super(HomeView, self).get_context_data(**kwargs)
        number_of_properties = 0

        context.update({
            'state_choices': state_choices,
            'bedroom_choices': bedroom_choices,
            'price_choices': price_choices,
            'properties': properties_view,
            'number_of_properties': number_of_properties
        })
        print(context)
        return context


# def about(request):
#     return render(request, 'about.html')


def property(request, id):
    property_view = Catalogue.objects.get(id=id)
    # images = property.images.all()

    context = {
        'property': property_view,
        # 'images':images

    }
    return render(request, 'property.html', context)


# class PropertyView(TemplateView):
#     template_name = 'property.html'
#
#     def get_context_data(self, **kwargs):
#         pk = self.request.user.pk
#         context = super(HomeView, self).get_context_data(**kwargs)
#         property = Catalogue.objects.get(pk=pk)
#         context.update({
#             'property': property,
#         })
#         return context


def properties(request):
    # properties_view = Catalogue.objects.all()
    properties_view = Catalogue.objects.order_by('-catalogue_date')
    number_of_properties = properties_view.count
    paginator = Paginator(properties_view, 6)
    page = request.GET.get('page')
    pages = paginator.get_page(page)
    # count = 1
    # images = []
    # for i in properties:
    # if count == 1:
    # images = i.images.all()
    # count = count + 1
    # print(images[0].image)
    return render(request, 'properties.html', {'properties': properties_view,
                                               'number_of_properties': number_of_properties,
                                               'pages': pages})


# def contactus(request):
#     return render(request, 'contact.html')


class SearchView(ListView):
    template_name = 'index.html'
    paginate_by = 20
    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['keywords'] = self.request.GET.get('keywords')
        context['city'] = self.request.GET.get('city')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('keywords', None)

        if query is not None:
            # search_results = Catalogue.objects.search(query)

            # # combine querysets
            # queryset_chain = chain(
            #     search_results,
            # )
            # qs = sorted(queryset_chain,
            #             key=lambda instance: instance.pk,
            #             reverse=True)
            # self.count = len(qs)  # since qs is actually a list
            return Catalogue.objects.search(query=query)
        return Catalogue.objects.none()


class AddProperty(CreateView):
    # model = Catalogue
    form_class = PropertyForm
    template_name = 'property_form.html'
    success_url = '/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        # self.object.profile = self.request.user
        instance.save()
        form.save_m2m()
        instance.profile.add(self.request.user)

        return HttpResponse("<html>ok</html>")
