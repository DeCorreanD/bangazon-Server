"""View module for handling requests about Product"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bangazonapi.models import Product, User

class ProductView(ViewSet):
    """Bangazon Product View"""
    
    def retrieve(self, request, pk):
        """Handle GET Request for Single Product
        Returns:
            Response -- JSON Serialized Product
        """
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
      
    def list(self, request):

        product = Product.objects.all()
        seller_id = request.query_params.get('sellerId', None)
        if seller_id is not None:
            product = product.filter(seller_id=seller_id)
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
      
    def create(self, request):
        """Handle POST operations

        Returns
        Response -- JSON serialized Product instance
        """

        seller_id = User.objects.get(pk=request.data["sellerId"])
        
        product = Product.objects.create(
            name=request.data["name"],
            description=request.data["description"],
            quantity=request.data["quantity"],
            price=request.data["price"],
            image=request.data["image"],
            seller_id=seller_id,
        )
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """Handle PUT requests for a product

        Returns:
        Response -- Empty body with 204 status code
        """

        product = Product.objects.get(pk=pk)
        product.name = request.data["name"]
        product.description = request.data["description"]
        product.image = request.data["image"]
        product.price = request.data["price"]
        product.quantity = request.data["quantity"]
        product.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        """Delete Product
        """
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)  

class ProductSerializer(serializers.ModelSerializer):
    """JSON Serializer For Products"""
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'quantity', 'price', 'image', 'seller_id')
        depth = 1
