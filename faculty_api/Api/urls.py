from django.urls import path
# from faculty_api.Api.views import faculty,books,confrences, faculty_id,journals
from faculty_api.Api.views import faculty_id,faculty,Books_id,Books,journal,journal_id,confrence,confrence_id

urlpatterns = [
    path('faculty/',faculty.as_view(),name='faculty_list'),
    path('faculty/<int:pk>',faculty_id.as_view(),name='faculty_id'),
    path('books/',Books.as_view(),name='Book_list'),
    path('books/<int:pk>',Books_id.as_view(),name='Book_id'),
    path('journals/',journal.as_view(),name='journal_list'),
    path('journals/<int:pk>',journal_id.as_view(),name='journal_id'),
    path('confrences/',confrence.as_view(),name='confrence_list'),
    path('confrences/<int:pk>',confrence_id.as_view(),name='confrence_id'),
    # path('confrences/',confrences,name='confrence_list'),
    # path('journals/',journals,name='journal_list'),
]
