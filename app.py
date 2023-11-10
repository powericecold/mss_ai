from flask import Flask, render_template, request, redirect

app = Flask(__name__)

board = [' '] * 9
current_player = 'X'
game_over = False


def check_winner():
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]  # diagonals
    ]

    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return board[combo[0]]

    if ' ' not in board:
        return 'Draw'

    return None


def make_move(position):
    global current_player, game_over

    if board[position] == ' ' and not game_over:
        board[position] = current_player

        winner = check_winner()
        if winner:
            game_over = True
            return winner + ' wins!'
        elif ' ' not in board:
            game_over = True
            return 'Draw'

        current_player = 'O' if current_player == 'X' else 'X'

    return None


# Routes
@app.route('/')
def index():
    return render_template('index.html', board=board)


@app.route('/play', methods=['POST'])
def play():
    position = int(request.form['position'])
    result = make_move(position)
    if result:
        return result
    return redirect('/')


@app.route('/reset')
def reset():
    global board, current_player, game_over
    board = [' '] * 9
    current_player = 'X'
    game_over = False
    return ''


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7019, debug=True)
