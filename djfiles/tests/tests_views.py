from django.test import TestCase
from django.urls import reverse


class LoadFileTest(TestCase):
    def test_load_file(self):
        url = reverse('load_file')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Импорт данных')


class LoginTest(TestCase):
    def test_login(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Аутентификация')



# class LogoutTest(TestCase):
#     def test_logout(self):
#         url = reverse('logout')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'Выход')



# class EditProfileTest(TestCase):
#     def test_edit_profile(self):
#         url = reverse('edit_profile')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'Изменить персональные данные')


class MainPageTest(TestCase):
    def test_main_page(self):
        url = reverse('main_page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


#
# class PersonalInfTest(TestCase):
#     def test_personal_inf(self):
#         url = reverse('personal_inf')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'Персональная информация')



class RegisterTest(TestCase):
    def test_register(self):
        url = reverse('register')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Регистрация')


