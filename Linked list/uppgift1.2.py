# Fredrik Jonsson, grudat22 uppgift 1.2

class _ListElement:
    """A list element that stores a value of type T."""

    def __init__(self, value):
        """Construct a list element with given value of type T."""
        # _data stores the list element's value of type T.
        self._data = value
        # _next points at the next element in the linked list.
        self._next = None

    def _edit_next(self, list_element):
        """Edit _next so that it points to another list element."""
        self._next = list_element


class LinkedList:
    """A singly linked list of elements of type T."""

    def __init__(self):
        """Create an empty list."""
        self._first = None  # first element in list
        self._last = None  # last element in list
        self._size = 0  # number of element in list

    def add_first(self, element):
        """Insert the given element at the beginning of this list."""
        temp = _ListElement(element)
        temp._edit_next(self._first)
        self._first = temp
        if self._last is None:
            self._last = temp
        self._size += 1

    def add_last(self, element):
        """Insert the given element at the end of this list."""
        temp = _ListElement(element)
        if self._last is not None:
            self._last._edit_next(temp)
        self._last = temp
        if self._first is None:
            self._first = temp
        self._size += 1

    def get_first(self):
        """Return the first element of this list.
        Return None if the list is empty"""
        if self._first is None:
            return None
        return self._first._data

    def get_last(self):
        """Return the last element of this list.
        Return None if the list is empty"""
        if self._first is None:
            return None
        return self._last._data

    def get(self, index):
        """Return the element at the specified position in this list.
        Return None if index is out of bounds"""
        if index > self._size - 1 or index < 0:
            return None
        temp = self._first
        for i in range(0, index):
            temp = temp._next
        return temp._data

    def remove_first(self):
        """Remove and returns the first element from this list.
        Return None if the list is empty."""
        if self._first is None:
            return None
        temp = self._first._data
        self._first = self._first._next
        if self._size == 1:  # Komplettering: fallet då det endast fanns ett element i listan
            self._last = None
        self._size -= 1
        return temp

    def clear(self):
        """Remove all elements from this list."""
        self._first = None
        self._last = None
        self._size = 0

    def size(self):
        """Return the number of elements in this list."""
        return self._size

    def string(self):
        """Return a string representation of this list.
        The elements are enclosed in square brackets ('[]').
        Adjacent elements are seperated by ', ' """
        if self._first is None:
            return "[]"
        str_repr = "["
        for i in range(0, self._size):
            str_repr += str(self.get(i)) + ", "
        str_repr = str_repr[:-2]
        str_repr += "]"
        return str_repr


# Unit Test
def main():
    # constructor test
    empty_list = LinkedList()
    assert empty_list._first is None
    assert empty_list._last is None
    assert empty_list._size == 0

    # add_first test
    test_list1 = LinkedList()
    test_list1.add_first(2)
    assert type(test_list1._first) is _ListElement
    assert test_list1._first._data == 2
    assert test_list1._first._next is None
    assert type(test_list1._last) is _ListElement
    assert test_list1._last._data == 2
    assert test_list1._last._next is None
    assert test_list1._size == 1
    test_list1.add_first(3)
    assert test_list1._first._data == 3
    assert test_list1._last._data == 2
    assert test_list1._first._next is test_list1._last
    assert test_list1._size == 2
    test_list1.add_first(26)
    assert test_list1._first._data == 26
    assert test_list1._last._data == 2
    assert test_list1._first._next._data == 3
    assert test_list1._first._next is not test_list1._last
    assert test_list1._first._next._next is test_list1._last
    assert test_list1._size == 3

    # add_last test
    test_list2 = LinkedList()
    test_list2.add_last(2)
    assert type(test_list2._first) is _ListElement
    assert test_list2._first._data == 2
    assert test_list2._first._next is None
    assert type(test_list2._last) is _ListElement
    assert test_list2._last._data == 2
    assert test_list2._last._next is None
    assert test_list2._size == 1
    test_list2.add_last(3)
    assert test_list2._first._data == 2
    assert test_list2._last._data == 3
    assert test_list2._first._next is test_list2._last
    assert test_list2._size == 2
    test_list2.add_last(26)
    assert test_list2._first._data == 2
    assert test_list2._last._data == 26
    assert test_list1._first._next._data == 3
    assert test_list2._first._next is not test_list2._last
    assert test_list2._first._next._next is test_list2._last
    assert test_list2._size == 3

    # get_first test
    assert empty_list.get_first() is None
    assert test_list1.get_first() == 26

    # get_last test
    assert empty_list.get_last() is None
    assert test_list1.get_last() == 2

    # get test
    assert empty_list.get(0) is None
    assert test_list1.get(0) == 26
    assert test_list1.get(1) == 3
    assert test_list1.get(2) == 2
    assert test_list1.get(3) is None
    assert test_list1.get(-1) is None

    # remove_first test
    assert empty_list.remove_first() is None
    assert test_list1.remove_first() == 26
    assert test_list1._first._data == 3
    assert test_list1._size == 2
    test_list3 = LinkedList()  # komplettirngstestfall: remove_first om det endast fanns ett element i listan
    test_list3.add_first(5)  # komplettirngstestfall:
    assert test_list3.remove_first() == 5  # komplettirngstestfall:
    assert test_list3._last is None  # komplettirngstestfall:
    assert test_list3._first is None  # komplettirngstestfall:

    # clear test
    empty_list.clear()
    assert empty_list._first is None
    assert empty_list._last is None
    assert empty_list._size == 0
    test_list1.clear()
    assert test_list1._first is None
    assert test_list1._last is None
    assert test_list1._size == 0

    # size test
    assert empty_list.size() == 0
    assert test_list2.size() == 3

    # string test
    assert empty_list.string() == "[]"
    assert test_list1.string() == "[]"
    assert test_list2.string() == "[2, 3, 26]"


if __name__ == '__main__':
    main()
