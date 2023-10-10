from django.test import TestCase
from .models import MenuItens


class MenuItemTestCase(TestCase):
    def test_get_item(self):
        item = MenuItens.objects.create(title="IceCream", price=80)
        self.assertEqual(str(item), "IceCream : 80")
