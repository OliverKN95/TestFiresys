import requests
from django.shortcuts import render
from django.db import models
from django.utils.translation import ugettext_lazy as _
from rest_framework import viewsets, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from datetime import datetime
from .models import person, test
from .serializers import testSerializer, personSerializer, itunesSerializer
from .filters import PersonFilter
from django.db.models import Q
import urllib.request
import json




# Create your views here.


class testViewset(viewsets.ModelViewSet):
    queryset = test.objects.all()
    serializer_class = testSerializer


class personViewset(viewsets.ModelViewSet):
    queryset = person.objects.all()
    serializer_class = personSerializer
    filterset_class = PersonFilter

    def get_queryset(self):
        queryset = self.queryset

        query_search = self.request.query_params.get('search', None)

        if query_search is not None :
            queryset = queryset.filter(
                Q(first_name__icontains=query_search) |
                Q(last_name__icontains=query_search)
            )

        return queryset


class itunesViewset(GenericAPIView):
    """
    API para traer info publica del Cliente.
    """
    queryset = person.objects.all()
    serializer_class = itunesSerializer
    authentication_classes = []
    permission_classes = []

    def post(self, request):

        quantity = request.data.get('quantity', '')

        if quantity != '':

            json_data = None

            try:
                response = requests.get(f"https://rss.itunes.apple.com/api/v1/us/apple-music/new-releases/all/{quantity}/explicit.json") #response = urllib.request.urlopen(f"https://rss.itunes.apple.com/api/v1/us/apple-music/new-releases/all/{quantity}/explicit.json")
                json_data = json.loads(response.text)
                json_data = json_data['feed']['results']
            except Exception as e:
                response = None

            if response:
                contry_data = json.loads(response.text)['feed']['country']
                release_data = []
                genres_data = []
                type_data = []
                update_song_date = None
                update_song_data = None

                for d in json_data:

                    if not d['releaseDate'] in release_data:
                        release_data.append(d['releaseDate'])

                    for c in d['genres']:

                        if not c in genres_data:
                            genres_data.append(c)

                    if not d['kind'] in type_data:
                        type_data.append(d['kind'])

                    if not update_song_data:
                        update_song_date = datetime.strptime(d['releaseDate'], "%Y-%m-%d") 
                        update_song_data = d

                    if datetime.strptime(d['releaseDate'], "%Y-%m-%d") > update_song_date:
                        update_song_date = datetime.strptime(d['releaseDate'], "%Y-%m-%d") 
                        update_song_data = d



                data = {
                    "Pais": contry_data,
                    "Fecha(s) de lanzamiento":  { 
                        "data": release_data,
                        "total": len(release_data)
                        },
                    "Género(s)": { 
                        "data": genres_data,
                        "total": len(genres_data)
                        },
                    "Tipo(s)":  { 
                        "data": type_data,
                        "total": len(type_data)
                        },
                    "Ultima canción que se actualizo": update_song_data,
                    "Número de canciones analizadas": quantity

                }
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response(_('Hubo un error al obtener datos de itunes.'), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            # if client:
            #     json_response = {
            #         'id': client.id,
            #         'name': client.name,
            #         'description': client.description,
            #         'logo': settings['URL_SERVER']+client.image.url,
            #         'terms': terms,
            #         'terms_origin': terms_origin,
            #     }
            #     return Response(data=json_response, status=status.HTTP_200_OK)
           
        else:
            return Response(data={'detail': _("Se esperaba parámetro 'quantity'.")}, status=status.HTTP_400_BAD_REQUEST)
