class DynamicArray:
    def __init__(self):
        # Start with a capacity of 4
        self.capacity = 4
        self.size = 0
        self.data = [0] * self.capacity

    def _resize(self):
        # Double the capacity when the array is full
        self.capacity *= 2
        new_data = [0] * self.capacity  # Create a new array with doubled capacity
        for i in range(self.size):
            new_data[i] = self.data[i]  # Copy old data to new array
        self.data = new_data  # Update the data to point to the new array

    def push_back(self, value):
        if self.size == self.capacity:
            self._resize()
        self.data[self.size] = value  #
        self.size += 1
    def pop_back(self):
        if self.size == 0:
            raise IndexError("Pop from empty array")  #
        value = self.data[self.size - 1]
        self.size -= 1
        return value

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        if self.size == self.capacity:
            self._resize()  # Resize if full
        # Shift elements to the right to make space for the new element
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = value  # Insert the new value
        self.size += 1  # Increment size

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")  #
        # Shift elements to the left to remove the element
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        self.size -= 1  # Decrement size

    def clear(self):
        self.size = 0  # Clear the array by resetting size

    def find(self, value):
        for i in range(self.size):
            if self.data[i] == value:
                return i  # Return the index of the first occurrence
        return -1  # Return -1 if not found

    def resize(self, new_size):
        if new_size < self.size:
            self.size = new_size  # If shrinking, truncate the array
        elif new_size > self.capacity:
            self.capacity = new_size  # Resize the array to new size
            new_data = [0] * self.capacity
            for i in range(self.size):
                new_data[i] = self.data[i]
            self.data = new_data

    def get(self, index):
        if index >= self.size or index < 0:
            raise IndexError("Index out of range")  # Handle out-of-bounds access
        return self.data[index]

    def set(self, index, value):
        if index >= self.size or index < 0:
            raise IndexError("Index out of range")  # Handle out-of-bounds access
        self.data[index] = value

    def get_size(self):
        return self.size

    def get_capacity(self):
        return self.capacity

    def is_empty(self):
        return self.size == 0

    def __str__(self):
        return str(self.data[:self.size])  # Print the elements up to the current size


# Example usage
if __name__ == "__main__":
    arr = DynamicArray()

    # Add some elements to the dynamic array
    arr.push_back(10)
    arr.push_back(60)
    arr.push_back(30)


    print(f"Array: {arr}")  # Array should have [10, 20, 30, 40]
    print(f"Size: {arr.get_size()}")  # Should print 4
    print(f"Capacity: {arr.get_capacity()}")  # Should print 4

    # Add more elements to trigger resizing
    arr.push_back(20)
    arr.push_back(55)

    print(f"Array after resizing: {arr}")
    print(f"Size after resizing: {arr.get_size()}")
    print(f"Capacity after resizing: {arr.get_capacity()}")

    # Pop an element
    popped_value = arr.pop_back()
    print(f"Popped value: {popped_value}")
    print(f"Array after pop: {arr}")  #

    # Insert at index 2
    arr.insert(2, 100)
    print(f"Array after insert: {arr}")


    arr.remove(4)
    print(f"Array after remove: {arr}")  #

    # Find an element
    index = arr.find(100)
    print(f"Index of 100: {index}")

    # Resize the array
    arr.resize(4)
    print(f"Array after resizing: {arr}")

    # Clear the array
    arr.clear()
    print(f"Array after clear: {arr}")
    print(f"Is array empty? {arr.is_empty()}")






#