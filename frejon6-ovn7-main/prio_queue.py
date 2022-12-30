# The module prio_queue provides a queue data structure with priority functionality.
#
# A priority queue is an extension of the queue data structure where all elements
# are placed in and removed from the queue according to a given priority value.
#
# That means that elements that are enqueued are assigned a priority value that
# will determine the enqueued elements' position in the queue. An enqueued element
# will be placed in the queue so that all elements in front of it have
# priority values larger than or equal to its priority value and so that all
# elements behind it have priority values less than its priority value.
# This has the effect that elements with high priority values will be removed before
# elements with lower priority values when the first element in the queue is dequeued,
# i.e. when the queue moves forward. This also means that when two elements share
# a priority value they will be enqueued/dequeued according to FIFO; first in first out.


class _PrioQueueElement:
    """A priority queue element that stores a value of type string, float or
    int, a priority value of type float or int and points
    to the elements in front of and behind of it in the queue."""

    def __init__(self, value, prio):
        """Construct a queue element that stores the given value
        of type string, float or int and the given priority
        value of type float or int that doesn't
        point at any other queue elements."""
        # _data stores the queue element's value.
        self._data = value
        # _prio stores the queue element's priority value.
        self._prio = prio
        # _in_front points at the element in front of this one in the queue.
        self._in_front = None
        # _behind points at the element behind this one in the queue.
        self._behind = None


class PrioQueue:
    """A priority queue of elements of type string, float
    or int with an associated priority value of type float
    or int."""

    def __init__(self):
        """Create an empty priority queue"""
        # _first stores the element first in queue.
        self._first = None
        # _last stores the element last in queue.
        self._last = None
        # _length stores the number of elements in the queue.
        self._length = 0

    def enqueue(self, element, prio):
        """Place the given element of type string, float or int
        with the given priority value of type float or int in this
        priority queue at a position so that all elements in front have
        a larger or equal priority value and all elements behind have a
        smaller priority value."""
        enqueued_element = _PrioQueueElement(element, prio)
        if self._first is None:
            self._first = enqueued_element
            self._last = enqueued_element
        elif self._last._prio >= enqueued_element._prio:
            enqueued_element._in_front = self._last
            self._last._behind = enqueued_element
            self._last = enqueued_element
        else:
            temp = self._last
            while (temp._in_front is not None) and (enqueued_element._prio > temp._in_front._prio):
                temp = temp._in_front
            enqueued_element._in_front = temp._in_front
            enqueued_element._behind = temp
            if temp._in_front is not None:
                temp._in_front._behind = enqueued_element
            else:
                self._first = enqueued_element
            temp._in_front = enqueued_element
        self._length += 1

    def dequeue(self):
        """Return and remove the first element in this priority queue.
        Return None if the queue is empty."""
        if self._first is None:
            return None
        temp = self._first._data
        self._first = self._first._behind
        self._first._in_front = None
        if self._length == 1:
            self._last = None
        self._length -= 1
        return temp

    def look(self, index):
        """Return the element at the specified position in this
        priority queue without removing it. The element at index
        0 is first in the queue. Return None if index is out of
        bounds."""
        if index > self._length-1 or index < 0:
            return None
        if index > self._length//2:
            temp = self._last
            for i in range(self._length - 1 - index):
                temp = temp._in_front
            return temp._data
        else:
            temp = self._first
            for i in range(index):
                temp = temp._behind
            return temp._data

    def look_first(self):
        """Return the first element in this priority queue without
        removing it. Return None if the queue is empty."""
        if self._first is None:
            return None
        return self._first._data

    def look_last(self):
        """Return the last element in this priority queue without
        removing it. Return None if the queue is empty."""
        if self._first is None:
            return None
        return self._last._data

    def clear(self):
        """Remove all elements from this priority queue."""
        self._first = None
        self._last = None
        self._length = 0

    def __len__(self):
        """Return the number of elements in this priority queue."""
        return self._length

    def __repr__(self):
        """Return a string representation of this priority queue.
        The queue elements are enclosed in square brackets ( ' [ ] ' ),
        placed in queue order (the first element in the string
        is first in the queue) and adjacent elements are
        seperated by ( ', ' )."""
        repr_list = []
        temp = self._first
        for i in range(self._length):
            repr_list.append(temp._data)
            temp = temp._behind
        return str(repr_list)
