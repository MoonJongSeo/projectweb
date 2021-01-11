from django.shortcuts import render

from django.views.generic.base import View, TemplateView

from django.http import HttpResponse, JsonResponse

class HomeView(TemplateView):
    template_name = "population/home.html"

class SearchPastView(View):
    def get(self, request, key):
        from .population_repository import PopulationRepository
        import json

        repository = PopulationRepository()
        searched_population = repository.select_pop_past_by_name(key)
        json_population = json.dumps(searched_population, ensure_ascii=False)
        return HttpResponse(json_population, content_type="application/json")

class SearchFutureView(View):
    def get(self, request, key):
        from .population_repository import PopulationRepository
        import json

        repository = PopulationRepository()
        searched_population = repository.select_pop_future_by_name(2000)
        json_population = json.dumps(searched_population, ensure_ascii=False)
        return HttpResponse(json_population, content_type="application/json")