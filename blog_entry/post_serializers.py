from django.forms import widgets
from rest_framework import serializers

class ModelSerializer(serializers.Serializer):
	pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
   	title = serializers.CharField(max_length=100)
   	body  = serializers.CharField()
   	guid  = serializers.CharField()

	def restore_object(self, attrs, instance=None):
		if instance:
            # Update existing instance
			instance.title = attrs.get('title', instance.title)
			instance.body  = attrs.get('body' , instance.body)
			instance.guid  = attrs.get('guid' , instance.guid)
			return instance
		return Snippet(**attrs)


