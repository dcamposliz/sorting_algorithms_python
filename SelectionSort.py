class SelectionSort:

    def __init__(self, array):

        self.array = array
        self.array_length = len(array)
        self.compare_position = 0
        self.sorted_end = 0
    
    def sort(self):

        if self.array_length == 0:
            return "Cannot sort empty data structure."

        if self.array_length == 1:
            return self.array

        if not all(isinstance(element, (int, float)) for element in self.array):
            return "Cannot sort non-numeric lists"

        if self.array_length > 1:

            for i in range(0, self.array_length - 1):
                
    
    def swap(self, left_position, right_position):
        temp_left_position = self.array[left_position]
        temp_right_positon = self.array[right_position]

        self.array[right_position] = temp_left_position
        self.array[left_position] = temp_right_positon
