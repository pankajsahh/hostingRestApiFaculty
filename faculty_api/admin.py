from django.contrib import admin
from faculty_api.models import Faculty,JournalPublication,ConfrencePublication,BookPublication
# Register your models here.
admin.site.register(Faculty)
admin.site.register(JournalPublication)
admin.site.register(BookPublication)
admin.site.register(ConfrencePublication)