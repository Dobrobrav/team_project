from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *


class CatalogElementsAPIView(APIView):
    def post(self, request):
        limit = int(request.data['limit'])  # 1
        page = int(request.data['page'])  # 2
        id_start = limit * (page - 1) + 1
        id_end = id_start + limit
        count_of_els = len(Title.objects.all())

        if count_of_els < id_end - 1:
            id_end = count_of_els + 1

        id_range = range(id_start, id_end)

        total_list = []
        for id in id_range:
            title = Title.objects.get(pk=id)
            anime_content = title.anime
            img = title.poster
            age_distinction = anime_content.age_limit.age_limit
            anime_genres_list = AnimeGenres.objects.filter(anime=anime_content.pk)
            genres_list = [anime_genres_inst.genres for anime_genres_inst in anime_genres_list]
            seasons = Seasons.objects.filter(anime=anime_content.pk)

            genres = [
                {
                    'id': genre.genres_id,
                    'name': genre.genres_name,
                }
                for genre in genres_list
            ]

            title_out = {
                'ru': title.title_russian_name,
                'eng': 'null',
            }

            manga_id = 'null'
            try:
                manga_id = title.manga.pk
            except:
                pass

            content = [
                {
                    'id': season.season_id,
                    'title': season.anime_names.russian_name,
                }
                for season in seasons if season.is_main_content == "true"
            ]

            current_dict = {
                'id': id,
                'genres': genres,
                'title': title_out,
                'age_distinction': age_distinction,
                'img': img,
                'manga_id': manga_id,
                'content': content,
                'count_of_els': count_of_els,
            }
            total_list.append(current_dict)

        return Response({"list": total_list})


class BasicAnimeInfoAPIView(APIView):
    def post(self, request):

        season_id = int(request.data['season_id'])
        anime_content = Seasons.objects.get(season_id=season_id)
        anime_id = anime_content.pk

        title = {
            'rus': Title.objects.get(anime=anime_id).title_russian_name,
            'eng': 'null',
        }

        img = Title.objects.get(anime=anime_id).poster

        anime_genres_list = AnimeGenres.objects.filter(anime=anime_id)

        genres_list = [anime_genres_inst.genres for anime_genres_inst in anime_genres_list]
        genres = [
            {'id': genre.genres_id, 'name': genre.genres_name}
            for genre in genres_list
        ]

        age_distinction = AnimeContent.objects.get(pk=anime_id).age_limit.age_limit

        season = Seasons.objects.get(season_id=season_id)
        studio = season.studio
        chapter_id = season.chapter_id

        description = season.anime_description

        anime_info = AnimeInfoByStudio.objects.get(season_id=season_id)
        opening_length = anime_info.opening_length


        studio = [
            {
                'id': anime_info.studio.studio_id,
                'name': studio.studio_name,
            }
        ]

        episode_duration = 'null'
        status = anime_info.anime_status
        manga_id = 'null'
        try:
            manga_id = Title.objects.get(anime=anime_id).manga.manga_id
        except:
            pass

        series = season.series_set
        count_of_episodes = series.count()
        release_date = anime_info.release_date
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
            chapter_id=chapter_id,
            count_of_episodes=count_of_episodes,
            release_date=release_date,
            rate=rate,
            opening_length=opening_length,
        )

        return Response(total_dict)


class ConcreteAnimeEpisode(APIView):
    def post(self, request):
        episode_number = request.data['episode_number']
        season_id = request.data['season_id']
        episode = Series.objects.get(series_id=episode_number, season=season_id)
        opening_start = episode.opening_start

        return Response({
            'title': episode.russian_name,
            'url': episode.serises_url,
            'opening_start': opening_start,
        })


class AvailableContentForAnime(APIView):
    def post(self, request):
        anime_id = request.data['anime_id']

        available_seasons = Seasons.objects.filter(anime=anime_id)
        available_seasons_info = [
            {
                'id': season.season_id,
                'title': season.anime_names.russian_name,
                'type': season.anime_type.anime_type_name,
                'status': AnimeInfoByStudio.objects.get(
                    season_id=season.season_id,
                    anime_id=anime_id,
                    studio=season.studio.studio_id,
                ).anime_status,
                'count_of_episodes': 'null',
                'rate': 'null',
                'count_of_related_content': len(Seasons.objects.filter(main_parent_season=season.season_id)),
                'img': Title.objects.get(anime=anime_id).poster,
                'date_of_release': AnimeInfoByStudio.objects.get(
                    season_id=season.season_id,
                    anime_id=anime_id,
                    studio=season.studio.studio_id,
                ).release_date
            }
            for season in available_seasons if season.is_main_content == 'true'
        ]

        return Response({'list': available_seasons_info})


class CurrentContentInfoAPIView(APIView):
    def post(self, request):
        anime_id = request.data['anime_id']
        season_id = request.data['season_id']

        id = season_id
        season = Seasons.objects.get(anime=anime_id, season_id=season_id)

        title = Seasons.objects.get(season_id=season_id).anime_names.russian_name

        parent_id = 'null'

        if season.is_main_content == 'false':
            parent_id = season.main_parent_season.season_id

        return Response(dict(
            id=id,
            title=title,
            parent_id=parent_id,  # в дальнейшем реализовать проверку на наличие
        ))


class RelatedSeasonAPIView(APIView):
    def post(self, request):
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
    def post(self, request):
        manga_id = request.data['manga_id']

        existing_manga_chapters = Chapters.objects.filter(manga=manga_id)

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
    def post(self, request):
        manga_id = request.data['manga_id']

        manga_content = MangaContent.objects.get(manga_id=manga_id)
        manga_names = manga_content.manga_names

        title_out = {
            'rus': manga_names.russian_name,
            'eng': manga_names.english_name,
        }
        title = Title.objects.get(manga=manga_id)
        img = title.poster

        manga_genres_list = MangaGenres.objects.filter(manga=manga_id)
        genres = [
            {
                'id': genre.genres_id,
                'name': genre.genres_name,
            }
            for genre in (manga_genre.genres
                          for manga_genre in manga_genres_list)
        ]

        description = manga_content.manga_description

        age_distinction = manga_content.age_limit.age_limit

        author = manga_content.author
        author_out = {
            'id': author.pk,
            'name': f"{author.first_name} {author.last_name}",
        }

        status = manga_content.manga_status_tittle

        anime_id = title.anime.pk

        release_date = manga_content.release_date_id

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
    def post(self, request):
        manga_id = request.data['manga_id']
        chapter_number = request.data['chapter_number']

        chapter = Chapters.objects.get(manga=manga_id, chapter_number=chapter_number)
        pages = Pages.objects.filter(chapter=chapter.chapter_id)

        return Response(
            [
                {
                    'id': page.page_id,
                    'url': page.chapter_url,
                }
                for page in pages
            ]
        )


class ConcreteMangaNameAPIView(APIView):
    def post(self, request):
        manga_id = request.data['manga_id']

        return Response({
            'title': MangaContent.objects.get(pk=manga_id).manga_names.russian_name
        })


class UserInfoAPIView(APIView):  # Таблица Profiles пустая - надо заполнить!(хз, работает ли)
    def post(self, request):
        user_id = request.data['user_id']

        profile = Profiles.objects.get(pk=user_id)
        return Response()

        img = profile.avatar

        nickname = profile.nickname
        count_of_titles = len(AnimeRating.objects.filter(user=user_id))
        favourite_genre = 'Может не надо?(('
        status = profile.status

        return Response(dict(
            id=user_id,
            img=img,
            nickname=nickname,
            count_of_titles=count_of_titles,
            favourite_genre=favourite_genre,
            status=status,
        ))
