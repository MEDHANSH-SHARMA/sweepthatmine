import requests
import time


class State:
    last_action = None

    def __init__(self, rows, cols):
        self.board = [[0 * cols] * rows]


def check_status():
    return True


def update_state(s: State, a, value: int):
    r, c = a.position
    s.board[r][c] = value
    s.last_action = a


def create_locator(location):
    x, y = location
    locator = f"#cell-{x}-{y}"
    return locator


def call_api(data):
    response = requests.post(url="", data=data)
    return response.content


def run_engine(page, state):
    while check_status():
        action = call_api()
        locator = create_locator(action)
        page.locator(locator).click()

        update_state(state, action)


def run(page, rows, cols):
    s = State(rows, cols)
    run_engine(page, s)
    time.sleep(2)
