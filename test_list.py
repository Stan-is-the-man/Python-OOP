class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


from unittest import TestCase, main


class IntegerListTest(TestCase):

    def test_the_constructor_without_data(self):
        int_list = IntegerList()

        self.assertEqual([], int_list.get_data())
        # self.assertEqual([], int_list._IntegerList__data)

    def test_the_constructor_with_wrong_data(self):
        int_list = IntegerList("Seat Tarraco 2020", 1.345, 5, -3, 100, 0)

        self.assertEqual([5, -3, 100, 0], int_list.get_data())
        # self.assertEqual([5, -3, 100, 0], int_list._IntegerList__data)

    def test_the_constructor_with_ok_data(self):
        int_list = IntegerList(5, -3)

        self.assertEqual([5, -3], int_list.get_data())
        # self.assertEqual([5, -3], int_list._IntegerList__data)

    def test_get_data(self):
        int_list = IntegerList(100)
        self.assertEqual([100], int_list.get_data())

    def test_add_if_incorrect_data_raises(self):
        int_list = IntegerList(100)
        with self.assertRaises(ValueError) as ex:
            int_list.add(3.55)
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_add_if_value_itself(self):
        int_list = IntegerList(100)
        int_list.add(123)
        self.assertEqual([100, 123], int_list.get_data())

    def test_remove_index_if_index_is_out_of_range_raise(self):
        int_list = IntegerList(100)
        # greater index
        with self.assertRaises(IndexError) as error:
            int_list.remove_index(3)
        self.assertEqual("Index is out of range", str(error.exception))

        # equal len index
        with self.assertRaises(IndexError) as error:
            int_list.remove_index(1)
        self.assertEqual("Index is out of range", str(error.exception))

    def test_remove_index_itself(self):
        int_list = IntegerList(100)
        int_list.remove_index(0)
        self.assertEqual([], int_list.get_data())

    def test_remove_returns_the_removed_element(self):
        int_list = IntegerList(125)
        result = int_list.remove_index(0)
        self.assertEqual(125, result)

    def test_get_index_raise_error(self):
        int_list = IntegerList(125)
        # greater index
        with self.assertRaises(IndexError) as ex:
            int_list.get(3)
        self.assertEqual("Index is out of range", str(ex.exception))
        # equal of length index
        with self.assertRaises(IndexError) as ex:
            int_list.get(1)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_index_itself(self):
        int_list = IntegerList(125)
        result = int_list.get(0)
        self.assertEqual(125, result)

    def test_insert_index_raises_error(self):
        int_list = IntegerList(5, 50)
        with self.assertRaises(IndexError) as ex:
            int_list.insert(5, 333)
        self.assertEqual("Index is out of range", str(ex.exception))

        with self.assertRaises(IndexError) as ex:
            int_list.insert(2, 333)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_not_an_integer(self):
        int_list = IntegerList(5, 50)
        with self.assertRaises(ValueError) as ex:
            int_list.insert(0, 2.45)
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert_itself(self):
        int_list = IntegerList(5)
        int_list.insert(0, 100)
        self.assertEqual([100, 5], int_list.get_data())

    def test_get_biggest(self):
        int_list = IntegerList(5, 200, 11)
        result = int_list.get_biggest()
        self.assertEqual(200, result)

    def test_get_index(self):
        int_list = IntegerList(5, 200, 11)
        result = int_list.get_index(200)
        self.assertEqual(1, result)


if __name__ == "__main__":
    main()
