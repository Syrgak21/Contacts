from django.test import TestCase
from django.template.defaultfilters import slugify
# Create your tests here.

from .models import Contact

class ContactModelTest(TestCase):

    @classmethod
    def setUpTestData(self):
        contact = Contact.objects.create(name='Syrgak', number='123456789')

    def test_first_name_label(self):
        contact=Contact.objects.get(id=1)
        field_label = contact._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_index_loads_properly(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_get_absolute_url(self):
        contact=Contact.objects.get(id=1)
        self.assertEquals(contact.get_absolute_url(), '/detail_contact/1')
