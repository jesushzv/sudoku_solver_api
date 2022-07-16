from email import message
from unittest import result
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
        data = request.get_json()
        if data is None:
            return "No data provided"
        elif data["board"] is None:
            return "No board provided"
        board = data["board"]
        ans = solveSudoku(board)
        answer = {
            "answer": ans["result"] if ans["result"] != False else board,
            "message": ans["message"]
        }
        
        return answer

if __name__ == '__main__':
    app.run()
    # app.run(host='