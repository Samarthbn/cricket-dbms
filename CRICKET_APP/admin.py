from django.contrib import admin
from CRICKET_APP.models import sign, team,umpire,player,matches,captain
# Register your models here.

admin.site.register(team)

admin.site.register(umpire)
admin.site.register(player)

admin.site.register(captain)

admin.site.register(matches)


admin.site.register(sign)




