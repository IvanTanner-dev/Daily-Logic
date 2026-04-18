from itertools import combinations

def find_sum(arr, target):
    # 1. Store all possible solutions alongside their indices
    all_valid_matches = []
    
    indices = list(range(len(arr)))

    # 2. Check every possible combination size (from 2 up to the full array)
    for r in range(2, len(arr) + 1):
        for combo_indices in combinations(indices, r):
            # Calculate the sum using the values at those indices
            current_combo_values = [arr[i] for i in combo_indices]
            
            if sum(current_combo_values) == target:
                # We store a tuple: (the indices, the values)
                all_valid_matches.append((combo_indices, current_combo_values))

    # 3. Handle the "Not Found" case
    if not all_valid_matches:
        return "Sum not found"

    # 4. Sort by Indices
    # Python sorts tuples element-by-element. 
    # (0, 1, 2) comes before (0, 4) because 1 < 4.
    all_valid_matches.sort()

    # 5. Return the values of the "winning" match
    winner_indices, winner_values = all_valid_matches[0]
    return winner_values