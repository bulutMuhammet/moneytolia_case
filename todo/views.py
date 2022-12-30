import random
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Todo
from .permissions import IsOwnerOrAdmin
from .serializers import TodoSerializer


class TodoListCreateView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    filterset_fields = ('id', 'title', 'user', 'created_date', 'completed')


# this gets user's todos
class TodoUserListView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(user=request.user)
        return self.list(request, *args, **kwargs)


class TodoView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]


class RandomTodoView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        pks = self.queryset.values_list('pk', flat=True).order_by('id')
        random_pk = random.choice(pks)
        return self.queryset.filter(pk=random_pk)
