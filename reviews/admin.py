from django.contrib import admin
from .models import Review


# Admin interface for the Review model
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'rating', 'created_at', 'approved')
    list_filter = ('approved', 'created_at', 'rating')
    search_fields = ('title', 'content')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)
    approve_reviews.short_description = "Mark selected reviews as approved"


admin.site.register(Review, ReviewAdmin)
