from django.test import TestCase
from .models import Category
# Create your tests here.

class TestCategory(TestCase):

    def setUp(self) -> None:
        self.category = Category.objects.create(name='курс')
        print('Я выполняюсь ПЕРЕД каждым тестом')

    def tearDown(self) -> None:
        print('Я выполняюсь ПОСЛЕ каждого теста')

    def test_str(self):
        category = Category.objects.get(name='курс')
        self.assertEqual(str(category), 'курс')
