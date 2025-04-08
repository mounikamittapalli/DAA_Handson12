class DynamicArray:
    def __init__(self):
        # Start with an initial array of size 1
        self.array = [None]
        self.size = 0
        self.capacity = 1

    def insert(self, value):
        # If we are out of space, we double the size
        if self.size == self.capacity:
            self.resize()
        # Insert the element
        self.array[self.size] = value
        self.size += 1

    def resize(self):
        # Double the size of the array
        self.capacity *= 2
        new_array = [None] * self.capacity
        # Copy the elements to the new array
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def get_size(self):
        return self.size

    def get_capacity(self):
        return self.capacity

    def get_array(self):
        return self.array[:self.size]

# Aggregate method simulation for amortized runtime
def aggregate_method_insertion(n):
    dynamic_array = DynamicArray()
    total_operations = 0

    # Insert n elements into the dynamic array
    for i in range(n):
        dynamic_array.insert(i)
        total_operations += 1
        # If we resized the array, count the extra operations
        if dynamic_array.get_size() == dynamic_array.get_capacity():
            total_operations += dynamic_array.get_size()  # Resizing cost

    # Return amortized cost per operation (aggregate method)
    amortized_cost = total_operations / n
    print(f"Aggregate Method - Total Operations: {total_operations}, Amortized Cost per Operation: {amortized_cost}")

# Accounting method simulation for amortized runtime
def accounting_method_insertion(n):
    dynamic_array = DynamicArray()
    total_operations = 0
    prepaid_credits = 0

    for i in range(n):
        # Charge O(1) for each insertion
        prepaid_credits += 1
        dynamic_array.insert(i)

        # If we resized, we need to charge extra credits to cover future costs
        if dynamic_array.get_size() == dynamic_array.get_capacity():
            # We are doubling the array size, so we charge extra credits for future insertions
            prepaid_credits += dynamic_array.get_size()  # Overcharge for future insertions
            total_operations += dynamic_array.get_size()  # Resizing cost

    # Total number of operations
    total_operations += n  # For each of the n insertions
    amortized_cost = total_operations / n
    print(f"Accounting Method - Total Operations: {total_operations}, Amortized Cost per Operation: {amortized_cost}")

n=8
aggregate_method_insertion(n)
accounting_method_insertion(n)
