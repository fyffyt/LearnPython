
TEST_DEVICE = ''
def test_a():
    assert 'a' == 'a'


class TestTwo:
    @staticmethod
    def displayTestDevice():
        print(TEST_DEVICE)

    def test_two(self):
        assert 'b' == 'b'


