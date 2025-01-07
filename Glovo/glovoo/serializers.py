from .models import *
from rest_framework import serializers




class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields ='__all__'


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields ='__all__'


class CategoryDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields ='__all__'


class StoreSerializers(serializers.ModelSerializer):
    class Meta:
        model =Store
        fields ='__all__'


class StoreDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model =Store
        fields ='__all__'



class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'



class ProductImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields ='__all__'


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields ='__all__'


class CourierSerializers(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields ='__all__'



class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields ='__all__'



class ComboProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = ComboProduct
        fields ='__all__'



class ComboImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = ComboImage
        fields ='__all__'


class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields ='__all__'

class CartItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields ='__all__'
