from solution import get_next_bingo_number

def run_tests():
    tests = [
        ("B10", "B11"),      # Standard case
        ("B15", "I16"),      # Boundary case (Letter change)
        ("I30", "N31"),      # Boundary case
        ("N45", "G46"),      # Boundary case
        ("G60", "O61"),      # Boundary case
        ("O75", "B1"),       # The "Reset" case (Back to start)
        ("O65", "O66"),      # Standard case in high range
    ]

    print("--- Running Bingo Tests ---")
    
    for input_val, expected in tests:
        actual = get_next_bingo_number(input_val)
        
        if actual == expected:
            print(f"PASS: Input {input_val} -> Output {actual}")
        else:
            print(f"FAIL: Input {input_val} | Expected {expected} | Got {actual}")

if __name__ == "__main__":
    run_tests()