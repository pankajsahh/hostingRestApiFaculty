
from rest_framework.response import Response
from rest_framework.views import APIView
from faculty_api.Api.Serialiser import Bookserializer, FacultySerializer, journalserializer,confrenceserializer
from faculty_api.models import Faculty,BookPublication, JournalPublication,ConfrencePublication
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class faculty(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        faculty = Faculty.objects.all()
        serializer = FacultySerializer(faculty,many=True)
        return Response(serializer.data)
    def post(self,request):
        
        serializer = FacultySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class faculty_id(APIView):

    def get(self,request,pk):
        try:
            faculty = Faculty.objects.get(pk=pk)
        except Faculty.DoesNotExist:
            return Response({ 'error:faculty'' id not found'},status=status.HTTP_404_NOT_FOUND)
        searializer = FacultySerializer(faculty)
        return Response(searializer.data)

    def put(self,request,pk):
        faculty = Faculty.objects.get(pk=pk)
        searializer = FacultySerializer(faculty,data=request.data)
        if searializer.is_valid():
            searializer.save()
            return Response(searializer.data)
        else:
            return Response(searializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        faculty=Faculty.objects.get(pk=pk)
        faculty.delete()
        return Response({"faculty":"faculty deleted sucessfully"},status=status.HTTP_204_NO_CONTENT)

class Books(APIView):
    def get(self,request):
        books = BookPublication.objects.all()
        serializer = Bookserializer(books,many=True)
        return Response(serializer.data)

    def post(self,request):
        
        serializer = Bookserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Books_id(APIView):
    def get(self,request,pk):
        try:
            book = BookPublication.objects.get(pk=pk)
        except BookPublication.DoesNotExist:
            return Response({'error':'book id not found'},status=status.HTTP_404_NOT_FOUND)
        searializer = Bookserializer(book)
        return Response(searializer.data)
        


    def put(self,requst,pk):
        book = BookPublication.objects.get(pk=pk)
        searializer = Bookserializer(book,data=requst.data)
        if searializer.is_valid():
            searializer.save()
            return Response(searializer.data)
        else:
            return Response(searializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        book=BookPublication.objects.get(pk=pk)
        book.delete()
        return Response({"content":" book content deleted sucessfully"},status=status.HTTP_204_NO_CONTENT)



class journal(APIView):
    def get(self,request):
        journal = JournalPublication.objects.all()
        serializer = journalserializer(journal,many=True)
        return Response(serializer.data)

    def post(self,request):
        
        serializer = journalserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class journal_id(APIView):
    def get(self,request,pk):
        try:
            journal = JournalPublication.objects.get(pk=pk)
        except JournalPublication.DoesNotExist:
            return Response({'error':'journal id not found'},status=status.HTTP_404_NOT_FOUND)
        searializer = journalserializer(journal)
        return Response(searializer.data)
        


    def put(self,requst,pk):
        book = JournalPublication.objects.get(pk=pk)
        searializer = journalserializer(book,data=requst.data)
        if searializer.is_valid():
            searializer.save()
            return Response(searializer.data)
        else:
            return Response(searializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        book=JournalPublication.objects.get(pk=pk)
        book.delete()
        return Response({"content":"journal content deleted sucessfully"},status=status.HTTP_204_NO_CONTENT)




class confrence(APIView):
    def get(self,request):
        confrence = ConfrencePublication.objects.all()
        serializer = confrenceserializer(confrence,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = confrenceserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class confrence_id(APIView):
    def get(self,request,pk):
        try:
            confrence = ConfrencePublication.objects.get(pk=pk)
        except ConfrencePublication.DoesNotExist:
            return Response({'error':'confrence id not found'},status=status.HTTP_404_NOT_FOUND)
        searializer = confrenceserializer(confrence)
        return Response(searializer.data)
        


    def put(self,requst,pk):
        confrence = ConfrencePublication.objects.get(pk=pk)
        searializer = confrenceserializer(confrence,data=requst.data)
        if searializer.is_valid():
            searializer.save()
            return Response(searializer.data)
        else:
            return Response(searializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        confrence=ConfrencePublication.objects.get(pk=pk)
        confrence.delete()
        return Response({"content":"confrence content deleted sucessfully"},status=status.HTTP_204_NO_CONTENT)

# # function based view
"""
@api_view(['Get','Post'])
def faculty(request):
    if request.method == 'GET':
        try:
            faculty = Faculty.objects.all()
        except Faculty.DoesNotExist:
            return Response({'error':'movie id not found'},status=status.HTTP_404_NOT_FOUND)
        serializer = FacultySerializer(faculty,many=True)
        return Response(serializer.data) 
    if request.method == 'POST':
        serializer = FacultySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET','PUT','DELETE'])
def faculty_id(request,pk):
    if request.method == 'GET':
        try:
            faculty = Faculty.objects.get(pk=pk)
        except Faculty.DoesNotExist:
            return Response({'error':'movie id not found'},status=status.HTTP_404_NOT_FOUND)
        searializer = FacultychildSerializer(faculty)
        return Response(searializer.data)

    if request.method == 'PUT':
        faculty = Faculty.objects.get(pk=pk)
        searializer = FacultychildSerializer(faculty,data=request.data)
        if searializer.is_valid():
            searializer.save()
            return Response(searializer.data)
        else:
            return Response(searializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method =='DELETE':
        faculty=Faculty.objects.get(pk=pk)
        faculty.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





@api_view(['Get','Post'])
def books(request):

    if request.method == 'GET':
        try:
            books = BookPublication.objects.all()
        except BookPublication.DoesNotExist:
            return Response({'error':'book List not found'},status=status.HTTP_404_NOT_FOUND)
        serializer = Bookserializer(books,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = Bookserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)






@api_view(['Get','Post'])
def confrences(request):
    confrences = ConfrencePublication.objects.all()
    serializer = Confrenceserializer(confrences,many=True)
    return Response(serializer.data)




@api_view(['Get','Post'])
def journals(request):
    journals = JournalPublication.objects.all()
    serializer = Journalserializer(journals,many=True)
    return Response(serializer.data)
"""