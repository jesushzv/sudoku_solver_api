from flask import Flask, request
from solver import solveSudoku

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/', methods=['POST', 'GET'])
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

@app.route("/test",methods=['POST'])
def test():
    data = request.get_json()
    print(data)
    return "OK"

if __name__ == '__main__':
    app.run()
    # app.run(host='