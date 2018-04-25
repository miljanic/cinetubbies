from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import permission_classes, action
from rest_framework.response import Response

from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

from .models import Theater, THEATER_KIND, Voting
from .serializers import TheaterSerializer
from .permissions import IsAdminOrReadOnly, IsSystemAdmin
from django.db.models import Avg


class TheaterAPI(viewsets.ModelViewSet):
  queryset = Theater.objects.all()
  serializer_class = TheaterSerializer

  def list(self, request):
    num = request.GET.get('num')
    paginator = Paginator(self.queryset, num if num else 10)
    page = request.GET.get('page')
    theaters = paginator.get_page(page if page else 1)
    return Response(data=TheaterSerializer(theaters, many=True).data)

  @permission_classes((IsSystemAdmin,))
  def create(self, request):
    serializer = TheaterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(data=serializer.data)

  def retrieve(self, request, pk=None):
    theater = get_object_or_404(Theater, pk=pk)
    return Response(data=TheaterSerializer(theater).data)

  @permission_classes((IsAdminOrReadOnly,))
  def update(self, request, pk=None):
    theater = get_object_or_404(Theater, pk=pk)
    self.check_object_permissions(request, theater)
    serializer = TheaterSerializer(
      theater, data=request.data, partial=True
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(data=serializer.data)

  @permission_classes((IsSystemAdmin,))
  def update_admin(self, request, pk=None):
    theater = get_object_or_404(Theater, pk=pk)
    self.check_object_permissions(request, theater)
    theater.admin = request.data['admin']
    return Response(data=TheaterSerializer(theater).data)

  @permission_classes((IsSystemAdmin,))
  def destroy(self, request, pk=None):
    theater = get_object_or_404(Theater, pk=pk)
    self.check_object_permissions(request, theater)
    theater.delete()
    return Response(
      data={'message': 'Theater {0} successfully deleted.'.format(pk)}
    )

  @action(detail=False)
  def count(self, request):
    return Response(data=Theater.objects.count())

  # get all theaters and all cinemas
  @action(detail=False)
  def get_theaters(self, request):
    theaters = Theater.objects.all()
    return Response(TheaterSerializer(theaters, many=True).data)

  @action(detail=False)
  def update_rating(self, request):
    vote, _ = Voting.objects.get_or_create(user_id=request.user.id, theater_id=request.data['id'])
    vote.rating = request.data['rating']
    vote.save()
    rating = Voting.objects.filter(theater_id=request.data['id']).aggregate(rating=Avg('rating'))
    voters = len(Voting.objects.filter(theater_id=request.data['id']).all())
    data = {'rating':rating,'voters':voters}
    return Response(data)
