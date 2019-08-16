import solver
import pytest

DO_NOT_TEST = 0

sudoku_values = [0,0,7,0,0,0,0,0,5, \
                    0,0,0,0,0,2,0,8,3, \
                    0,0,0,7,6,0,2,1,0, \
                    0,6,4,0,9,0,0,2,1, \
                    0,0,1,8,2,3,4,0,0, \
                    2,5,0,0,1,0,8,9,0, \
                    0,8,2,0,7,1,0,0,0, \
                    3,7,0,2,0,0,0,0,0, \
                    1,0,0,0,0,0,6,0,0 ]

def test_get_row_1():
    index = 0
    s = solver.SudokuBoard(sudoku_values)
    p = solver.PossibilityExtractor(s)
    result = p.get_row(index)
    assert result == [0,0,7,0,0,0,0,0,5]

def test_get_row_2():
    index = 8
    s = solver.SudokuBoard(sudoku_values)
    p = solver.PossibilityExtractor(s)
    result = p.get_row(index)
    assert result == [0,0,7,0,0,0,0,0,5]

def test_get_row_3():
    index = 27
    s = solver.SudokuBoard(sudoku_values)
    p = solver.PossibilityExtractor(s)
    result = p.get_row(index)
    assert result == [0,6,4,0,9,0,0,2,1]

def test_get_row_4():
    index = 80
    s = solver.SudokuBoard(sudoku_values)
    p = solver.PossibilityExtractor(s)
    result = p.get_row(index)
    assert result == [1,0,0,0,0,0,6,0,0]

def test_get_row_bad_index_1():
    index = 90
    s = solver.SudokuBoard(sudoku_values)
    p = solver.PossibilityExtractor(s)
    result = p.get_row(index)
    assert result == []

def test_get_row_bad_index_2():
    index = -1
    s = solver.SudokuBoard(sudoku_values)
    p = solver.PossibilityExtractor(s)
    result = p.get_row(index)
    assert result == []

def test_get_column_1():
    index = 0
    s = solver.SudokuBoard(sudoku_values)
    p = solver.PossibilityExtractor(s)
    result = p.get_column(index)
    assert result == [0,0,0,0,0,2,0,3,1]

def test_get_column_2():
    index = 8
    s = solver.SudokuBoard(sudoku_values)
    p = solver.PossibilityExtractor(s)
    result = p.get_column(index)
    assert result == [5,3,0,1,0,0,0,0,0]

def test_get_column_3():
    index = 9
    s = solver.SudokuBoard(sudoku_values)
    p = solver.PossibilityExtractor(s)
    result = p.get_column(index)
    assert result == [0,0,0,0,0,2,0,3,1]

def test_get_column_4():
    index = 80
    s = solver.SudokuBoard(sudoku_values)
    p = solver.PossibilityExtractor(s)
    result = p.get_column(index)
    assert result == [5,3,0,1,0,0,0,0,0]

def test_get_column_bad_index_1():
    index = -1
    s = solver.SudokuBoard(sudoku_values)
    p = solver.PossibilityExtractor(s)
    result = p.get_column(index)
    assert result == []

def test_get_column_bad_index_2():
    index = 81
    s = solver.SudokuBoard(sudoku_values)
    p = solver.PossibilityExtractor(s)
    result = p.get_column(index)
    assert result == []

if DO_NOT_TEST:
    def test_get_used_values_in_row_1():
        iLower = 0
        iUpper = 8
        s = solver.SudokuBoard(sudoku_values)
        p = solver.PossibilityExtractor(s)
        result = p.get_used_values_in_row(iLower, iUpper)
        assert result == [7,5]

if DO_NOT_TEST:
    def test_get_used_values_in_row_2():
        iLower = 9
        iUpper = 17
        s = solver.SudokuBoard(sudoku_values)
        p = solver.PossibilityExtractor(s)
        result = p.get_used_values_in_row(iLower, iUpper)
        assert result == [2,8,3]

def test_get_used_values_in_row_3():
    iLower = 72
    iUpper = 80
    s = solver.SudokuBoard(sudoku_values)
    p = solver.PossibilityExtractor(s)
    result = p.get_used_values_in_row(iLower, iUpper)
    assert result == [1,6]

if DO_NOT_TEST:
    def test_get_used_values_in_row_4():
        iLower = 27
        iUpper = 35
        s = solver.SudokuBoard(sudoku_values)
        p = solver.PossibilityExtractor(s)
        result = p.get_used_values_in_row(iLower, iUpper)
        assert result == [6,4,9,2,1]

def test_get_used_values_in_row_bad_index_1():
    iLower = -1
    iUpper = 35
    s = solver.SudokuBoard(sudoku_values)
    p = solver.PossibilityExtractor(s)
    result = p.get_used_values_in_row(iLower, iUpper)
    assert result == []

def test_get_used_values_in_row_bad_index_2():
    iLower = 2
    iUpper = 100
    s = solver.SudokuBoard(sudoku_values)
    p = solver.PossibilityExtractor(s)
    result = p.get_used_values_in_row(iLower, iUpper)
    assert result == []

def test_get_used_values_in_row_bad_index_3():
    iLower = -1
    iUpper = 100
    s = solver.SudokuBoard(sudoku_values)
    p = solver.PossibilityExtractor(s)
    result = p.get_used_values_in_row(iLower, iUpper)
    assert result == []

def test_get_used_values_in_column_1():
    index = 0
    s = solver.SudokuBoard(sudoku_values)
    p = solver.PossibilityExtractor(s)
    result = p.get_used_values_in_column(0)
    assert result == [2,3,1]

if DO_NOT_TEST:
    def test_get_used_values_in_column_2():
        index = 1
        s = solver.SudokuBoard(sudoku_values)
        p = solver.PossibilityExtractor(s)
        result = p.get_used_values_in_column(0)
        assert result == [6,5,8,7]

if DO_NOT_TEST:
    def test_get_used_values_in_column_3():
        index = 8
        s = solver.SudokuBoard(sudoku_values)
        p = solver.PossibilityExtractor(s)
        result = p.get_used_values_in_column(0)
        assert result == [5,3,1]

def test_values_at_index_1():
    indexes = [2]
    s = solver.SudokuBoard(sudoku_values)
    p = solver.PossibilityExtractor(s)
    result = p.values_at_index(indexes)
    assert result == [7]

def test_values_at_index_2():
    indexes = [8]
    s = solver.SudokuBoard(sudoku_values)
    p = solver.PossibilityExtractor(s)
    result = p.values_at_index(indexes)
    assert result == [5]

def test_values_at_index_3():
    indexes = [2,8]
    s = solver.SudokuBoard(sudoku_values)
    p = solver.PossibilityExtractor(s)
    result = p.values_at_index(indexes)
    assert result == [7,5]



#This Test Means nothing Just to test build pipeline works
"""
def test_values_at_index():

    s = solver.SudokuBoard(sudoku_values)
    p = solver.PossibilityExtractor(s)
    p.extract_possibilities()

    maphere = p.refactored_novemant_map()
    val = maphere["TOP_LEFT"]

    assert [ 0,1,2,9,10,11,18,19,20 ] == val
"""