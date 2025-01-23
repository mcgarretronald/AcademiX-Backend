from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from school.models import School
from .serializers import SchoolSerializer

# SCHOOL API
class SchoolCreate(APIView):
    def post(self, request):
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SchoolUpdate(APIView):
    def put(self, request, pk):
        try:
            school = School.objects.get(pk=pk)
        except School.DoesNotExist:
            return Response({'error': 'School not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SchoolSerializer(school, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SchoolDelete(APIView):
    def delete(self, request, pk):
        try:
            school = School.objects.get(pk=pk)
        except School.DoesNotExist:
            return Response({'error': 'School not found'}, status=status.HTTP_404_NOT_FOUND)

        school.delete()
        return Response({'message': 'School deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
