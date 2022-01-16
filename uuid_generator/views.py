from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UuidSerializer
from .models import UUID_table

# Create your views here.
@api_view(["GET", "POST", "PUT", "PATCH"])
def uuid_view_set(request):
    serializer_class = UuidSerializer
    UUID_table.objects.create()
    queryset = UUID_table.objects.all()
    serializer = serializer_class(queryset, many=True)

    # convert list of ordered dictionaries to key value pairs

    output = {
        item["key"].replace("T", " ").split("+", 1)[0]: item["value"]
        for item in serializer.data
    }

    return Response(output)
