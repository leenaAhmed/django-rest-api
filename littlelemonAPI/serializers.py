from decimal import Decimal
from rest_framework import serializers
from .models import MenuItem,Category



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
         model = Category
         fields = ['id','slug', 'title']


## 
 # another way to display a category field as a hyperlink
 #serializers.HyperlinkedModelSerializer class instead of the serializers.ModelSerializer class.
##
class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_after_stock = serializers.SerializerMethodField(method_name='calculate_tax')
    # category = serializers.StringRelatedField()
    # category = CategorySerializer(read_only=True)
    category = serializers.HyperlinkedRelatedField(
                 queryset = Category.objects.all(),
                 view_name='category-detail')
    category_id = serializers.IntegerField(write_only=True)
    extra_kwargs = {
                'price': {'min_value': 2},
                'inventory': {'min_value': 0}
            }
    class Meta:
        model = MenuItem
        fields = ['id' , 'title', 'price' , 'stock' , 'price_after_stock', 'category' ,'category_id']
        # depth = 1
    
    def calculate_tax(self,product:MenuItem):
        return product.price * Decimal(1.1)