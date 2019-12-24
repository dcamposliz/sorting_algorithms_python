class BubbleSort:
    def __init__(self, array):
        self.array = array
        self.array_length = len(array)
        self.initial_position = 0
        self.sorted_end = len(array)
    
    def sort(self):
        
        if self.array_length == 0:
            return "Cannot sort empty data structure."

        if self.array_length == 1:
            return self.array

        if not all(isinstance(element, (int, float)) for element in self.array):
            return "Cannot sort non-numeric lists"

        if self.array_length > 1:
            for i in range(0, self.array_length - 1):     
                self.initial_position = 0
                for k in range(0, self.sorted_end - 1):
                    if self.array[self.initial_position] > self.array[self.initial_position + 1]:
                        self.swap(self.initial_position)
                    self.initial_position = self.initial_position + 1
                self.sorted_end = self.sorted_end - 1
            return self.array

    def swap(self, left_position):
        temp_left_value = self.array[left_position]
        temp_right_value = self.array[left_position + 1]

        self.array[left_position] = temp_right_value
        self.array[left_position + 1] = temp_left_value


x = [17, 3, 5, 13, 11, 7, 33.44, 22, 33, 22, 109343, 345]
some_shit = BubbleSort(x)

print(some_shit.sort())