from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import URL
from .serializers import URLSerializer

import random
import string


def generate_short_url():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(6))


class URLCreateView(APIView):
    def post(self, request):
        serializer = URLSerializer(data=request.data)
        if serializer.is_valid():
            url = serializer.save(short_url=generate_short_url())
            short_url = request.build_absolute_uri('/') + url.short_url
            return Response({'short_url': short_url}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class URLRedirectView(APIView):
    def get(self, request, short_url):
        url = URL.objects.filter(short_url=short_url).first()
        if url:
            if 'application/json' in request.META.get('HTTP_ACCEPT', ''):
                data = {
                    'original_url': url.original_url,
                    'short_url': url.short_url
                }
                return Response(data)
            else:
                context = {
                    'original_url': url.original_url,
                    'short_url': url.short_url
                }
                return render(request, 'redirect.html', context)
        return redirect('/')
