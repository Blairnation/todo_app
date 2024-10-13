from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import Todoserializer
from .models import Todo
from rest_framework import status

# Create your views here.
class TodoListView(APIView):
      serializer_class = Todoserializer

      def get(self, request, todo_id=None):
          try:
            if todo_id:
                todo = Todo.objects.get(id=todo_id)
                serializer = Todoserializer(todo, many=False)
                return Response({'data':serializer.data,
                                'status':status.HTTP_200_OK},
                                  status=status.HTTP_200_OK)
            
                
            todo = Todo.objects.all()
            serializer = Todoserializer(todo, many=True)
            return Response({'data':serializer.data,
                             'status':status.HTTP_200_OK},
                              status=status.HTTP_200_OK)
          except:
              return Response({'status':status.HTTP_404_NOT_FOUND,
                               'message':'Something went wrong'},
                                status=status.HTTP_404_NOT_FOUND)
          

class CreateTodoView(APIView):
      serializer_class = Todoserializer

      def post(self, request):
          try:
              body = request.data['body']
              todo = Todo.objects.create(body=body)
              serializer = Todoserializer(todo)
              return Response({'data':serializer.data,
                             'status':status.HTTP_200_OK},
                              status=status.HTTP_200_OK)
          except Exception as e:
              return Response({'Status':status.HTTP_400_BAD_REQUEST,
                               'message':str(e)},
                                status=status)
          
class EditTodoView(APIView):
    serializer_class = Todoserializer
       
    def put( self, request, todo_id):
        try:
            data = Todoserializer(data=request.data)
            data.is_valid(raise_exception=False)
            requested_data = data.data
            todo = Todo.objects.get(id=todo_id)

            if requested_data['completed'] == True:
                todo.completed = True
            else:
                todo.completed = False

            if requested_data['body']:
                todo.body = requested_data['body']

            todo.save()        
            return Response({ 'Message':'Todo Edited Successfully',
                             'Data':requested_data},
                              status=status.HTTP_200_OK)  
        
        except Todo.DoesNotExist:
            return Response({'Error': 'Todo not found'},
                             status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'Error':str(e)},
                             status=status.HTTP_400_BAD_REQUEST) 
   

class DeleteTodoView(APIView):
    
    def delete(self, request, todo_id):
        try:
          todo = Todo.objects.get(id=todo_id)
          todo.delete()

          return Response({ 'Message':'Todo Removed Successfully',
                              },
                              status=status.HTTP_200_OK)  
      
        except Todo.DoesNotExist:
           return Response({'Error': 'Todo not found'},
                            status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
           return Response({'Error':str(e)},
                            status=status.HTTP_400_BAD_REQUEST) 
       