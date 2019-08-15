import solver
import pytest

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






#This Test Means nothing Just to test build pipeline works
def test_values_at_index():

    s = solver.SudokuBoard(sudoku_values)
    p = solver.PossibilityExtractor(s)
    p.extract_possibilities()

    maphere = p.refactored_novemant_map()
    val = maphere["TOP_LEFT"]

    assert [ 0,1,2,9,10,11,18,19,20 ] == val
