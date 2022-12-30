import prio_queue as pq


def healthy(queue):
    """Test that the given priority queue is healthy by verifying
    that the first queue element's self._front is None and the last
    queue element's self._behind is None, that self._length is
    equal to the number of enqueued elements, that self._first
    and self_last point at priority queue elements unless the
    queue is empty, in which case they are null pointers and
    that the queue is ordered correctly according to priority
    values."""
    assert queue._last is None or queue._last._behind is None
    assert queue._first is None or queue._first._in_front is None
    forward_counter = 0
    temp1 = queue._last
    while temp1 is not None:
        if temp1._in_front is not None:
            assert temp1._prio <= temp1._in_front._prio
        forward_counter += 1
        temp1 = temp1._in_front
    assert forward_counter == queue._length
    backward_counter = 0
    temp2 = queue._first
    while temp2 is not None:
        if temp2._behind is not None:
            assert temp2._prio >= temp2._behind._prio
        backward_counter += 1
        temp2 = temp2._behind
    assert backward_counter == queue._length
    if queue._length == 0:
        assert queue._first is None
        assert queue._last is None
        return
    assert type(queue._first) is pq._PrioQueueElement
    assert type(queue._last) is pq._PrioQueueElement


def main():
    # __init__ test
    empty_test_queue = pq.PrioQueue()
    healthy(empty_test_queue)

    # enqueue test
    test_queue1 = pq.PrioQueue()
    test_queue1.enqueue(1, 4)
    healthy(test_queue1)
    test_queue1.enqueue(90, 6)
    healthy(test_queue1)
    test_queue1.enqueue(12, 1)
    healthy(test_queue1)
    test_queue1.enqueue(1, 10)
    healthy(test_queue1)
    test_queue1.enqueue(6, 1)
    healthy(test_queue1)
    test_queue1.enqueue(5, 6)
    healthy(test_queue1)
    test_queue1.enqueue(4, 3)
    healthy(test_queue1)
    test_queue1.enqueue(3, 10)
    healthy(test_queue1)
    test_queue2 = pq.PrioQueue()
    test_queue2.enqueue("A", 10.34)
    healthy(test_queue2)
    test_queue2.enqueue("BD", 100.3)
    healthy(test_queue2)
    test_queue2.enqueue("S", 100.3)
    healthy(test_queue2)
    test_queue2.enqueue("AA", 0.1)
    healthy(test_queue2)
    test_queue2.enqueue("O", 15.5)
    healthy(test_queue2)

    # __repr__ test
    assert repr(empty_test_queue) == "[]"
    healthy(empty_test_queue)
    assert repr(test_queue1) == "[1, 3, 90, 5, 1, 4, 12, 6]"
    healthy(test_queue1)
    assert repr(test_queue2) == "['BD', 'S', 'O', 'A', 'AA']"
    healthy(test_queue2)

    # look test
    assert empty_test_queue.look(0) is None
    healthy(empty_test_queue)
    assert empty_test_queue.look(1) is None
    healthy(empty_test_queue)
    assert empty_test_queue.look(-1) is None
    healthy(empty_test_queue)
    assert test_queue1.look(0) == 1
    healthy(test_queue1)
    assert test_queue1.look(7) == 6
    healthy(test_queue1)
    assert test_queue1.look(2) == 90
    healthy(test_queue1)
    assert test_queue1.look(4) == 1
    healthy(test_queue1)
    assert test_queue1.look(10) is None
    healthy(test_queue1)
    assert test_queue1.look(-10) is None
    healthy(test_queue1)
    assert test_queue2.look(0) == 'BD'
    healthy(test_queue2)
    assert test_queue2.look(4) == 'AA'
    healthy(test_queue2)
    assert test_queue2.look(3) == 'A'
    healthy(test_queue2)
    assert test_queue2.look(2) == 'O'
    healthy(test_queue2)
    assert test_queue2.look(10) is None
    healthy(test_queue2)
    assert test_queue2.look(-10) is None
    healthy(test_queue2)

    # look_first test
    assert empty_test_queue.look_first() is None
    healthy(empty_test_queue)
    assert test_queue1.look_first() == 1
    healthy(test_queue1)
    assert test_queue2.look_first() == 'BD'
    healthy(test_queue2)

    # look_last test
    assert empty_test_queue.look_last() is None
    healthy(empty_test_queue)
    assert test_queue1.look_last() == 6
    healthy(test_queue1)
    assert test_queue2.look_last() == 'AA'
    healthy(test_queue2)

    # __len__ test
    assert len(empty_test_queue) == 0
    healthy(empty_test_queue)
    assert len(test_queue1) == 8
    healthy(test_queue1)
    assert len(test_queue2) == 5
    healthy(test_queue2)

    # dequeue test
    assert empty_test_queue.dequeue() is None
    assert len(empty_test_queue) == 0
    healthy(empty_test_queue)
    assert test_queue1.dequeue() == 1
    assert len(test_queue1) == 7
    healthy(test_queue1)
    assert test_queue1.dequeue() == 3
    assert len(test_queue1) == 6
    healthy(test_queue1)
    assert test_queue1.dequeue() == 90
    assert len(test_queue1) == 5
    healthy(test_queue1)
    assert test_queue2.dequeue() == 'BD'
    assert len(test_queue2) == 4
    healthy(test_queue1)
    assert test_queue2.dequeue() == 'S'
    assert len(test_queue2) == 3
    healthy(test_queue2)
    assert test_queue2.dequeue() == 'O'
    assert len(test_queue2) == 2
    healthy(test_queue2)
    assert repr(empty_test_queue) == "[]"
    healthy(empty_test_queue)
    assert repr(test_queue1) == "[5, 1, 4, 12, 6]"
    healthy(test_queue1)
    assert repr(test_queue2) == "['A', 'AA']"
    healthy(test_queue2)

    # clear test
    empty_test_queue.clear()
    assert len(empty_test_queue) == 0
    healthy(empty_test_queue)
    test_queue1.clear()
    assert len(test_queue1) == 0
    healthy(test_queue1)
    test_queue2.clear()
    assert len(test_queue2) == 0
    healthy(test_queue2)


if __name__ == '__main__':
    main()
