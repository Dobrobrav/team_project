from django.urls import path
from .views import *


urlpatterns = [
    path('catalog_elements/', (CatalogElementsAPIView.as_view())),
    path('basic_anime_info/', (BasicAnimeInfoAPIView.as_view())),
    path('concrete_anime_episode/', (ConcreteAnimeEpisode.as_view())),
    path('available_content_for_anime/', (AvailableContentForAnime.as_view())),

    path('current_content_info/', (CurrentContentInfoAPIView.as_view())),
    path('related_seasons_info/', (RelatedSeasonAPIView.as_view())),
    path('existing_manga_chapters_info/', (ExistingMangaChaptersInfoAPIView.as_view())),
    path('manga_info/', (MangaInfoAPIView.as_view())),
    path('concrete_chapter_pages/', (ConcreteChapterPagesAPIView.as_view())),
    path('concrete_manga_name/', (ConcreteMangaNameAPIView.as_view())),
    # Profile
    # path('user_info/', (UserInfoAPIView.as_view())),
]