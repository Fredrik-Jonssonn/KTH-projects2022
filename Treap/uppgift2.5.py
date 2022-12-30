# Fredrik Jonsson, grudat22 uppgift 2.5
import random


class _node:
    """A node of a Treap that stores a string and
     a randomly assigned priority value."""

    def __init__(self, string):
        """Construct a node that stores the given string."""
        self._data = string  # _data stores the node's string.
        self._prio = random.random()  # _prio stores the node's priority value.
        self._left = None  # _left points at the Node to the left in the binary tree.
        self._right = None  # _right points at the Node to the right in the binary tree.


class Treap:
    """A Treap (randomized binary search tree) of string elements."""

    def __init__(self):
        """Construct an empty Treap."""
        self._root = None  # The root of the Treap
        self._length = 0  # number of elements in the Treap

    def _insert_helper(self, node, root):
        """Insert a node into the Treap (or sub-Treap) with
        given root-node and return the updated Treap."""
        if root is None:
            return node
        if node._data < root._data:
            root._left = self._insert_helper(node, root._left)
            if root._prio > root._left._prio:  # right rotation
                temp1 = root
                temp2 = root._left._right
                root = root._left
                root._right = temp1
                root._right._left = temp2
        else:
            root._right = self._insert_helper(node, root._right)
            if root._prio > root._right._prio:  # left rotation
                temp1 = root
                temp2 = root._right._left
                root = root._right
                root._left = temp1
                root._left._right = temp2
        return root

    def insert(self, string):
        """Insert the given string into this Treap."""
        self._root = self._insert_helper(_node(string), self._root)
        self._length += 1

    def __len__(self):
        """Return the number of elements in this Treap"""
        return self._length

    def _repr_helper(self, element_list, root):
        """Append the given list with the string elements of the
        Treap (or sub-Treap) with given root-node."""
        if root is None:
            pass
        else:
            self._repr_helper(element_list, root._left)
            element_list.append(root._data)
            self._repr_helper(element_list, root._right)

    def __repr__(self):
        """Return a string representation of this Treap.
         The string elements are enclosed in square brackets ('[]'),
         placed in alphabetical order and adjacent string elements
         are seperated by (', ')."""
        element_list = []
        self._repr_helper(element_list, self._root)
        element_list.sort(key=str.lower)
        return str(element_list)

    def _healthy(self, root="init"):
        """Test that the Treap is healthy by verifying that
        self._length is equal to the number of Treap elements
        and that all Treap elements are ordered correctly in regard
        to both string values and priority values."""
        if root == "init":
            root = self._root
        counter = 0
        if root is None:
            pass
        else:
            counter += 1
            counter += self._healthy(root._left)
            counter += self._healthy(root._right)
            assert root._left is None or root._left._data <= root._data
            assert root._left is None or root._left._prio >= root._prio
            assert root._right is None or root._right._data >= root._data
            assert root._right is None or root._right._prio >= root._prio
        if root == self._root:
            assert counter == self._length
        return counter


# Unit Test
def main():
    # __init__ test
    empty_treap = Treap()
    empty_treap._healthy()

    # insert test
    test_treap1 = Treap()
    test_treap1.insert("A")
    test_treap1._healthy()
    test_treap1.insert("a")
    test_treap1._healthy()
    test_treap1.insert("g")
    test_treap1._healthy()
    test_treap1.insert("t")
    test_treap1._healthy()
    test_treap1.insert("h")
    test_treap1._healthy()
    test_treap1.insert("T")
    test_treap1._healthy()
    test_treap1.insert("AH")
    test_treap1._healthy()
    test_treap1.insert("3")
    test_treap1._healthy()
    test_treap1.insert(":")
    test_treap1._healthy()

    # __len__ test
    assert len(empty_treap) == 0
    empty_treap._healthy()
    assert len(test_treap1) == 9
    test_treap1._healthy()

    # __repr__ test
    assert repr(empty_treap) == "[]"
    empty_treap._healthy()
    assert repr(test_treap1) == "['3', ':', 'A', 'a', 'AH', 'g', 'h', 'T', 't']"
    test_treap1._healthy()


if __name__ == '__main__':
    main()
