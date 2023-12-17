import ctypes
"""
реализовать динамический массив самостоятельно, а именно класс MyArray, 
включающий операции: get, set, pushBack (add), popBack (del), size. 
Дополнительно сделайте метод getCapacity, который возвращает текущую вместимость массива.
"""


class MyIntArray(object):
    def __init__(self):
        self.n = 0  # Count actual elements (Default is 0)
        self.capacity = 10  # Default Capacity
        self.A = self.make_array(self.capacity)

    def __len__(self):
        """
        Return number of elements in array
        """
        return self.n

    def get_size(self):
        return self.n

    def get(self, k):
        """
        Return element at index k
        """
        if not 0 <= k < self.n:
            # Check it k index is in bounds of array
            return IndexError('K is out of bounds !')

        return self.A[k]  # Retrieve from the array at index k

    def set(self, k, x):
        """
        set element at index k
        """
        if not 0 <= k < self.n:
            # Check it k index is in bounds of array
            return IndexError('K is out of bounds !')

        self.A[k] = x

    def pushBack(self, ele):
        """
        Add element to end of the array
        """
        if self.n == self.capacity:
            # Double capacity if not enough room
            self._increase_capacity(2 * self.capacity)

        self.A[self.n] = ele  # Set self.n index to element
        self.n += 1

    def popBack(self):
        """
        Delete item from the end of array
        """

        if self.n == 0:
            print("Array is empty deletion not Possible")
            return

        self.A[self.n - 1] = 0
        self.n -= 1

    def _increase_capacity(self, new_cap):
        """
        Resize internal array to capacity new_cap
        """

        B = self.make_array(new_cap)  # New bigger array

        for k in range(self.n):  # Reference all existing values
            B[k] = self.A[k]

        self.A = B  # Call A the new bigger array
        self.capacity = new_cap  # Reset the capacity

    def make_array(self, new_cap):
        """
        Returns a new array with new_cap capacity
        """
        return (new_cap * ctypes.py_object)()