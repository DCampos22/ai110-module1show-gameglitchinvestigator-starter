# logic_utils.py
#
def get_range_for_difficulty(difficulty: str):
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Hard":
        return 1, 50
    return 1, 100

def parse_guess(raw: str):
    if not raw:
        return False, None, "Enter a guess."
    try:
        return True, int(float(raw)), None
    except:
        return False, None, "That is not a number."

def check_guess(guess, secret):
    # Pytest expects JUST the string for the comparison to work
    g, s = int(guess), int(secret)
    if g == s:
        return "Win"
    if g > s:
        return "Too High"
    return "Too Low"

def update_score(current_score: int, outcome: str, attempt_number: int):
    if outcome == "Win":
        points = 100 - (10 * attempt_number)
        return current_score + max(points, 10)
    if outcome in ["Too High", "Too Low"]:
        return current_score - 5
    return current_score