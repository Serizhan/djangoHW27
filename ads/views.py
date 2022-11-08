import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Ads, Categories


def home_page(request):
    return JsonResponse({"status": "ok"})


@method_decorator(csrf_exempt, name="dispatch")
class AdsView(View):
    def get(self, request):
        adsies = Ads.objects.all()

        response = []
        for ads in adsies:
            response.append({
                "id": ads.id,
                "name": ads.name,
                "author": ads.author,
                "price": ads.price,
                "description": ads.description,
                "address": ads.address,
                "is_published": ads.is_published
            })

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})

    def post(self, request):
        ads_data = json.loads(request.body)

        ads = Ads()
        # ads.id = ads_data['id']
        ads.name = ads_data['name']
        ads.author = ads_data['author']
        ads.price = ads_data['price']
        ads.description = ads_data['description']
        ads.address = ads_data['address']
        ads.is_published = ads_data['is_published']

        ads.save()

        return JsonResponse({
            "id": ads.id,
            "name": ads.name,
            "author": ads.author,
            "price": ads.price,
            "description": ads.description,
            "address": ads.address,
            "is_published": ads.is_published
        })


class CategoriesView(View):
    def get(self, request):
        categories = Categories.objects.all()

        response = []
        for category in categories:
            response.append({
                "id": category.id,
                "name": category.name
            })

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})


class AdsDetailView(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        try:
            ads = self.get_object()
        except Ads.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)

        return JsonResponse({
                "id": ads.id,
                "name": ads.name,
                "author": ads.author,
                "price": ads.price,
                "description": ads.description,
                "address": ads.address,
                "is_published": ads.is_published
            })


class CategoriesDetailView(DetailView):
    model = Categories

    def get(self, request, *args, **kwargs):
        try:
            categories = self.get_object()
        except Categories.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)

        return JsonResponse({
                "id": categories.id,
                "name": categories.name,
        })
