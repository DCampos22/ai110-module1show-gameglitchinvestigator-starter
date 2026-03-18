from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_reversed_hints_bug_single_guess_above():
    """Test that catches the reversed hints bug: guess 100 > secret 1 should be 'Too High'"""
    result = check_guess(100, 1)
    assert result == "Too High", "Bug detected: hints are reversed! Guess higher than secret should return 'Too High'"

def test_reversed_hints_bug_single_guess_below():
    """Test that catches the reversed hints bug: guess 1 < secret 100 should be 'Too Low'"""
    result = check_guess(1, 100)
    assert result == "Too Low", "Bug detected: hints are reversed! Guess lower than secret should return 'Too Low'"

def test_reversed_hints_bug_edge_case_one_off_above():
    """Test edge case where guess is just 1 above secret"""
    result = check_guess(51, 50)
    assert result == "Too High"

def test_reversed_hints_bug_edge_case_one_off_below():
    """Test edge case where guess is just 1 below secret"""
    result = check_guess(49, 50)
    assert result == "Too Low"

def test_reversed_hints_bug_negative_numbers():
    """Test that the bug is caught even with negative numbers"""
    result = check_guess(5, -10)
    assert result == "Too High", "Guess 5 is higher than secret -10, should return 'Too High'"
    
    result = check_guess(-10, 5)
    assert result == "Too Low", "Guess -10 is lower than secret 5, should return 'Too Low'"
