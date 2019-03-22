class Node:
    """
    Represents a Node of a LinkedList.  Each Node contains data (the value in the list) and a reference to the next Node
    """
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLinkedList:
    """
    Represents a LinkedList.  The LinkedList is composed with the first Node (or head) and its size
    """
    def __init__(self):
        """
        This is the constructor.  It is used to create a new instance of LinkedList.

        Ref: https://www.geeksforgeeks.org/constructors-in-python/
        """
        self.head = None
        self.size = 0

    def append(self, val):
        """
        Purpose: Given a value, appends the value to the RIGHT side of the LinkedList
        Signature: append :: val (AnyVal) => SLinkedList
        Example: 1 -> 2 :: append(3) => 1 -> 2 -> 3
        :param val: AnyVal (Any type of value -> Int, String, Bool, etc)
        :return: LinkedList
        """
        new_node = Node(val)
        if self.size == 0:
            self.head = new_node
            self.size += 1
            self._print()
            return self.head

        head = self.head
        prev = None

        while head is not None:
            prev = head
            head = head.next

        prev.next = new_node
        self.size += 1

        self._print()

        return self


    def remove(self, val):
        """
        Purpose: Given a value, removes the value from the LinkedList
        Signature: remove :: val (AnyVal) => SLinkedList
        Example: 1 -> 2 -> 3 :: remove(2) => 1 -> 3
        :param val: A value of any time (AnyVal)
        :return: LinkedList
        :param val: AnyVal
        :return: SLinkedList
        """
        head = self.head
        prev = None

        if head is not None:
            if head.data == val:
                self.head = head.next
                self.size -= 1
                return self.head

        while head is not None:
            if head.data == val:
                break
            prev = head
            head = head.next

        if head is None:
            print("Not Found")
            return self.head

        prev.next = head.next
        self.size -= 1
        return self

    def get_at(self, val):
        """
        Purpose: Given an index, gets the value at the index from the LinkedList
        Signature: get :: val (AnyVal) => val (AnyVal)
        Example: 1 -> 2 -> 3 :: get(2) => 2
        :param val: AnyVal
        :return: SLinkedList
        """
        head = self.head
        index = 0

        try:
            while index != val:
                head = head.next
                index += 1

            if head is not None:
                return head.data
            else:
                print("Not Found")
        except AttributeError:
            print("Index provided was too large. Given:" + str(index) + ". Size: " + str(self._size()))

    def get(self, val):
        """
        Purpose: Given a value, gets the value from the LinkedList
        Signature: get :: val (AnyVal) => val (AnyVal)
        Example: 1 -> 2 -> 3 :: get(2) => 2
        :param val: AnyVal
        :return: SLinkedList
        """
        head = self.head

        while head is not None and head.data != val:
            head = head.next

        if head is not None and head.data is val:
            return head.data
        else:
            print("Not Found")

    def _size(self):
        """
        Purpose: Returns the size of the LinkedList
        Signature: size :: () => Int
        Example: 1 -> 2 -> 3 :: size() => 3
        :return: Int
        """
        print(self.size)
        return self.size

    def _print(self):
        """
        Purpose: Prints the SLinkedList as an Array
        Signature: _print :: () => Void
        Example: 1 -> 2 -> 3 :: _print() => print([1, 2, 3])
        :return: Void
        """
        val = self.head
        var = []

        while val:
            var.append(val.data)
            val = val.next

        print(var)


    def remove_at(self, val):
        """
        Purpose: Given an index, removes the value at that index
        Signature: remove_at :: Int => SLinkedList
        Example: 1 -> 2 -> 3 :: remove_at(1) => 1 -> 3
        :param val:
        :return:
        """
        self._print()
        return self

    def push(self, val):
        """
        Purpose: Given a value, adds the value to the LEFT side of the SLinkedList
        #todo
        :param val:
        :return:
        """

        self._print()
        return self


    def pop(self):
        """
        Purpose: Removes a value from the LEFT side of the SLinkedList
        #todo
        :param val:
        :return:
        """

        self._print()
        return self


    def enqueue(self, val):
        """
        Purpose: Given a value, adds the value to the RIGHT side of the SLinkedList
        #todo
        :param val:
        :return:
        """

        self._print()
        return self


    def dequeue(self):
        """
        Purpose: Removes a value from the RIGHT side of the SLinkedList
        #todo
        :param val:
        :return:
        """

        self._print()
        return self

def test_SLinkedList_size_should_succeed():
    test = SLinkedList()
    assert(test._size() == 0)

    test.append(1)
    assert(test._size() == 1)

    test.append(2)
    assert(test._size() == 2)

    test.append(3)
    assert(test._size() == 3)

    test.remove(1)
    assert(test._size() == 2)


def test_SLinkedList_append_should_succeed():
    test = SLinkedList()
    test.append(1)
    test.append(2)
    test.append(3)

    assert(test.get(1) == 1 and test.get(1) == 1 and test.get(2) == 2)


def test_SLinkedList_get_should_succeed():
    test = SLinkedList()
    test.append(1)
    assert(test.get(1) == 1)
    test.append(2)
    assert(test.get(2) == 2)
    test.append(3)
    assert(test.get(3) == 3)


def test_SLinkedList_getAt_should_succeed():
    test = SLinkedList()
    test.append(1)
    assert(test.get_at(0) == 1)
    test.append(2)
    assert(test.get_at(1) == 2)
    test.append(3)
    assert(test.get_at(2) == 3)


def test_SLinkedList_remove_should_succeed():
    test = SLinkedList()
    test.append(1)
    test.append(2)
    test.append(3)

    assert(test.get_at(0) == 1)
    test.remove(1)

    assert(test.get_at(0) == 2)
    test.append(1)

    assert(test.get_at(0) == 2)
    assert(test.get_at(1) == 3)
    test.remove(3)

    assert(test.get_at(0) == 2)
    assert(test.get_at(1) == 1)

    assert(test._size() == 2)
