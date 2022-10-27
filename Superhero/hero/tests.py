from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from .models import Hero, Author
from django.contrib.auth.models import User


def create_test_author(username=""):
    test_user = User.objects.create(username=username)
    return Author.objects.create(user=test_user)


class HeroAppTest(SimpleTestCase):

    def test_django(self):
        self.assertTrue(True)


class DataTest(TestCase):

    def test_author_model(self):
        test_author1 = create_test_author("user1")
        test_author2 = create_test_author("user2")
        self.assertEqual(len(Author.objects.all()), 2)
        test_author1.bio = "aha"
        test_author2.bio = "haha"
        self.assertEqual(test_author1.bio, "aha")
        self.assertEqual(test_author2.bio, "haha")
        test_author2.delete()
        self.assertEqual(len(Author.objects.all()), 1)

    def test_hero_model(self):

        test_author = create_test_author()

        self.assertEqual(len(Hero.objects.all()), 0)
        hi = Hero.objects.create(author=test_author, hero_name='Title 1')
        Hero.objects.create(author=test_author, hero_name='Title 2')
        self.assertEqual(len(Hero.objects.all()), 2)

        a = Hero.objects.get(pk=2)
        self.assertEqual(a.hero_name, 'Title 2')

        a.hero_name = "New Title"
        a.save()
        self.assertEqual(a.hero_name, 'New Title')

        a.delete()
        self.assertEqual(len(Hero.objects.all()), 1)


class HeroViewTest(TestCase):
    def test_hero_list_view(self):
        self.assertEqual(reverse("hero_list"), "/hero/")

    def test_hero_add_view(self):

        test_author = create_test_author()

        a = dict(author=test_author, hero_name='T 1')
        response = self.client.post(reverse("hero_add"), a)
        print(response)
        self.assertEqual(response.status_code, 302)
