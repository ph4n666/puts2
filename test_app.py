 def test_sub(self):
        with app.test_client() as a:
            get_sub = a.get('/sub', query_string={'A':'6', 'B':'5'})
            self.assertEqual(get_sub._status_code, 200)
            result_string = get_sub.get_data(as_text=True)
            result = eval(result_string.split('result: ')[1])
            self.assertEqual(result, 1)
