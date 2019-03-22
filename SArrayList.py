class SArrayList:
    """
    Represents a ArrayList.  The ArrayList is composed with the currentIndex and its data list
    """
    def __init__(self):
        """
        This is the constructor.  It is used to create a new instance of SLinkedList.

        Ref: https://www.geeksforgeeks.org/constructors-in-python/
        """
        self.currentIndex = 0
        self.data = []

    def append(self, val):
        """
        Purpose: Given a value, appends the value to the RIGHT side of the SArrayList
        Signature: append :: val (AnyVal) => SArrayList
        Example: [1, 2] :: append(3) => [1, 2, 3]
        :param val: AnyVal (Any type of value -> Int, String, Bool, etc)
        :return: SArrayList
        """
        self.currentIndex += 1
        self.data.append(val)
        print(self.data)
        return self

    def remove(self, val):
        """
        Purpose: Given a value, removes the first value from the SArrayList
        Signature: remove :: val (AnyVal) => SArrayList
        Example: [1, 2, 3] :: remove(2) => [1, 3]
        Example: [1, 2, 3, 2] :: remove(2) => [1, 3, 2]
        :param val: AnyVal
        :return: SArrayList
        """

        new_list = []
        index = 0

        # Empty List case
        if len(self.data) == 0:
            return self.data

        #todo

        #todo

        self.data = new_list

        print(new_list)
        return new_list

    def _print(self):
        """
        Purpose: Prints the SArrayList
        Signature: _print :: () => Void
        Example: [1, 2, 3] :: _print() => print([1, 2, 3])
        :return: Void
        """
        print(self.data)

    def getAt(self, index):
        """
        Purpose: Given an index, gets the value at the SArrayList
        Signature: getAt :: val (Int) => val (AnyVal)
        Example: [1, 2, 3] :: get(1) => 2
        :param index: Int
        :return: AnyVal
        """
        try:
            print(self.data[index])
            return self.data[index]
        except IndexError:
            print("Index provided was too large. Given:" + str(index) + ". Size: " + str(self._size()))

    def get(self, val):
        """
        Purpose: Given an value, gets the value at the SArrayList
        Signature: get :: val (AnyVal) => val (AnyVal)
        Example: [1, 2, 3] :: get(2) => 2
        :param val: AnyVal
        :return: AnyVal
        """
        if self.data.count(val) == 0 or self._size() == 0:
            print("Not Found")
            return None
        else:
            for item in self.data:
                if item is val:
                    return item

    def _size(self):
        """
        Purpose: Returns the size of the SArrayList
        Signature: size :: () => Int
        Example: [1, 2, 3] :: size() => 3
        :return: Int
        """
        print(len(self.data))
        return len(self.data)


    def remove_at(self, val):
        """
        Purpose: Given an index, removes the value at that index
        Signature: remove_at :: Int => SArrayList
        Example: [1, 2, 3] :: remove_at(1) => [1,  3]
        :param val: Int
        :return: SArrayList
        """
        self._print()
        return self

    def push(self, val):
        """
        Purpose: Given a value, adds the value to the LEFT side of the SArrayList
        Signature: push :: val (AnyVal) => SArrayList
        Example: [1, 2, 3] :: push(0) => [0, 1, 2, 3]
        :param val: AnyVal (Any type of value -> Int, String, Bool, etc)
        :return: SArrayList
        """
        self._print()
        return self.data


    def pop(self):
        """
        Purpose: Removes a value from the LEFT side of the SArrayList
        Signature: pop :: () => SArrayList
        Example: [1, 2, 3] :: pop(1) => [2, 3]
        :return: SArrayList
        """
        self._print()
        return self.data


    def enqueue(self, val):
        """
        Purpose: Given a value, adds the value to the RIGHT side of the SArrayList
        Signature: enqueue :: val (AnyVal) => SArrayList
        Example: [1, 2] :: enqueue(3) => [1, 2, 3]
        :param val: AnyVal (Any type of value -> Int, String, Bool, etc)
        :return: SArrayList
        """
        self._print()
        return self.data


    def dequeue(self):
        """
        Purpose: Removes a value from the RIGHT side of the SArrayList
        Signature: dequeue :: () => SArrayList
        Example: [1, 2, 3] :: dequeue(1) => [1, 2]
        :return: SArrayList
        """
        self._print()
        return self.data


def test_SArrayList_size_should_succeed():
    test = SArrayList()
    assert(test._size() == 0)

    test.append(1)
    assert(test._size() == 1)

    test.append(2)
    assert(test._size() == 2)

    test.append(3)
    assert(test._size() == 3)

    test.remove(1)
    assert(test._size() == 2)


def test_SArrayList_append_should_succeed():
    test = SArrayList()
    test.append(1)
    test.append(2)
    test.append(3)

    assert(test.getAt(0) == 1 and test.getAt(1) == 2 and test.getAt(2) == 3)


def test_SArrayList_remove_should_succeed():
    test = SArrayList()
    test.append(1)
    test.append(2)
    test.append(3)

    assert(test.getAt(0) == 1)
    test.remove(1)

    assert(test.getAt(0) == 2)
    test.append(1)

    assert(test.getAt(0) == 2)
    assert(test.getAt(1) == 3)
    test.remove(3)

    assert(test.getAt(0) == 2)
    assert(test.getAt(1) == 1)

    assert(test._size() == 2)


def test_SArrayList_get_should_succeed():
    test = SArrayList()
    test.append(1)
    test.append(2)

    assert(test.get(2) == 2)

    test.append(3)
    assert(test.get(3) == 3)

    assert(test.get(4) is None)


def test_SArrayList_getAt_should_succeed():
    test = SArrayList()
    test.append(1)
    test.append(2)

    assert(test.getAt(1) == 2)

    test.append(3)
    assert(test.getAt(2) == 3)

    assert(test.getAt(4) is None)
