from rest_framework import serializers
from network.models import Element, Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('email', 'country', 'city', 'street', 'building_number',)


class ElementSerializer(serializers.ModelSerializer):
    supplier = serializers.SlugRelatedField(required=False,
                                            queryset=Element.objects.all(),
                                            slug_field="name")
    contact = ContactSerializer(required=False)

    class Meta:
        model = Element
        fields = '__all__'

    def is_valid(self, *args):

        self._contact = self.initial_data.pop("contact", {})
        if "supplier" in self.initial_data:
            self.initial_data["level"] = level_check(self.initial_data)
        return super().is_valid(raise_exception=False)


def level_check(dict_):

    level = 0
    if dict_["supplier"] is None:
        return level

    supplier = Element.objects.get(name=dict_["supplier"])

    while level != 2:
        level += 1
        if supplier.supplier is None:
            return level
        supplier = supplier.supplier
        raise Exception('Incorrect links')
