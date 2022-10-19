from django.contrib import admin
from api_user.models import UserReview, UserHighlight, UserBookActivity, UserLibraryActivity
# Register your models here.

admin.site.register(UserReview)
admin.site.register(UserHighlight)
admin.site.register(UserBookActivity)
admin.site.register(UserLibraryActivity)
