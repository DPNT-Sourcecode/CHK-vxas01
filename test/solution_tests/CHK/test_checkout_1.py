from solutions.CHK import checkout_solution


class TestCheckout():
    def test_empty(self):
        assert checkout_solution.checkout('') == 0

