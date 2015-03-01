from django.test import TestCase
from django.test.client import Client
from django.test.client import RequestFactory
from django.test import LiveServerTestCase

from selenium.webdriver.firefox.webdriver import WebDriver

from books.models import Book;
from books.views import ListBookView;

# Create your tests here.
class BookTest(TestCase):
    def test_str(self):
        b = Book(name = 'Concepts of Physics', author_name = 'H.C.Verma')
        self.assertEquals(str(b), 'Concepts of Physics by H.C.Verma')


class ListBookViewTest(TestCase):
    def test_book_in_context(self):
        client = Client()
        response = client.get('/books')
        self.assertEquals(
                list(response.context['object_list']), [])
        Book.objects.create(name = 'TestBook', author_name = 'TestAuthor')
        response = client.get('/books')
        self.assertEquals(len(list(response.context['object_list'])), 1)

    def test_book_in_context_request_factory(self):
        factory = RequestFactory()
        request = factory.get('/books')
        response = ListBookView.as_view()(request)
        self.assertEquals(list(response.context_data['object_list']), [])
        Book.objects.create(name = 'TestBook', author_name = 'TestAuthor')
        response = ListBookView.as_view()(request)
        self.assertEquals(len(list(response.context_data['object_list'])), 1)

class ListBookIntegrationTests(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(ListBookIntegrationTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(ListBookIntegrationTests, cls).tearDownClass()
    
    def test_book_listed(self):
        Book.objects.create(name = 'TestBook', author_name = 'TestAuthor')
        self.selenium.get('%s%s' % (self.live_server_url, '/books'))
        self.assertEquals(self.selenium.find_elements_by_css_selector('.book')[0].text,
                'TestBook by TestAuthor')

    def test_create_book_link_from_book_list(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/books'))
        self.selenium.find_element_by_link_text('Create Book').click()
        self.assertEquals('%s%s' % (self.live_server_url, '/books/new'), self.selenium.current_url)

class NewBookIntegrationTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(NewBookIntegrationTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(NewBookIntegrationTest, cls).tearDownClass()

    def test_list_link_from_new_book(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/books/new'))
        self.selenium.find_element_by_link_text('Book List').click()
        self.assertEquals('%s%s' % (self.live_server_url, '/books'), self.selenium.current_url)

    def test_book_new(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/books/new'))
        self.selenium.find_element_by_link_text('Book List').click()
        self.assertEquals('%s%s' % (self.live_server_url, '/books'), self.selenium.current_url)

