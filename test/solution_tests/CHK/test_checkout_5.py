from solutions.CHK import checkout_solution
from solutions.CHK import input_parser


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
        assert checkout_solution.checkout('E') == 40
        assert checkout_solution.checkout('F') == 10

    def test_multiple(self):
        assert checkout_solution.checkout('AB') == 80
        assert checkout_solution.checkout('ABCD') == 115
        assert checkout_solution.checkout('FF') == 20

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
        assert checkout_solution.checkout('AAAAA') == 200

    def test_multiple_promo_single(self):
        assert checkout_solution.checkout('AAAAAAAAAA') == 400

    def test_multiple_promo_single_mixed_quantities(self):
        assert checkout_solution.checkout('AAAAAAAA') == 330

    def test_multiple_mixed_promos(self):
        assert checkout_solution.checkout('AAABB') == 175

    def test_multiple_promo_overflow(self):
        assert checkout_solution.checkout('AAAABBB') == 255

    def test_free_product(self):
        assert checkout_solution.checkout('EEB') == 80

    def test_free_product_combo_without_benefit(self):
        assert checkout_solution.checkout('EE') == 80

    def test_free_product_2(self):
        assert checkout_solution.checkout('EEBB') == 110

    def test_free_product_same_sku(self):
        assert checkout_solution.checkout('FFF') == 20
        assert checkout_solution.checkout('FFFF') == 30
        assert checkout_solution.checkout('FFFFF') == 40
        assert checkout_solution.checkout('FFFFFF') == 40
        assert checkout_solution.checkout('FFFFFFF') == 50

    def test_free_product_same_sku_mixed(self):
        assert checkout_solution.checkout('FFFA') == 70
        assert checkout_solution.checkout('FFFFA') == 80
        assert checkout_solution.checkout('FFFFFA') == 90

    # In this case (CHK_R4), the logic has not changed, so we should be okay
    # just testing the automated input parsing.
    def test_input_parser(self):
        price_data, promo_data, free_item_data, group_promo_data \
            = input_parser.parse_input("./lib/solutions/CHK/test_input.txt")

        assert price_data == {
            'F': 10,
            'P': 50,
            'R': 50,
            'S': 20,
            'T': 20,
            'X': 17,
            'Y': 20,
            'Z': 21,
        }
        assert promo_data == {
            'P': {
                5: 200,
            }
        }
        assert free_item_data == {
            'F': {
                3: 'F',
            },
            'R': {
                3: 'Q',
            },
        }
        assert group_promo_data == {
            'ZSTYX': {
                3: 45,
            },
        }

    def test_group_discount(self):
        assert checkout_solution.checkout('SSS') == 45
        assert checkout_solution.checkout('SST') == 45
        assert checkout_solution.checkout('XYZ') == 45
        assert checkout_solution.checkout('XYZA') == 95

    def test_group_count_with_leftover_items(self):
        assert checkout_solution.checkout('SSSS') == 65
        assert checkout_solution.checkout('SSSSS') == 85
        assert checkout_solution.checkout('SSSSSSS') == 110

    def test_group_count_multiple(self):
        assert checkout_solution.checkout('SSSSSS') == 90
        assert checkout_solution.checkout('STXYZS') == 90

    def test_group_count_optimum(self):
        assert checkout_solution.checkout('STXY') == 62
        assert checkout_solution.checkout('STXYZ') == 82

