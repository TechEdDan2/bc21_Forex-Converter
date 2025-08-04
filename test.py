from unittest import TestCase
from app import app 
from calc import convert_currency

# Bundle the test cases for the currency converter application
# This will include tests for the main routes and the currency conversion logic
class CurrencyConverterTestCase(TestCase):
    def setUp(self):
        """Set up the test client"""
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        """Test the index route"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Currency Converter', response.data)

    def test_convert_currency_view(self):
        response = self.app.get('/convert')
        self.assertEqual(response.status_code, 200)

    def test_convert_currency_form_submission(self):
        """ Test form submission for currency conversion """
        form_data = {
            'amount': '100.00',
            'from_currency': 'DKK',
            'to_currency': 'DKK'
        }
        response = self.app.post('/convert', data=form_data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(convert_currency(form_data['amount'], form_data['from_currency'], form_data['to_currency']), 100.00)
        