from rest_framework.serializers import Serializer


class BaseService:
    def __init__(self, serializer: Serializer):
        self.serializer = serializer

    def get_field(self, field):
            return self.serializer.validated_data[str(field)]
