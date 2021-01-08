from django.shortcuts import render
from django.views.generic.base import View, TemplateView

from django.http import HttpResponse, JsonResponse

class HomeView(TemplateView):
    template_name = "surname/home.html"

class SearchView(View):
    def get(self, request, key):
        from .surname_repository import SurnameRepository
        import json

        repository = SurnameRepository()
        searched_surname = repository.select_surname_by_name(key)
        json_surname = json.dumps(searched_surname, ensure_ascii=False)
        return HttpResponse(json_surname, content_type="application/json")

class SearchDetailView(View):
    def get(self, request, key):
        from .surname_repository import SurnameRepository
        import json

        repository = SurnameRepository()
        searched_surname = repository.select_detail_surname_by_name(key)
        json_surname = json.dumps(searched_surname, ensure_ascii=False)
        return HttpResponse(json_surname, content_type="application/json")

# class StocksDetailView(View):
#     def get(self, request, pk):
#         from .surname_repository import SurnameRepository
#         import json

#         stock = StocksRepository().select_stockmaster_by_symbol(pk)
        
#         stock_info = fdr.DataReader(pk, '20200101').fillna('').reset_index()
#         stock_info["Date"] = stock_info['Date'].astype('string')
#         stock['stats'] = stock_info.values.tolist()
#         serialized_stocks = json.dumps([stock], ensure_ascii=False) #
#         return HttpResponse(serialized_stocks, content_type="application/json")