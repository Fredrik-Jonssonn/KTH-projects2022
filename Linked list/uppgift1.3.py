# Fredrik Jonsson, grudat22 uppgift 1.3

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
        if self._size == 1: # Komplettering: fallet då det endast fanns ett element i listan
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

    def _healthy(self):
        """Test that the list is healthy by verifying that
         the last list element's self._next is None, that
         self._size is equal to the number of list elements, and
         that self._first and self._last point at list element unless
         the list is empty, in which case they are null pointers."""
        assert self._last is None or self._last._next is None
        temp = self._first
        counter = 0
        while temp is not None:
            counter += 1
            temp = temp._next
        assert counter == self._size
        if self._size == 0:
            assert self._first is None
            assert self._last is None
            return
        assert type(self._first) is _ListElement
        assert type(self._last) is _ListElement


# Unit Test
def main():
    # constructor test
    empty_list = LinkedList()
    empty_list._healthy()

    # add_first test
    test_list1 = LinkedList()
    test_list1.add_first(2)
    test_list1._healthy()
    assert test_list1._first._data == 2
    assert test_list1._first._next is None
    assert test_list1._last._data == 2
    test_list1.add_first(3)
    test_list1._healthy()
    assert test_list1._first._data == 3
    assert test_list1._last._data == 2
    assert test_list1._first._next is test_list1._last
    test_list1.add_first(26)
    test_list1._healthy()
    assert test_list1._first._data == 26
    assert test_list1._last._data == 2
    assert test_list1._first._next._data == 3
    assert test_list1._first._next is not test_list1._last
    assert test_list1._first._next._next is test_list1._last

    # add_last test
    test_list2 = LinkedList()
    test_list2.add_last(2)
    test_list2._healthy()
    assert test_list2._first._data == 2
    assert test_list2._first._next is None
    assert test_list2._last._data == 2
    test_list2.add_last(3)
    test_list2._healthy()
    assert test_list2._first._data == 2
    assert test_list2._last._data == 3
    assert test_list2._first._next is test_list2._last
    test_list2.add_last(26)
    test_list2._healthy()
    assert test_list2._first._data == 2
    assert test_list2._last._data == 26
    assert test_list1._first._next._data == 3
    assert test_list2._first._next is not test_list2._last
    assert test_list2._first._next._next is test_list2._last

    # get_first test
    assert empty_list.get_first() is None
    empty_list._healthy()
    assert test_list1.get_first() == 26
    test_list1._healthy()

    # get_last test
    assert empty_list.get_last() is None
    empty_list._healthy()
    assert test_list1.get_last() == 2
    test_list1._healthy()

    # get test
    assert empty_list.get(0) is None
    empty_list._healthy()
    assert test_list1.get(0) == 26
    test_list1._healthy()
    assert test_list1.get(1) == 3
    test_list1._healthy()
    assert test_list1.get(2) == 2
    test_list1._healthy()
    assert test_list1.get(3) is None
    test_list1._healthy()
    assert test_list1.get(-1) is None
    test_list1._healthy()

    # remove_first test
    assert empty_list.remove_first() is None
    empty_list._healthy()
    assert test_list1.remove_first() == 26
    test_list1._healthy()
    assert test_list1._first._data == 3
    test_list3 = LinkedList() # komplettirngstestfall: remove_first om det endast fanns ett element i listan
    test_list3.add_first(5)  # komplettirngstestfall:
    assert test_list3.remove_first() == 5 # komplettirngstestfall:
    test_list3._healthy() # komplettirngstestfall:

    # clear test
    empty_list.clear()
    empty_list._healthy()
    test_list1.clear()
    test_list1._healthy()

    # size test
    assert empty_list.size() == 0
    empty_list._healthy()
    assert test_list2.size() == 3
    test_list2._healthy()

    # string test
    assert empty_list.string() == "[]"
    empty_list._healthy()
    assert test_list1.string() == "[]"
    test_list1._healthy()
    assert test_list2.string() == "[2, 3, 26]"
    test_list2._healthy()


if __name__ == '__main__':
    main()
