class SelectionSort:

    def __init__(self, array):

        self.array = array
        self.array_length = len(array)
        
        self.left_compare_index = None
        self.right_compare_index = None

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
                
                for j in range(self.sorted_end, self.array_length - 1):
                    
                    self.left_compare_index = j
                    self.right_compare_index = j + 1

                    if self.array[self.left_compare_index] > self.array[self.right_compare_index]:
                        print("  {0} is larger than {1}".format(self.array[self.left_compare_index], self.array[self.right_compare_index]))

                self.sorted_end = self.sorted_end + 1
                print("----- End of iteration {0} -----".format(i))


    
    def swap(self, left_position, right_position):
        temp_left_position = self.array[left_position]
        temp_right_positon = self.array[right_position]

        self.array[right_position] = temp_left_position
        self.array[left_position] = temp_right_positon

x = [17, 3, 5, 13, 11, 7]
some_shit = SelectionSort(x)

some_shit.sort()