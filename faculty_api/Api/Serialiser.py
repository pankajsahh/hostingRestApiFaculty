
from rest_framework import serializers
from faculty_api.models import BookPublication, Faculty,ConfrencePublication,JournalPublication

#model serializer
    # journalserializer 
class journalserializer(serializers.ModelSerializer):
     class Meta:
          model=JournalPublication
          fields="__all__"


class confrenceserializer(serializers.ModelSerializer):
     class Meta:
          model=ConfrencePublication
          fields="__all__"



class Bookserializer(serializers.ModelSerializer):
     class Meta:
          model =BookPublication
          fields = "__all__"





class FacultySerializer(serializers.ModelSerializer):
     BookPublication = Bookserializer(many=True,read_only=True)
     JournalPublication = journalserializer(many=True,read_only=True)
     ConfrencePublication = confrenceserializer(many=True,read_only=True)
     class Meta:
          model = Faculty
          fields = "__all__"
     


# normal serializers
"""
class FacultySerializer(serializers.Serializer):
     id = serializers.IntegerField(read_only=True)
     Name = serializers.CharField()
     Department = serializers.CharField()
     Designation = serializers.CharField()
     def create(self, validated_data):
         return Faculty.objects.create(**validated_data)


class FacultychildSerializer(serializers.Serializer):
     id = serializers.IntegerField(read_only=True)
     Name = serializers.CharField()
     Department = serializers.CharField()
     Designation = serializers.CharField()

     def update(self, instance, validated_data):
          instance.Name = validated_data.get('Name',instance.Name)
          instance.Department = validated_data.get('Department',instance.Department)
          instance.Designation = validated_data.get('Designation',instance.Designation)
          instance.save()
          return instance



class Bookserializer(serializers.Serializer):
     id = serializers.IntegerField(read_only=True)
     faculty = serializers.CharField()
     Book_title=serializers.CharField()
     Year = serializers.DateField()
     Co_Author = serializers.CharField(allow_blank=True, allow_null=True)
     Edition = serializers.IntegerField()
     Publisher = serializers.CharField()
     def create(self, validated_data):
         return BookPublication.objects.create(**validated_data)


class book_id_serializer(serializers.Serializer):
     id = serializers.IntegerField(read_only=True)
     faculty = serializers.CharField()
     Book_title=serializers.CharField()
     Year = serializers.DateField()
     Co_Author = serializers.CharField(allow_blank=True, allow_null=True)
     Edition = serializers.IntegerField()
     Publisher = serializers.CharField()
     def update(self, instance, validated_data):
          instance.faculty = validated_data.get('faculty',instance.faculty)
          instance.Book_title= validated_data.get('Book_title',instance.Book_title)
          instance.Year = validated_data.get('Year',instance.Year)
          instance.Co_Author =  validated_data.get('Co_Author',instance.Co_Author)
          instance.Edition =  validated_data.get('Edition',instance.Edition)
          instance.Publisher =  validated_data.get('Publisher',instance.Publisher)
          instance.save()
          return instance



class Confrenceserializer(serializers.Serializer):
     id = serializers.IntegerField(read_only=True)
     faculty=serializers.CharField()
     Organizer=serializers.CharField()
     Year = serializers.DateField()
     Co_Author = serializers.CharField()
     Proceeding=serializers.IntegerField()




class Journalserializer(serializers.Serializer):
     id = serializers.IntegerField(read_only=True)
     faculty=serializers.CharField()
     Paper_title=serializers.CharField()
     Year = serializers.DateField()
     Co_Author = serializers.CharField()
     Volume = serializers.IntegerField()
     Publisher = serializers.CharField()
     Indexing=serializers.IntegerField()

     """