from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.management import call_command

from .models import Hero, Investigator
from django.contrib.auth.models import User

test_hero_data = dict(hero_name="test",
                    real_name="test",
                    about_1="test",
                    about_2="test",
                    about_source="test",
                    quote="test",
                    primary_rgb="test",
                    strengths="test",
                    weaknesses="test",
                    image="test")

def create_test_investigator(username=""):
    test_user = User.objects.create(username=username)
    return Investigator.objects.create(user=test_user)

class HeroAppTest(SimpleTestCase):
    def test_django(self):
        self.assertTrue(True)

class DataTest(TestCase):

    def test_investigator_model(self):

        test_investigator1 = create_test_investigator("user1")
        test_investigator2 = create_test_investigator("user2")
        self.assertEqual(len(Investigator.objects.all()), 2)
        test_investigator1.bio = "aha"
        test_investigator2.bio = "haha"
        self.assertEqual(test_investigator1.bio, "aha")
        self.assertEqual(test_investigator2.bio, "haha")
        test_investigator2.delete()
        self.assertEqual(len(Investigator.objects.all()), 1)

    def test_hero_model(self):

        test_investigator = create_test_investigator()
        self.assertEqual(len(Hero.objects.all()), 0)
        hi = Hero.objects.create(investigator=test_investigator, hero_name='Title 1')
        Hero.objects.create(investigator=test_investigator, hero_name='Title 2')
        self.assertEqual(len(Hero.objects.all()), 2)
        a = Hero.objects.get(pk=2)
        self.assertEqual(a.hero_name, 'Title 2')
        a.hero_name = "New Title"
        a.save()
        self.assertEqual(a.hero_name, 'New Title')
        a.delete()
        self.assertEqual(len(Hero.objects.all()), 1)
    
    def test_json(self):

        test_investigator = create_test_investigator()
        Hero.objects.create(investigator=test_investigator, hero_name='Title 1')
        call_command('save_data_json')
        Hero.objects.create(investigator=test_investigator, hero_name='Title 2')
        call_command('load_data_json')
        self.assertEqual(len(Hero.objects.all()), 1)

    def test_csv(self):

        test_investigator = create_test_investigator()
        Hero.objects.create(investigator=test_investigator, hero_name='Title 1')
        call_command('save_data_csv')
        Hero.objects.create(investigator=test_investigator, hero_name='Title 2')
        call_command('load_data_csv')
        self.assertEqual(len(Hero.objects.all()), 1)
        

class ViewTest(TestCase):

    def login(self):
        user = get_user_model().objects.create_user(username="TESTUSER", password="TESTUSER")
        self.assertEqual(self.client.login(username="TESTUSER", password="TESTUSER"), True)
        return user

class HeroViewTest(ViewTest):

    def test_hero_list_view(self):
        response = self.client.get(reverse("hero_list"))
        self.assertEqual(response.status_code, 200)
    
    def test_hero_detail_view(self):
        user = self.login()
        investigator = Investigator.objects.create(user=user)
        Hero.objects.create(investigator=investigator, hero_name='title')
        response = self.client.get(reverse("hero_detail", args='1'))
        self.assertEqual(response.status_code, 200)

    def test_hero_add_view(self):
        self.login()
        self.client.post(reverse("hero_add"), test_hero_data)
        self.assertEqual(len(Hero.objects.all()), 1)
    
    def test_hero_edit_view(self):
        user = self.login()
        investigator = Investigator.objects.create(user=user)
        Hero.objects.create(investigator=investigator, hero_name='title')
        self.client.post(reverse("hero_edit", args='1'), test_hero_data)
        self.assertEqual(Hero.objects.all()[0].hero_name, "test")

    def test_hero_delete_view(self):
        user = self.login()
        investigator = Investigator.objects.create(user=user)
        Hero.objects.create(investigator=investigator, hero_name='title')
        self.client.post(reverse("hero_delete", args='1'))
        self.assertEqual(len(Hero.objects.all()), 0)

