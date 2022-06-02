# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AgeLimit(models.Model):
    age_limit_id = models.IntegerField(db_column='Age_Limit_Id', primary_key=True)  # Field name made lowercase.
    age_limit = models.IntegerField(db_column='Age_Limit')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Age_Limit'


class AnimeContent(models.Model):
    anime_id = models.IntegerField(db_column='Anime_Id', primary_key=True)  # Field name made lowercase.
    manga = models.ForeignKey('MangaContent', models.DO_NOTHING, db_column='Manga_Id', blank=True, null=True)  # Field name made lowercase.
    age_limit = models.ForeignKey(AgeLimit, models.DO_NOTHING, db_column='Age_Limit_Id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Anime_Content'


class AnimeGenres(models.Model):
    genres = models.OneToOneField('Genres', models.DO_NOTHING, db_column='Genres_Id', primary_key=True)  # Field name made lowercase.
    anime = models.ForeignKey(AnimeContent, models.DO_NOTHING, db_column='Anime_Id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Anime_Genres'
        unique_together = (('genres', 'anime'),)


class AnimeInfoByStudio(models.Model):
    season_id = models.IntegerField(db_column='Season_Id', primary_key=True)  # Field name made lowercase.
    anime_id = models.IntegerField(db_column='Anime_Id')  # Field name made lowercase.
    studio = models.ForeignKey('Studio', models.DO_NOTHING, db_column='Studio_Id')  # Field name made lowercase.
    anime_status = models.CharField(db_column='Anime_Status', max_length=45)  # Field name made lowercase.
    opening_length = models.IntegerField(db_column='Opening_Length')  # Field name made lowercase.
    release_date = models.CharField(db_column='Release_Date', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Anime_Info_By_Studio'
        unique_together = (('season_id', 'anime_id', 'studio'),)


class AnimeNames(models.Model):
    anime_names_id = models.IntegerField(db_column='Anime_Names_Id', primary_key=True)  # Field name made lowercase.
    russian_name = models.CharField(db_column='Russian_Name', max_length=45)  # Field name made lowercase.
    english_name = models.CharField(db_column='English_Name', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Anime_Names'


class AnimeRating(models.Model):
    user = models.OneToOneField('Profiles', models.DO_NOTHING, db_column='User_Id', primary_key=True)  # Field name made lowercase.
    anime = models.ForeignKey(AnimeContent, models.DO_NOTHING, db_column='Anime_Id')  # Field name made lowercase.
    season_id = models.IntegerField(db_column='Season_Id')  # Field name made lowercase.
    score = models.IntegerField(db_column='Score')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Anime_Rating'
        unique_together = (('user', 'anime', 'season_id'),)


class AnimeType(models.Model):
    anime_type_id = models.IntegerField(db_column='Anime_Type_Id', primary_key=True)  # Field name made lowercase.
    anime_type_name = models.CharField(db_column='Anime_Type_Name', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Anime_Type'


class Author(models.Model):
    author_id = models.IntegerField(db_column='Author_Id', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='First_Name', max_length=45)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_Name', max_length=45)  # Field name made lowercase.
    patrnymic = models.CharField(db_column='Patrnymic', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Author'


class Chapters(models.Model):
    chapter_id = models.IntegerField(db_column='Chapter_Id', primary_key=True)  # Field name made lowercase.
    manga = models.ForeignKey('MangaContent', models.DO_NOTHING, db_column='Manga_Id')  # Field name made lowercase.
    chapter_name = models.CharField(db_column='Chapter_Name', max_length=45)  # Field name made lowercase.
    chapter_url = models.CharField(db_column='Chapter_URL', max_length=45)  # Field name made lowercase.
    date_release = models.CharField(db_column='Date_Release', max_length=45)  # Field name made lowercase.
    chapter_number = models.IntegerField(db_column='Chapter_Number')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Chapters'
        unique_together = (('chapter_id', 'manga'),)


class Genres(models.Model):
    genres_id = models.IntegerField(db_column='Genres_Id', primary_key=True)  # Field name made lowercase.
    genres_name = models.CharField(db_column='Genres_Name', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Genres'


class MangaContent(models.Model):
    manga_id = models.IntegerField(db_column='Manga_Id', primary_key=True)  # Field name made lowercase.
    manga_names = models.ForeignKey('MangaNames', models.DO_NOTHING, db_column='Manga_Names_Id')  # Field name made lowercase.
    manga_description = models.CharField(db_column='Manga_Description', max_length=45)  # Field name made lowercase.
    author = models.ForeignKey(Author, models.DO_NOTHING, db_column='Author_Id')  # Field name made lowercase.
    manga_type = models.ForeignKey('MangaType', models.DO_NOTHING, db_column='Manga_Type_Id')  # Field name made lowercase.
    release_date_id = models.CharField(db_column='Release_Date_Id', max_length=45)  # Field name made lowercase.
    manga_status_tittle = models.CharField(db_column='Manga_Status_Tittle', max_length=45)  # Field name made lowercase.
    age_limit = models.ForeignKey(AgeLimit, models.DO_NOTHING, db_column='Age_Limit_Id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Manga_Content'


class MangaGenres(models.Model):
    genres = models.OneToOneField(Genres, models.DO_NOTHING, db_column='Genres_Id', primary_key=True)  # Field name made lowercase.
    manga = models.ForeignKey(MangaContent, models.DO_NOTHING, db_column='Manga_Id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Manga_Genres'
        unique_together = (('genres', 'manga'),)


class MangaNames(models.Model):
    manga_names_id = models.IntegerField(db_column='Manga_Names_Id', primary_key=True)  # Field name made lowercase.
    russian_name = models.CharField(db_column='Russian_Name', max_length=45)  # Field name made lowercase.
    english_name = models.CharField(db_column='English_Name', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Manga_Names'


class MangaRating(models.Model):
    user = models.OneToOneField('Profiles', models.DO_NOTHING, db_column='User_Id', primary_key=True)  # Field name made lowercase.
    manga = models.ForeignKey(MangaContent, models.DO_NOTHING, db_column='Manga_Id')  # Field name made lowercase.
    score = models.IntegerField(db_column='Score')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Manga_Rating'
        unique_together = (('user', 'manga'),)


class MangaType(models.Model):
    manga_type_id = models.IntegerField(db_column='Manga_Type_Id', primary_key=True)  # Field name made lowercase.
    manga_type_name = models.CharField(db_column='Manga_Type_Name', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Manga_Type'


class Pages(models.Model):
    page_id = models.IntegerField(db_column='Page_Id', primary_key=True)  # Field name made lowercase.
    chapter = models.ForeignKey(Chapters, models.DO_NOTHING, db_column='Chapter_Id')  # Field name made lowercase.
    chapter_url = models.CharField(db_column='Chapter_URL', max_length=150)  # Field name made lowercase.
    chapter_number = models.IntegerField(db_column='Chapter_Number')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pages'
        unique_together = (('page_id', 'chapter'),)


class Profiles(models.Model):
    user = models.OneToOneField('AuthUser', models.DO_NOTHING, db_column='User_Id', primary_key=True)  # Field name made lowercase.
    nickname = models.CharField(db_column='Nickname', max_length=45)  # Field name made lowercase.
    avatar = models.CharField(db_column='Avatar', max_length=45)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Profiles'


class Seasons(models.Model):
    season_id = models.IntegerField(db_column='Season_Id', primary_key=True)  # Field name made lowercase.
    anime = models.ForeignKey(AnimeContent, models.DO_NOTHING, db_column='Anime_Id')  # Field name made lowercase.
    anime_names = models.ForeignKey(AnimeNames, models.DO_NOTHING, db_column='Anime_Names_Id')  # Field name made lowercase.
    anime_description = models.CharField(db_column='Anime_Description', max_length=45)  # Field name made lowercase.
    anime_type = models.ForeignKey(AnimeType, models.DO_NOTHING, db_column='Anime_Type_Id')  # Field name made lowercase.
    studio = models.ForeignKey('Studio', models.DO_NOTHING, db_column='Studio_Id')  # Field name made lowercase.
    is_main_content = models.CharField(db_column='Is_Main_Content', max_length=45)  # Field name made lowercase.
    main_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='Main_Parent_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Seasons'
        unique_together = (('season_id', 'anime'),)


class Series(models.Model):
    series_id = models.IntegerField(db_column='Series_Id', primary_key=True)  # Field name made lowercase.
    season = models.ForeignKey(Seasons, models.DO_NOTHING, db_column='Season_Id')  # Field name made lowercase.
    english_name = models.CharField(db_column='English_Name', max_length=45)  # Field name made lowercase.
    russian_name = models.CharField(db_column='Russian_Name', max_length=45)  # Field name made lowercase.
    serises_url = models.CharField(db_column='Serises_URL', max_length=45)  # Field name made lowercase.
    opening_start = models.IntegerField(db_column='Opening_Start')  # Field name made lowercase.
    anime_id = models.IntegerField(db_column='Anime_Id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Series'
        unique_together = (('series_id', 'season', 'anime_id'),)


class Studio(models.Model):
    studio_id = models.IntegerField(db_column='Studio_Id', primary_key=True)  # Field name made lowercase.
    studio_name = models.CharField(db_column='Studio_Name', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Studio'


class Title(models.Model):
    title_id = models.IntegerField(db_column='Title_Id', primary_key=True)  # Field name made lowercase.
    anime = models.ForeignKey(AnimeContent, models.DO_NOTHING, db_column='Anime_Id')  # Field name made lowercase.
    manga = models.ForeignKey(MangaContent, models.DO_NOTHING, db_column='Manga_Id', blank=True, null=True)  # Field name made lowercase.
    title_name = models.CharField(db_column='Title_Name', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Title'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
