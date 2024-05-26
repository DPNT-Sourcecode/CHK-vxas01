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

    def test_incomplete_promo(self):
        assert checkout_solution.checkout('AA') == 100

    def test_complete_promo(self):
        assert checkout_solution.checkout('AAA') == 130

    def test_promo_overflow(self):
        assert checkout_solution.checkout('AAAA') == 180

    def test_promo_with_mixed(self):
        assert checkout_solution.checkout('BAB') == 95

    def test_promo_overflow_with_mixed(self):
        assert checkout_solution.checkout('AABAA') == 210

    def test_multiple_better_promo(self):
        assert checkout_solution.checkout('AAAAAA') == 200

    def test_multiple_mixed_promos(self):
        assert checkout_solution.checkout('AAABB') == 175

    def test_multiple_promo_overflow(self):
        assert checkout_solution.checkout('AAAABBB') == 255
