"""View module for handling requests about OrderProduct"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bangazonapi.models import OrderProduct, Orders, Product

class OrderproductView(ViewSet):
    """Bangazon OrderProduct View"""
    
    def retrieve(self, request, pk):
        """Handle GET Request for Single OrderProduct
        Returns:
            Response -- JSON Serialized OrderProduct
        """
        Orderproduct = OrderProduct.objects.get(pk=pk)
        serializer = OrderProductSerializer(Orderproduct)
        return Response(serializer.data)
      
    def list(self, request):

        Orderproduct = OrderProduct.objects.all()
        serializer = OrderProductSerializer(Orderproduct, many=True)
        return Response(serializer.data)
      
    def create(self, request):
        """Handle POST operations

        Returns
        Response -- JSON serialized OrderProduct instance
        """

        order_id = Orders.objects.get(pk=request.data["order_id"])
        product_id = Product.objects.get(pk=request.data["product_id"])
        
        orderproduct = OrderProduct.objects.create(
            product_id=product_id,
            order_id=order_id,
        )
        serializer = OrderProductSerializer(orderproduct)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """Handle PUT requests for a orderproduct

        Returns:
        Response -- Empty body with 204 status code
        """

        # orderproduct = OrderProduct.objects.get(pk=pk)
        # orderproduct.name = request.data["name"]
        # orderproduct.description = request.data["description"]
        # orderproduct.save()
        # return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        """Delete OrderProduct
        """
        orderproduct = OrderProduct.objects.get(pk=pk)
        orderproduct.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)   

class OrderProductSerializer(serializers.ModelSerializer):
    """JSON Serializer For OrderProducts"""
    class Meta:
        model = OrderProduct
        fields = ('id', 'order_id', 'product_id')
        depth = 2
