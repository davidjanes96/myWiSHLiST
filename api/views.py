from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import WishlistSerializer
from wishlists.models import Wishlist

@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET':'/api/wishists'},
        {'GET':'/api/wishists/id'},
        
        {'POST':'/api/account/token'},
        {'POST':'/api/account/token/refresh'},
    ]

    return Response(routes)


@api_view(['GET'])
def getWishlists(request):
    wishlists = Wishlist.objects.all()
    serializer = WishlistSerializer(wishlists, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getWishlist(request, pk):
    wishlist = Wishlist.objects.get(id=pk)
    serializer = WishlistSerializer(wishlist, many=False)
    return Response(serializer.data)