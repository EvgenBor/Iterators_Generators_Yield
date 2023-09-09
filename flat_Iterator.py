class FlatIterator:

    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists
        self.cursor = -1

    def __iter__(self):
        return self

    def __next__(self):
        new_list = sum(self.list_of_lists, [])
        if len(new_list) - 1 == self.cursor:
            raise StopIteration
        else:
            self.cursor += 1
        return new_list[self.cursor]


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item
    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

if __name__ == '__main__':
    test_1()