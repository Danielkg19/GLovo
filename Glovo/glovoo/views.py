
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets, generics, status, permissions
from .serializers import *
from .models import *
from .filters import CategoryFilter,ProductFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter




class UserProfileAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers


class UserProfileDetailAPIView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class =UserProfileSerializers




class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers



class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class CategoryCreateAPIView(generics.ListCreateAPIView):
    queryset = Category .objects.all()
    serializer_class = CategorySerializers



class CategoryEDITAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class StoreListAPIView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['store_name']




class StoreDetailAPIView(generics.RetrieveAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializers



class StoreCreateAPIView(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class =StoreSerializers



class StoreEDITAPIview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializers



class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['product_name']
    ordering_fields = ['price']


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers




class ProductCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers



class ProductEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class  ProductImageListAAPIView(generics.ListAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializers



class ComboProductImageProductListAPIView(generics.RetrieveAPIView):
    queryset = ComboProduct.objects.all()
    serializer_class = ComboProductSerializers


class ComboProductImageDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class CourierListViewSet(viewsets.ModelViewSet):
    queryset = Courier.objects.all()
    serializer_class =CourierSerializers


class CourierDetailViewSet(viewsets.ModelViewSet):
    queryset = Courier.objects.all()
    serializer_class =CourierSerializers


class CartListViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class =CartSerializers

class CartDetailViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class =CartSerializers

class CartItemListViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartItemSerializers

class CartItemDetailViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartItemSerializers


class ProductImageDetailAPIView(generics.RetrieveAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializers


class OrderListAPIView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers


class OrderDetailAPIView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers



class ReviewListAPIView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers


class ReviewDetailAPIView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers



class ComboProductListAPIView(generics.RetrieveAPIView):
    queryset = ComboProduct.objects.all()
    serializer_class = ComboProductSerializers


class ComboProductDetailAPIView(generics.RetrieveAPIView):
    queryset = ComboProduct.objects.all()
    serializer_class = ComboProductSerializers


class ComboProductCreateAPIView(generics.ListCreateAPIView):
    queryset = ComboProduct.objects.all()
    serializer_class = CategorySerializers



class ComboProductEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ComboProduct.objects.all()
    serializer_class = CategorySerializers
