from django.core.paginator import Paginator

from rest_framework.decorators import api_view
from rest_framework.response import Response

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rankings.serializers import TeamMatchSerializer
from rankings.models import TeamMatch as TeamMatchModel


@swagger_auto_schema(
    method='GET', responses={200: openapi.Response("", TeamMatchSerializer)},
    operation_description="Statistics for a specific (Team, Match) pair",
)
@api_view(['GET'])
def TeamMatch(request, num, match):
    teamMatch = TeamMatchModel.objects.filter(team=num).filter(match=match).all()  # noqa 502
    serializer = TeamMatchSerializer(teamMatch, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='GET', auto_schema=None)
@api_view(['GET'])
def _TeamMatches(request, num=None, year=None, event=None, match=None, page=1):
    teamMatches = TeamMatchModel.objects
    if num:
        teamMatches = teamMatches.filter(team=num)
    if year:
        teamMatches = teamMatches.filter(year=year)
    if event:
        teamMatches = teamMatches.filter(event=event)
    if match:
        teamMatches = teamMatches.filter(match=match)
    teamMatches = Paginator(teamMatches.all().order_by("time"), 5000).page(page)  # noqa 502
    serializer = TeamMatchSerializer(teamMatches, many=True)
    return Response(serializer.data)


@swagger_auto_schema(
    method='GET', responses={200: openapi.Response("", TeamMatchSerializer)},
    operation_description="Statistics for all (Team, Match) pairs",
)
@api_view(['GET'])
def TeamMatches(request):
    return _TeamMatches(request._request)


@swagger_auto_schema(
    method='GET', responses={200: openapi.Response("", TeamMatchSerializer)},
    operation_description="Statistics for (Team, Match) pairs with specified team",  # noqa 502
)
@api_view(['GET'])
def TeamMatchesTeam(request, num):
    return _TeamMatches(request._request, num=num)


@swagger_auto_schema(
    method='GET', responses={200: openapi.Response("", TeamMatchSerializer)},
    operation_description="Statistics for (Team, Match) pairs with specified year",  # noqa 502
)
@api_view(['GET'])
def TeamMatchesYear(request, year):
    return _TeamMatches(request._request, year=year)


@swagger_auto_schema(
    method='GET', responses={200: openapi.Response("", TeamMatchSerializer)},
    operation_description="Statistics for (Team, Match) pairs with specified event",  # noqa 502
)
@api_view(['GET'])
def TeamMatchesEvent(request, event):
    return _TeamMatches(request._request, event=event)


@swagger_auto_schema(
    method='GET', responses={200: openapi.Response("", TeamMatchSerializer)},
    operation_description="Statistics for (Team, Match) pairs with specified match",  # noqa 502
)
@api_view(['GET'])
def TeamMatchesMatch(request, match):
    return _TeamMatches(request._request, match=match)


@swagger_auto_schema(
    method='GET', responses={200: openapi.Response("", TeamMatchSerializer)},
    operation_description="Statistics for (Team, Match) pairs with specified team, year",  # noqa 502
)
@api_view(['GET'])
def TeamMatchesTeamYear(request, num, year):
    return _TeamMatches(request._request, num=num, year=year)


@swagger_auto_schema(
    method='GET', responses={200: openapi.Response("", TeamMatchSerializer)},
    operation_description="Statistics for (Team, Match) pairs with specified team, event",  # noqa 502
)
@api_view(['GET'])
def TeamMatchesTeamEvent(request, num, event):
    return _TeamMatches(request._request, num=num, event=event)
