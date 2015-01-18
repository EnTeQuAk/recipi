from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin,
    UpdateModelMixin, DestroyModelMixin)
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer


from recipi.api.auth import AnonymousAuthentication
from recipi.api.parsers import JSONParser


class Endpoint(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin,
               CreateModelMixin, GenericAPIView):
    authentication_classes = (AnonymousAuthentication,)

    # TODO: Move to recipi.api.permissions
    permission_classes = (IsAuthenticated,)

    parser_classes = (JSONParser,)
    renderer_classes = (JSONRenderer,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class ListEndpoint(ListModelMixin, Endpoint):

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
