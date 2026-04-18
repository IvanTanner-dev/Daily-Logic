import solution

def test_find_sum():
    
    assert solution.find_sum([1, 3, 5, 7], 6) == [1, 5]
    assert solution.find_sum([1, 2, 3, 4, 5], 5) == [1, 4]
    assert solution.find_sum([1, 2, 3, 4, 5], 6) == [1, 2, 3]
    assert solution.find_sum([-1, -2, 3, 4], 1) == [-1, -2, 4]
    assert solution.find_sum([3, 1, 4, 1, 5, 9, 2, 6], 10) == [3, 1, 4, 2]
    assert solution.find_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 20) == [1, 2, 3, 5, 9]
    assert solution.find_sum([7, 9, 4, 2, 5], 10) == "Sum not found"

    print("All Array Sum Finder tests passed!")

if __name__ == "__main__":
    test_find_sum()
