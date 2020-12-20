from django.test import TestCase
from django.urls import reverse
from app_users.models import News


NUMBER_OF_ITEMS = 20
WORD_OF_ITEMS = ['Квас', 'Жук', 'Камень', 'Круглый остров', 'Весёлый дрон', 'Дерево', 'Буксировщик', ' Сало', 'Ар', 'Хор']


class NewsListTest(TestCase):

    # def test_news_list(self):
    #     url = reverse('news_list')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)

    @classmethod
    def setUpTestData(cls):
        for word in WORD_OF_ITEMS:
            News.objects.create(
                user='admin',
                title=word,
                description=f'The time of sunset is defined in astronomy as the moment when the upper limb of  {word}',
                status=True
            )

    def test_items_in_location(self):
        url = reverse('news_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_users/news_list.html')

    def test_items_in_template(self):
        url = reverse('news_list')
        response = self.client.get(url)
        self.assertTrue(len(response.context['object_list']) == len(WORD_OF_ITEMS))
