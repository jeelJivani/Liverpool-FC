from django.contrib import admin
from home.models import *


admin.site.register(Contact)
admin.site.register(Blog)
admin.site.register(Position)
admin.site.register(Player)
admin.site.register(PlayerID)
admin.site.register(Specs)
admin.site.register(Student)

class PlayerRating(admin.ModelAdmin):
    list_display=['player','specs','rating']
admin.site.register(SpecsRating,PlayerRating)



