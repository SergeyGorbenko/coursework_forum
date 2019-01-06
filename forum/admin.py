from django.contrib import admin
from forum.models import *


class LikeFilter(admin.SimpleListFilter):
    title = 'Likes'
    parameter_name = 'like'

    def lookups(self, request, model_admin):
        return (
            ('10', '< 10'),
            ('50', '10 - 50'),
            ('100', '50 - 100'),
            ('500', '100 - 500'),
            ('1000', '500 - 1000'),
            ('10000', '> 1000'),
        )

    def queryset(self, request, queryset):
        if self.value() == '10':
            return queryset.filter(like__gte=0,
                                   like__lte=10)
        if self.value() == '50':
            return queryset.filter(like__gte=10,
                                   like__lte=50)
        if self.value() == '100':
            return queryset.filter(like__gte=50,
                                   like__lte=100)
        if self.value() == '500':
            return queryset.filter(like__gte=100,
                                   like__lte=500)
        if self.value() == '1000':
            return queryset.filter(like__gte=500,
                                   like__lte=1000)
        if self.value() == '10000':
            return queryset.filter(like__gte=1000)


class DislikeFilter(admin.SimpleListFilter):
    title = 'Disikes'
    parameter_name = 'dislike'

    def lookups(self, request, model_admin):
        return (
            ('10', '< 10'),
            ('50', '10 - 50'),
            ('100', '50 - 100'),
            ('500', '100 - 500'),
            ('1000', '500 - 1000'),
            ('10000', '> 1000'),
        )

    def queryset(self, request, queryset):
        if self.value() == '10':
            return queryset.filter(dislike__gte=0,
                                   dislike__lte=10)
        if self.value() == '50':
            return queryset.filter(dislike__gte=10,
                                   dislike__lte=50)
        if self.value() == '100':
            return queryset.filter(dislike__gte=50,
                                   dislike__lte=100)
        if self.value() == '500':
            return queryset.filter(dislike__gte=100,
                                   dislike__lte=500)
        if self.value() == '1000':
            return queryset.filter(dislike__gte=500,
                                   dislike__lte=1000)
        if self.value() == '10000':
            return queryset.filter(dislike__gte=1000)


class PostInline(admin.TabularInline):
    model = Post


class CommentInline(admin.TabularInline):
    model = Comment


class TagInline(admin.TabularInline):
    model = Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('theme', 'creator', 'like', 'dislike', 'display_tags')
    fieldsets = (
        (None, {
            'fields': (('theme', 'creator'),)
        }),
        ('Popularity', {
            'fields': (('like', 'dislike'),)
        }),
        ('Context', {
            'fields': ('context',)
        }),
    )
    list_filter = ('creator', 'create', LikeFilter, DislikeFilter)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('creator', 'create', 'post', LikeFilter, DislikeFilter)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        ('About', {
            'fields': (('authors', 'edition', 'tags'), 'creator',)
        }),
        ('Context', {
            'fields': (('description',), ('file',),)
        }),
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'creator', 'count')


@admin.register(UserProfile)
class UserProfiletAdmin(admin.ModelAdmin):
    inlines = [PostInline, CommentInline, TagInline]
