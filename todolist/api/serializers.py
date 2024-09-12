from rest_framework import serializers
from api.models import TodoList

class TodoSerializers(serializers.HyperlinkedModelSerializer):
    td_id=serializers.ReadOnlyField()
    class Meta:
        model=TodoList
        fields='__all__'