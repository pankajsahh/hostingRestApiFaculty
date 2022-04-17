# from django.shortcuts import render
# from faculty_api.models import Faculty,BookPublication,JournalPublication,ConfrencePublication
# from django.http import JsonResponse
# def faculty(request):
#     faculty = Faculty.objects.all()
#     data={
#         'faculty':list(faculty.values())
#     }
#     return JsonResponse(data)