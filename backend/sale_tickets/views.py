from django.shortcuts import render
from .serializers import TicketOnSaleSerializer
from .models import TicketOnSale
from rest_framework import viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response
# from .permissions import IsCreatorOrReadOnly
from django.shortcuts import get_object_or_404

class TicketOnSaleViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows tickets on sale to be viewed or edited.
  """
  queryset = TicketOnSale.objects.all()
  serializer_class = TicketOnSaleSerializer
  # permission_classes = [IsCreatorOrReadOnly]

  def create(self, request):
    serializer = TicketOnSaleSerializer(data=request.data, partial=True)
    if not serializer.is_valid():
      return Response(serializer.errors, status=400)
    serializer.save()
    return Response(serializer.data)

  # def list(self, request):
  #   tickets = TicketOnSale.objects.all()
  #   return Response(TicketOnSaleSerializer(tickets, many=True).data)

  def destroy(self, request, pk=None):
    ticket = get_object_or_404(TicketOnSale, pk=pk)
    # self.check_object_permissions(request, ticket)
    ticket.delete()
    return Response({'message': 'Ticket successfully deleted'})

  def retrieve(self, request, pk=None):
    ticket = get_object_or_404(TicketOnSale, pk=pk)
    return Response(data=TicketOnSaleSerializer(ticket).data)

  def update(self, request, pk=None):
    ticket = get_object_or_404(TicketOnSale, id=pk)
    # self.check_object_permissions(request, ticket)
    serializer = TicketOnSaleSerializer(ticket, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(data=serializer.data)
