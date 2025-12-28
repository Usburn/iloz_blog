from django.contrib import admin

from .models import Reader , Project, Author, Comment, Article

# Register your models here.


admin.site.register(Reader)



class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "authors")
    list_filter = ("date",)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Article, ArticleAdmin)

