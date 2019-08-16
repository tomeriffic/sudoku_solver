import math
from flask import Flask, request, jsonify

app = Flask(__name__) 

class SudokuBoard:
    def __init__(self, sudoku_array):
        self.sudoku_array = sudoku_array
        self.values_to_completion = sudoku_array.count(0)
        self.completed_values = dict((i, sudoku_array.count(i)) for i in sudoku_array)
        self.completed_values.pop(0)

class PossibilityExtractor:
    """
    Will return a list of possible values_at_index in each index
    e.g.
    (0, [4,6,8,9]),
    (1, [1,2,3,4,9])
    """
    def __init__(self, sudoku_puzzle):
        list_of_possibilities = []
        puzzle_size = len(sudoku_puzzle.sudoku_array)
        i = 0
        while i < puzzle_size:
            val_in_puzzle = sudoku_puzzle.sudoku_array[i]
            if val_in_puzzle == 0:
                possibility = (val_in_puzzle, [1,2,3,4,5,6,7,8,9])
            else:
                possibility = (val_in_puzzle, [])
            list_of_possibilities.append(possibility)
            i = i + 1

        self.possibilities = list_of_possibilities
        self.squared_len = int(math.sqrt(puzzle_size))
        self.puzzle = sudoku_puzzle
        self.puzzle_array_len = len(sudoku_puzzle.sudoku_array)
        self.nov_map = self.refactored_novemant_map()

    def extract_possibilities(self):
        self.extract_possible_from_row()
        self.extract_possible_from_column()
        self.extract_possible_from_novemant()
        self.extract_possible_brute_force()

        #-------------------------------------------------------
        #BRUTE FORCE PROCESSING
        #-------------------------------------------------------
    def retrieve_priority_index(self):
        largest_val = 0
        index = 0
        for i in range(1, len(self.puzzle.completed_values)):
            val = self.puzzle.completed_values[i]
            if val > largest_val and val != 9:
                largest_val = val
                index = i
        return index

    def locate_novemants_where_value_is_not_contained(self, value_to_search):
        list_of_novs_text = []
        nov_map = self.refactored_novemant_map()
        for nov in nov_map:
            index_map = nov_map[nov]
            values_in_novem = [self.puzzle.sudoku_array[i] for i in index_map]
            if value_to_search not in values_in_novem:
                list_of_novs_text.append(nov)
        return list_of_novs_text

    def get_candidates_locations(self, value_to_search_to_insert):
        novemant_list = self.locate_novemants_where_value_is_not_contained(value_to_search_to_insert)
        candidate_indexes = []
        candidate_values = []
        for nov in novemant_list:
            candidate_indexes.extend(self.nov_map[nov])
        for index in candidate_indexes:
            candidate_values.append(self.puzzle.sudoku_array[index])
        candidate_zip = list(zip(candidate_indexes, candidate_values))
        #for i in candidate_zip: 
        #    if i[1] != 0:
        #        candidate_zip.remove(i)
        candidate_zip = [ i for i in candidate_zip if i[1] == 0]
        return candidate_zip

    def extract_possible_brute_force(self):
        highest_priority = self.retrieve_priority_index()
        novemant_list = self.locate_novemants_where_value_is_not_contained(highest_priority)
        candidate_zip = self.get_candidates_locations(highest_priority)

        reduced_candidates = []
        for i in candidate_zip:
            row = self.get_row(i[0])
            column = self.get_column(i[0])
            if not(highest_priority in row or highest_priority in column):
                reduced_candidates.append(i)

        nov_count = []
        for nov in novemant_list:
            for index in reduced_candidates:
                if index[0] in self.nov_map[nov]:
                    x =  nov
                    nov_count.append( x )

        for nov in self.nov_map:
            count = nov_count.count(nov)
            if count == 1:
                self.possibilities[i[0]] = (i[1], [highest_priority])

    def get_row(self, index):
        if index > 80 or index < 0:
            return []
        if ( index % self.squared_len == 0):
            row = [self.puzzle.sudoku_array[i] for i in range(index , index + self.squared_len)]
            return row
        else:
            #raise ValueError #implement self heal
            mod_result = index % self.squared_len
            return self.get_row(index - mod_result)
            
    def get_column(self, index):
        if index > 80 or index < 0:
            return []
        col_index = index % 9
        col = [ self.puzzle.sudoku_array[i] for i in range(col_index, self.puzzle_array_len, self.squared_len) ]
        return col

        #-------------------------------------------------------
        #ROW PROCESSING
        #-------------------------------------------------------
    def get_used_values_in_row(self, lower, upper):
        if lower > 80 or lower < 0:
            return  []
        if upper > 80 or upper < 0:
            return []
        list_of_existing_values_in_puzzle = []
        i = lower
        while i < upper:
            if self.puzzle.sudoku_array[i] != 0:
                list_of_existing_values_in_puzzle.append(self.puzzle.sudoku_array[i])
            i = i + 1
        return list_of_existing_values_in_puzzle

    def ammend_row_possibilities(self, lower, upper, found_values):
        i = lower
        while i < upper:
            x = found_values
            y = self.possibilities[i][1]
            new_list = [ item for item in y if item not in x ]
            self.possibilities[i] = (self.puzzle.sudoku_array[i], new_list)
            i = i + 1

    def process_row(self, lower, upper):
        used_values = self.get_used_values_in_row(lower, upper)
        self.ammend_row_possibilities(lower, upper, used_values)

    def extract_possible_from_row(self):
        i = 0
        while i < self.puzzle_array_len:
            range_lower = i
            range_upper = i + self.squared_len
            self.process_row(range_lower, range_upper)
            i = range_upper

        #-------------------------------------------------------
        #COLUMN PROCESSING
        #-------------------------------------------------------
    
    def get_used_values_in_column(self, column_start_val):
        list_of_used_values = []
        i = column_start_val
        while i < self.puzzle_array_len:
            if self.puzzle.sudoku_array[i] != 0:
                list_of_used_values.append(self.puzzle.sudoku_array[i])
            i = i + self.squared_len
        return list_of_used_values
    
    def ammend_column_possibilities(self, column_start_val, found_values):
        i = column_start_val
        while i < self.puzzle_array_len:
            x = found_values
            y = self.possibilities[i][1]
            new_list = [ item for item in y if item not in x ]
            self.possibilities[i] = (self.puzzle.sudoku_array[i], new_list)
            i = i + self.squared_len

    def process_column(self, column_start_val):
        used_values = self.get_used_values_in_column(column_start_val)
        self.ammend_column_possibilities(column_start_val, used_values)
    
    def extract_possible_from_column(self):
        column_start_val = 0
        while column_start_val < self.squared_len:
            self.process_column(column_start_val)
            column_start_val = column_start_val + 1

        #-------------------------------------------------------
        #NOVEMANT PROCESSING
        #-------------------------------------------------------
    
    def extract_possible_from_novemant(self):
        i = 0
        nov_pos_map = self.novemant_map()

        while i < self.squared_len:
            for small_square in nov_pos_map:
                if i in small_square:
                    x = self.values_at_index(small_square)
                    y = self.possibilities[i][1]
                    new_list = [ item for item in y if item not in x ]
                    self.possibilities[i] = (self.puzzle.sudoku_array[i], new_list)
                    break
            i = i + 1

    def novemant_map(self):
        TOP_LEFT        = [  0, 1, 2,\
                             9,10,11,\
                            18,19,20 ]

        TOP_MIDDLE      = [  3, 4, 5,\
                            12,13,14,\
                            21,22,23 ]

        TOP_RIGHT       = [  6, 7, 8,\
                            15,16,17,\
                            24,25,26 ]

        MIDDLE_LEFT     = [ 27,28,29,\
                            36,37,38,\
                            45,46,47 ]

        CENTER          = [ 30,31,32,\
                            39,40,41,\
                            48,49,50 ]

        MIDDLE_RIGHT    = [ 33,34,35,\
                            42,43,44,\
                            51,52,53 ]

        BOTTOM_LEFT     = [ 54,55,56,\
                            63,64,65,\
                            72,73,74 ]

        BOTTOM_MIDDLE   = [ 57,58,59,\
                            66,67,68,\
                            75,76,77 ]

        BOTTOM_RIGHT    = [ 60,61,62,\
                            69,70,71,\
                            78,79,80 ]
        
        position_map = [TOP_LEFT,       TOP_MIDDLE,     TOP_RIGHT,\
                        MIDDLE_LEFT,    CENTER,         MIDDLE_RIGHT,\
                        BOTTOM_LEFT,    BOTTOM_MIDDLE,  BOTTOM_RIGHT]
        return position_map
      
    def refactored_novemant_map(self):
        nov_map = {
            "TOP_LEFT" : [ 0,1,2,9,10,11,18,19,20 ],
            "TOP_MIDDLE" : [ 3,4,5,12,13,14,21,22,23 ],
            "TOP_RIGHT" : [ 6,7,8,15,16,17,24,25,26 ],
            "MIDDLE_LEFT" : [ 27,28,29,36,37,38,45,46,47 ],
            "CENTER" : [ 30,31,32,39,40,41,48,49,50 ],
            "MIDDLE_RIGHT" : [ 33,34,35,42,43,44,51,52,53 ],
            "BOTTOM_LEFT" : [ 54,55,56,63,64,65,72,73,74 ],
            "BOTTOM_MIDDLE" : [ 57,58,59,66,67,68,75,76,77 ],
            "BOTTOM_RIGHT" : [ 60,61,62,69,70,71,78,79,80 ]
        }
        return nov_map

    def values_at_index(self, list_of_indexes):
        values_in_nov = []
        for index in list_of_indexes:
            value = self.puzzle.sudoku_array[index]
            if value != 0:
                values_in_nov.append(value)
        return values_in_nov

        #-------------------------------------------------------
        #PRINT DATA
        #-------------------------------------------------------
    def print_definate_values(self):
        i = 0
        for pissabolity in self.possibilities:
            if len(pissabolity[1]) == 1 and pissabolity[0] == 0:
                print( "Location: " + str(i) + " " + str(pissabolity) )
            i = i + 1

    def get_possibilities_for_index(self, index, bPrint):
        if index > self.puzzle_array_len or index < 0:
            raise IndexError
        x = self.possibilities[index]
        if bPrint == 1:
            pass
            #print("Location: " + index + " Value: " + str(x[0]) + " Possibilities: " + str(x[1]))
        return x[1]
        
        #-------------------------------------------------------
        #UPDATE SUDOKU
        #-------------------------------------------------------
    def update_sudoku(self):
        i = 0
        for poss in self.possibilities:
            if poss[0] == 0 and len(poss[1]) == 1:
                self.puzzle.sudoku_array[i] = poss[1][0]
            i = i + 1
        return self.puzzle.sudoku_array

class TestPossibilityExtractor:

    def test_list(self, p):
        status = True
        overall_status = True
    
        status = self.__test_case(p.get_possibilities_for_index(0, 0), [4,6,8,9])
        overall_status = self.__combine_status(status)
    
        status = self.__test_case(p.get_possibilities_for_index(1, 0), [1,2,3,4,9])
        overall_status = self.__combine_status(status)
    
        status = self.__test_case(p.get_possibilities_for_index(9, 0), [4,5,6,7,9])
        overall_status = self.__combine_status(status)
    
        status = self.__test_case(p.get_possibilities_for_index(20, 0), [3,5,8,9])
        overall_status = self.__combine_status(status)
    
        status = self.__test_case(p.get_possibilities_for_index(27, 0), [5,7,8])
        overall_status = self.__combine_status(status)
    
        status = self.__test_case(p.get_possibilities_for_index(37, 0), [9])
        overall_status = self.__combine_status(status)
    
        status = self.__test_case(p.get_possibilities_for_index(80, 0), [2,4,7,8,9])
        overall_status = self.__combine_status(status)
    
        if(overall_status == False):
            #print("UNIT TEST FAILED")
            return False
        else:
            return True

    def __test_case(self, inserted, expected):
        b_test_case = False
        if len(inserted) != len(expected):
            return b_test_case
        else:
            iterator = zip(inserted, expected)
            for item in iterator:
                if (item[0] != item[1]):
                    return b_test_case
            
            b_test_case = True
    
        return b_test_case

    def __combine_status(self, status):
        if status == False:
            overall_status = False
            return overall_status

"""           
def print_sudoku(sudoku):
    i = 0
    token = ""
    size = len(sudoku)
    while i < size:
        if i % 3 == 0: 
            token = " "

        if i % 9 == 0:
            token = "\n"

        if i == 0:
            token = ""

        #print(str(sudoku[i]) + ",", end=token)
        i = i + 1
        token = ""
        sudoku.pop(0)
"""
def sudoku_solve_iteration(sudoku_values):
    s = SudokuBoard(sudoku_values)
    p = PossibilityExtractor(s)
    p.extract_possibilities()
    #p.print_definate_values()
    return p.update_sudoku()
    
def unit_test():
    #Can be divided into test puzzles
    sudoku_values = [0,0,7,0,0,0,0,0,5, \
                     0,0,0,0,0,2,0,8,3, \
                     0,0,0,7,6,0,2,1,0, \
                     0,6,4,0,9,0,0,2,1, \
                     0,0,1,8,2,3,4,0,0, \
                     2,5,0,0,1,0,8,9,0, \
                     0,8,2,0,7,1,0,0,0, \
                     3,7,0,2,0,0,0,0,0, \
                     1,0,0,0,0,0,6,0,0 ]
    s = SudokuBoard(sudoku_values)
    p = PossibilityExtractor(s)
    p.extract_possibilities()
    t = TestPossibilityExtractor()
    return t.test_list(p)
    
def main(args):
    sudoku_values = args
    i = 0
    while True:
        print("ITERATION: " + str(i))
        sudoku_values = sudoku_solve_iteration(sudoku_values)
        i = i + 1
        break #Breaking after first
    #print("Done")
    return sudoku_values

@app.route('/sudoku_solve', methods=["POST"])
def sudoku_api():
    try:
        x = main( request.json["sudoku"] )
        y = { "solved_sudoku" : x } 
        return jsonify(y)
    except:
        pass


if __name__ == "__main__":
    app.run(host="0.0.0.0")







    
"""
sudoku_values = [0,0,7,0,0,0,0,0,5, \
                0,0,0,0,0,2,0,8,3, \
                0,0,0,7,6,0,2,1,0, \
                0,6,4,0,9,0,0,2,1, \
                0,0,1,8,2,3,4,0,0, \
                2,5,0,0,1,0,8,9,0, \
                0,8,2,0,7,1,0,0,0, \
                3,7,0,2,0,0,0,0,0, \
                1,0,0,0,0,0,6,0,0 ] 

#main(sudoku_values)
"""
""" PASSED IN
0,0,7,  0,0,0,  0,0,5,
0,0,0,  0,0,2,  0,8,3, 
0,0,0,  7,6,0,  2,1,0, 

0,6,4,  0,9,0,  0,2,1, 
0,0,1,  8,2,3,  4,0,0, 
2,5,0,  0,1,0,  8,9,0, 

0,8,2,  0,7,1,  0,0,0, 
3,7,0,  2,0,0,  0,0,0, 
1,0,0,  0,0,0,  6,0,0 
"""
