import solver

#This Test Means nothing Just to test build pipeline works
def test_values_at_index():
    sudoku_values = [0,0,7,0,0,0,0,0,5, \
                     0,0,0,0,0,2,0,8,3, \
                     0,0,0,7,6,0,2,1,0, \
                     0,6,4,0,9,0,0,2,1, \
                     0,0,1,8,2,3,4,0,0, \
                     2,5,0,0,1,0,8,9,0, \
                     0,8,2,0,7,1,0,0,0, \
                     3,7,0,2,0,0,0,0,0, \
                     1,0,0,0,0,0,6,0,0 ]
    s = solver.SudokuBoard(sudoku_values)
    p = solver.PossibilityExtractor(s)
    p.extract_possibilities()

    maphere = p.refactored_novemant_map()
    val = maphere["TOP_LEFT"]

    assert [ 0,1,2,9,10,11,18,19,20 ] == val
