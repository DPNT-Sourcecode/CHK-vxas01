from solutions.CHK import checkout_solution


class TestCheckout():
    def test_empty(self):
        assert checkout_solution.checkout('') == 0

    def test_illegal(self):
        assert checkout_solution.checkout('Illegal') == -1
        assert checkout_solution.checkout('A,B,C,D') == -1
        assert checkout_solution.checkout('1234') == -1

    def test_single(self):
        assert checkout_solution.checkout('A') == 50
        assert checkout_solution.checkout('B') == 30
        assert checkout_solution.checkout('C') == 20
        assert checkout_solution.checkout('D') == 15

    def test_multiple(self):
        assert checkout_solution.checkout('AB') == 80
        assert checkout_solution.checkout('ABCD') == 115


