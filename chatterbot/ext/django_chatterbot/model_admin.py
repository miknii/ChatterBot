from django.contrib import admin


class StatementAdmin(admin.ModelAdmin):
    list_display = ('text', 'in_response_to', 'conversation', 'rating', 'created_at', 'rating', )
    list_filter = ('text', 'created_at', 'conversation', )
    search_fields = ('text', )


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('name', )
    search_fields = ('name', )
