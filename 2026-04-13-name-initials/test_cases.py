from solution import get_initials;

def test_get_initials():
    assert solution.get_initials("John Doe") == "J.D."
    assert solution.get_initials("Alice Bob Charlie") == "A.B.C."
    assert solution.get_initials("Jane") == "J."
    print("All tests passed!")

test_get_initials()