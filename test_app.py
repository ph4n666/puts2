def test_mul(self):
        with app.test_client() as a:
            get_mul = a.get('/mul', query_string={'A':'6', 'B':'5'})
            self.assertEqual(get_mul._status_code, 200)
            result_string = get_mul.get_data(as_text=True)
            result = eval(result_string.split('result: ')[1])
            self.assertEqual(result, 30)

