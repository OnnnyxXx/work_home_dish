from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FoodCategory
from .serializers import FoodListSerializer


class FoodCategoryListView(APIView):
    def get(self, reqeust):
        categories = FoodCategory.objects.filter(food__is_publish=True).distinct()
        categories = categories.prefetch_related('food')
        serializers = FoodListSerializer(categories, many=True)

        return Response(serializers.data, status=status.HTTP_200_OK)
