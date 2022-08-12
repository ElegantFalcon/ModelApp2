from rest_framework import serializers
from appl.models import ProductDetails

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetails  
        fields = ('id' , 'serial_no' , 'product_name' , 'model_name', 'seller_name' , 'stock_num' , 'ratings' , 'price')
