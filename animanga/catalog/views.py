from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Genres, AnimeGenres

from .models import *


class CatalogAPIView(APIView):
    def get(self, request):
        # return Response({1: 10, 2: 20})

        limit = int(request.data['limit'])
        page = int(request.data['page'])
        # return Response(dict(limit=limit, page=page))

        id_start = limit * (page - 1) + 1
        # id_start = limit * page
        # return Response(dict(id_start=id_start))

        id_end = id_start + limit
        # return Response(dict(id_start=id_start, id_end=id_end))

        id_range = range(id_start, id_end + 1)

        total_list = []
        for id in id_range:
            title = Title.objects.get(pk=id)
            anime_content = title.anime
            anime_genres_list: list[AnimeGenres] = AnimeGenres.objects.filter(anime=anime_content.pk)
            genres_list = [anime_genres_inst.genres for anime_genres_inst in anime_genres_list]


            # genres_names = [genre.genres_name for genre in genres_list]
            current_dict = {
                'id': id,
                'genres': [
                    {'id': genre.genres_id, 'name': genre.genres_name}
                           for genre in genres_list
                ],
                'title': {
                    'ru': 12,
                    'eng': 34,
                }
            }
            total_list.append(current_dict)

        total_dict = {"list": total_list}
        return Response(total_dict)

