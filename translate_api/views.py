from googletrans import Translator
import googletrans
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import ParentCategory
from .serializer import GetParentCategorySerializer
from rest_framework.response import Response
import json

# Create your views here.

class addParentCategoryView(CreateAPIView):
    serializer_class = GetParentCategorySerializer

    def post(self, request, *args, **kwargs):
        category = self.get_serializer(data = request.data)
        if category.is_valid(raise_exception=True):
            category.save()
        return Response(category.data)

class getParentCategoryView(ListAPIView):
    serializer_class = GetParentCategorySerializer

    def get_queryset(self):
        """
        function for returning all Parent Resources Category.
        """
        return ParentCategory.objects.all()

    def translator(self, dict1, arg_list):
        translator = Translator()
        data_dict = dict1

        json_data = json.dumps(data_dict)
        parsed_data = json.loads(json_data)
        for i in range(len(parsed_data)):

            for key, value in parsed_data[i].items():

                if key in arg_list:
                    
                    parsed_data[i][key] = translator.translate(value, src = 'en', dest = 'es').text
                         
        return (parsed_data)

            
            
        
    def get(self, request, *args, **kwargs):
        """
        Get Method for getting Parent Resources Category list.
        """

        resource_model = self.filter_queryset(self.get_queryset())
        
        resource_serializer = self.get_serializer(resource_model, many=True)
     
        arg_list = ['title']
        self.translator(resource_serializer.data, arg_list)
        resource_serializer = self.get_serializer(self.translator(resource_serializer.data, arg_list), many=True)

        return Response(resource_serializer.data)