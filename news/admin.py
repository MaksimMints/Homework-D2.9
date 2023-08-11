from django.contrib import admin
from .models import Category, Post, Author, PostCategory


# class AuthorAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    # list_display = [field.name for field in Author._meta.get_fields()] # генерируем список имён всех полей для более красивого отображения
    # list_display = ('title', 'author', 'postCategory')
    # list_filter = ('postCategory', 'author') # добавляем примитивные фильтры в нашу админку
    # search_fields = ('title') #

class PostCategoryInLine(admin.TabularInline):
    model = PostCategory
    extra = 1


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'dateCreation', 'title', 'author', 'post_categories')
    inlines = (PostCategoryInLine,)

    def post_categories(self, obj):
        categories = obj.postCategory.all()[:2]
        return ', '.join(map(str, categories))

    post_categories.short_description = 'Category'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'sub')
    inlines = (PostCategoryInLine,)

    def sub(self, obj):
        sub = obj.subscribers.all()[:3]
        return ', '.join(map(str, sub))

    sub.short_description = 'Subscribers'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
# admin.site.register(Author, AuthorAdmin)
admin.site.register(PostCategory)
