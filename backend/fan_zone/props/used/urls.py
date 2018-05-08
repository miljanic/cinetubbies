from django.urls import include
from django.urls import path

from cinetubbies.utils.routing import BaseManageView

from .views import MemberAPI
from .views import PublicAPI
from .views import RestrictedAPI

class UsedProps(BaseManageView):
  VIEWS_BY_METHOD = {
    'GET': PublicAPI.as_view({'get': 'list'}),
    'POST': MemberAPI.as_view({'post': 'create'}),
  }


class UsedProp(BaseManageView):
  VIEWS_BY_METHOD = {
    'DELETE': MemberAPI.as_view({'delete': 'destroy'}),
    'GET': PublicAPI.as_view({'get': 'retrieve'}),
    'PUT': MemberAPI.as_view({'put': 'update'}),
  }

count_used_props = PublicAPI.as_view({'get' : 'count'})

review_prop = RestrictedAPI.as_view({'put': 'review'})


urlpatterns = [
  path(
    route='',
    view=UsedProps.as_view(),
    name='used-props'
  ),
  path(
    route='count',
    view=count_used_props,
    name='count-used-props'
  ),
  path(
    route='<int:pk>',
    view=UsedProps.as_view(),
    name='used-prop'
  ),
  path(
    route='<int:pk>/review',
    view=review_prop,
    name='review-prop'
  ),
]
