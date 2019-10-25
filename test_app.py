import unittest
from cal import app

class MyTestCase(unittest.TestCase):
    def test_index(self):
        with app.test_client() as a:
            get_index = a.get('/')
            self.assertEqual(get_index._status_code, 200)
            post_index_add = a.post('/', data={'A':'6', 'B':'5', 'operator': 'Add'})
            post_index_sub = a.post('/', data={'A':'6', 'B':'5', 'operator': 'Sub'})
            post_index_mul = a.post('/', data={'A':'6', 'B':'5', 'operator': 'Mul'})
            post_index_div = a.post('/', data={'A':'6', 'B':'5', 'operator': 'Div'})
            self.assertEqual(post_index_add._status_code, 302)
            self.assertEqual(post_index_sub._status_code, 302)
            self.assertEqual(post_index_mul._status_code, 302)
            self.assertEqual(post_index_div._status_code, 302)


if __name__ == '__main__':
    unittest.main()
