from django.test import TestCase

from authors.models import Author

# Create your tests here.
class AuthorTest(TestCase):
    def test_str(self):
        author = Author(first_name = 'H.C.', last_name = 'Verma')
        self.assertEquals('H.C. Verma', str(author))
