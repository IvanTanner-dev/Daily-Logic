import solution

def test_find_org():
    
    assert solution.find_org("NASA") == "National Avocado Storage Authority"
    assert solution.find_org("CIA") == "Cats Infiltration Agency"
    assert solution.find_org("FBI") == "Fluffy Beanbag Inspectors"
    assert solution.find_org("DOJ") == "Department Of Jelly"
    assert solution.find_org("WHO") == "Wild Honey Organization"
    assert solution.find_org("EPA") == "Eating Pancakes Administration"

if __name__ == "__main__":
    try:
        test_find_org()
        print("All 6 tests passed successfully!")
    except AssertionError as e:
        print(f"A test failed! Check your dictionary keys or function logic.")