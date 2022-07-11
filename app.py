from flask import Flask, request
from solver import solveSudoku
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['POST', 'GET'])
@cross_origin()
def solve():
    if request.method == "GET":
        return "SUDOKU SOLVER API"
    elif request.method == "POST":
        board = request.get_json()["board"]
        ans = solveSudoku(board)
        answer = {
            "answer": ans if ans else board,
            "message": "Solved!" if ans else "Not Solved!, Invalid Board"
        }
        
        return answer

if __name__ == '__main__':
    app.run()
    # app.run(host='