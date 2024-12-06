from typing import Callable

from rest_framework import generics
from rest_framework import viewsets
from rest_framework.exceptions import NotFound
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Person
from .serializers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    """
    Class for managing person's data
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class AncestorsView(generics.GenericAPIView):
    """
    Class for getting person's ancestors
    """
    serializer_class = PersonSerializer

    def get(self, request: Request, person_id: str) -> Response:
        depth = request.query_params.get('depth', None)
        try:
            person = Person.objects.get(id=person_id)
        except Person.DoesNotExist:
            raise NotFound("Person not found")

        return Response(self.get_ancestors(person, depth))

    def get_ancestors(self, person: Person, depth: str | None, curr_depth: int = 0) -> dict | Callable:
        """Recursively gets person's data about the ancestors with a specified depth.

        Args:
            person: Instance of a "Person" class
            depth: Depth of nested levels to get. None for getting full depth
            curr_depth: Current depth of a nested dict to compare with initial depth

        Returns:
            Nested dict of ancestors or this function
        """
        if person and (depth is None or curr_depth <= int(depth)):
            # Includes this person data to result for all nested levels except the first one
            fields = 'id', 'first_name', 'last_name'
            person_data = {field: getattr(person, field) for field in fields} if curr_depth else {}

            return {
                **person_data,
                'mother': self.get_ancestors(person.mother, depth, curr_depth + 1),
                'father': self.get_ancestors(person.father, depth, curr_depth + 1)
            }
