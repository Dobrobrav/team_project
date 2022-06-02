from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *


class CatalogElementsAPIView(APIView):
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

        id_range = range(id_start, id_end)

        total_list = []
        for id in id_range:

            title = Title.objects.get(pk=id)
            # return Response({1: title.pk})
            anime_content = title.anime
            # return  Response({1: anime_content.pk})
            anime_genres_list = AnimeGenres.objects.filter(anime=anime_content.pk)
            # return Response({1: len(anime_genres_list)})
            # if anime_genres_list:
            #     return Response({1: 10})
            # return Response({2: 20})
            genres_list = [anime_genres_inst.genres for anime_genres_inst in anime_genres_list]
            # return Response({1: len(genres_list)})

            seasons = Seasons.objects.filter(anime=anime_content.pk)
            # return Response({1: len(seasons)})
            genres = [
                {
                    'id': genre.genres_id,
                    'name': genre.genres_name,
                }
                for genre in genres_list
            ]
            # return Response({1: genres})

            title_out = {
                'ru': title.title_russian_name,
                'eng': 'null',
            }
            # return Response({1: title_out})

            manga_id = title.manga.pk
            # return Response({1: manga_id})

            content = [
                {
                    'id': season.season_id,
                    'title': season.anime_names.russian_name
                }
                for season in seasons
            ]
            # return Response({1: 10})



            current_dict = {
                'id': id,
                'genres': genres,
                'title': title_out,
                # 'rate': anime_rating.score,
                'manga_id': manga_id,
                'content': content
            }
            total_list.append(current_dict)

        return Response({"list": total_list})


class BasicAnimeInfoAPIView(APIView):
    def get(self, request):

        anime_id = int(request.data['anime_id'])
        season_id = int(request.data['season_id'])
        # return Response({1: 10})

        title = {
            'rus': Title.objects.get(anime=anime_id).title_russian_name,
            'eng': 'null',
        }
        # return Response({1: 10})


        img = 'null'
        anime_genres_list = AnimeGenres.objects.filter(anime=anime_id)

        genres_list = [anime_genres_inst.genres for anime_genres_inst in anime_genres_list]
        genres = [
            {'id': genre.genres_id, 'name': genre.genres_name}
            for genre in genres_list
        ]
        # return Response({1: genres})

        age_distinction = AnimeContent.objects.get(pk=anime_id).age_limit.age_limit
        # return Response({1: age_distinction})


        season = Seasons.objects.get(anime=anime_id)
        studio = season.studio
        # return Response({1: studio.studio_name})

        description = season.anime_description


        anime_info = AnimeInfoByStudio.objects.get(studio=studio.pk, anime_id=anime_id, season_id=season_id)

        # return Response({'quantity': anime_info})

        studio = [
            {
                'id': anime_info.studio.studio_id,
                'name': studio.studio_name,
            }
        ]
        # return Response({1: studio})

        episode_duration = 'null'
        status = anime_info.anime_status

        manga_id = Title.objects.get(anime=anime_id).manga.manga_names.russian_name
        # return Response(manga_id)
        count_of_episodes = 'null'

        release_date = anime_info.release_date
        # anime_rating = AnimeRating.objects.get(Anime)
        # anime_rating =
        rate = 'null'

        total_dict = dict(
            anime_id=anime_id,
            title=title,
            img=img,
            genres=genres,
            description=description,
            age_distinction=age_distinction,
            studio=studio,
            episode_duration=episode_duration,
            status=status,
            manga_id=manga_id,
            count_of_episodes=count_of_episodes,
            release_date=release_date,
            rate=rate,
        )

        return Response(total_dict)


class CurrentContentInfoAPIView(APIView):
    def get(self, request):
        anime_id = request.data['anime_id']
        season_id = request.data['season_id']
        # return Response()

        id = season_id
        season = Seasons.objects.get(anime=anime_id, season_id=season_id)
        # return Response()


        title = Title.objects.get(anime=anime_id).title_russian_name
        # return Response()

        return Response(dict(
            id=id,
            title=title,
            parent_id='null', #в дальнейшем реализовать проверку на наличие
        ))


class RelatedSeasonAPIView(APIView):
    def get(self, request):
        anime_id = request.data['anime_id']
        season_id = request.data['season_id']

        related_seasons_info = [
            {
                "id": season.season_id,
                "type": season.anime_type.anime_type_name,
                "count_of_episodes": 'null',
                "title": season.anime_names.russian_name,
                "date_of_release": 'null',
            }
            for season in Seasons.objects.filter(main_parent_season=season_id)
        ]

        return Response(dict(list=related_seasons_info))


class ExistingMangaChaptersInfoAPIView(APIView):
    def get(self, request):
        manga_id = request.data['manga_id']

        existing_manga_chapters = Chapters.objects.filter(manga=manga_id)
        # return Response({1: len(existing_manga_chapters)})

        existing_manga_chapters_info = [
            {
                'id': chapter.chapter_id,
                'number': chapter.chapter_number,
                'title': chapter.chapter_name,
                'date': chapter.date_release,
            }
            for chapter in existing_manga_chapters
        ]

        return Response({"list": existing_manga_chapters_info})


class MangaInfoAPIView(APIView):
    def get(self, request):
        manga_id = request.data['manga_id']

        manga_content = MangaContent.objects.get(manga_id=manga_id)
        manga_names = manga_content.manga_names

        title_out = {
            'rus': manga_names.russian_name,
            'eng': manga_names.english_name,
        }
        # return Response()
        title = Title.objects.get(manga=manga_id)
        img = title.poster
        # return Response({1: img})

        manga_genres_list = MangaGenres.objects.filter(manga=manga_id)
        genres = [
            {
                'id': genre.genres_id,
                'name': genre.genres_name,
            }
            for genre in (manga_genre.genres
                          for manga_genre in manga_genres_list)
        ]
        # return Response({"genres": genres})

        description = manga_content.manga_description
        # return Response({1: description})

        age_distinction = manga_content.age_limit.age_limit
        # return Response({1: age_distinction})

        author = manga_content.author
        # return Response({1: author.last_name})
        author_out = {
            'id': author.pk,
            'name': f"{author.first_name} {author.last_name}",
        }
        # return Response({1: author_out})

        status = manga_content.manga_status_tittle
        # return Response({1: status})

        anime_id = title.anime.pk
        # return Response({1: anime_id})

        release_date = manga_content.release_date_id
        # return Response({1: release_date})

        rate = 'null'

        return Response(dict(
            title=title_out,
            img=img,
            genres=genres,
            description=description,
            age_distinction=age_distinction,
            author=author_out,
            status=status,
            anime_id=anime_id,
            release_date=release_date,
            rate=rate,
        ))


class ConcreteChapterPagesAPIView(APIView):
    def get(self, request):
        manga_id = request.data['manga_id']
        chapter_number = request.data['chapter_number']
        # return Response()

        chapter = Chapters.objects.get(chapter_number=chapter_number)
        pages = Pages.objects.filter(chapter=chapter.chapter_id)
        # return Response()

        return Response(
            [
                {
                    'id': page.page_id,
                    'url': page.chapter_url,
                }
                for page in pages
            ]
        )
