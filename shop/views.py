from rest_framework import viewsets
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer
from rest_framework.response import Response
from rest_framework import status

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()  # This will create the product
            response_data = {
                'status': 201,
                'success': True,
                'message': "Product created successfully",
                'data': serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        except Exception as e:
            response_data = {
                'status': 400,
                'success': False,
                'message': f"An error occurred while creating the product: {str(e)}",
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        try:
            products = self.get_queryset()
            serializer = self.get_serializer(products, many=True)
            response_data = {
                'status': 200,
                'success': True,
                'message': "List of products",
                'data': serializer.data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            response_data = {
                'status': 500,
                'success': False,
                'message': f"An error occurred: {str(e)}",
                'data': []
            }
            return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            response_data = {
                'status': 200,
                'success': True,
                'message': "Get product by ID",
                'data': serializer.data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            response_data = {
                'status': 404,
                'success': False,
                'message': f"Product not found: {str(e)}",
                'data': []
            }
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            response_data = {
                'status': 200,
                'success': True,
                'message': "Product deleted successfully",
                'data': []
            }
            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            response_data = {
                'status': 500,
                'success': False,
                'message': f"An error occurred while deleting the product: {str(e)}",
                'data': []
            }
            return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            response_data = {
                'status': 200,
                'success': True,
                'message': "Product updated successfully",
                'data': []
            }
            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            response_data = {
                'status': 400,
                'success': False,
                'message': f"An error occurred while updating the product: {str(e)}",
                'data': []
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            response_data = {
                'status': 201,
                'success': True,
                'message': "Order created successfully",
                'data': []
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        except Exception as e:
            response_data = {
                'status': 400,
                'success': False,
                'message': f"An error occurred while creating the order: {str(e)}",
                'data': []
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    # def update(self, request, *args, **kwargs):
    #     try:
    #         instance = self.get_object()
    #         serializer = self.get_serializer(instance, data=request.data)
    #         serializer.is_valid(raise_exception=True)
    #         self.perform_update(serializer)
    #         response_data = {
    #             'status': 200,
    #             'success': True,
    #             'message': "Order updated successfully",
    #             'data': []
    #         }
    #         return Response(response_data, status=status.HTTP_200_OK)
    #     except Exception as e:
    #         response_data = {
    #             'status': 400,
    #             'success': False,
    #             'message': f"An error occurred while updating the order: {str(e)}",
    #             'data': []
    #         }
    #         return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            response_data = {
                'status': 200,
                'success': True,
                'message': "Order canceled successfully",
            }
            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            response_data = {
                'status': 400,
                'success': False,
                'message': f"An error occurred while canceling the order: {str(e)}",
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        try:
            orders = self.get_queryset()
            serializer = self.get_serializer(orders, many=True)
            response_data = {
                'status': 200,
                'success': True,
                'message': "List of Orders",
                'data': serializer.data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            response_data = {
                'status': 400,
                'success': False,
                'message': f"An error occurred while listing the order: {str(e)}",
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
