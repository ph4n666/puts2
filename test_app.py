   def test_div(self):
        with app.test_client() as a:
            get_div = a.get('/div', query_string={'A':'6', 'B':'5'})
            self.assertEqual(get_div._status_code, 200)
            result_string = get_div.get_data(as_text=True)
            result = eval(result_string.split('result: ')[1])
            self.assertEqual(result, 6/5)

