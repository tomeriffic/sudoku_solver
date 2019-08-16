import math
from flask import Flask, request, jsonify

app = Flask(__name__) 



@app.route('/generate', methods=["POST"])
def sudoku_api():
    try:
        sudoku_values = [0,0,7,0,0,0,0,0,5, \
                    0,0,0,0,0,2,0,8,3, \
                    0,0,0,7,6,0,2,1,0, \
                    0,6,4,0,9,0,0,2,1, \
                    0,0,1,8,2,3,4,0,0, \
                    2,5,0,0,1,0,8,9,0, \
                    0,8,2,0,7,1,0,0,0, \
                    3,7,0,2,0,0,0,0,0, \
                    1,0,0,0,0,0,6,0,0 ]
        y = { "sudoku" : sudoku_values } 
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