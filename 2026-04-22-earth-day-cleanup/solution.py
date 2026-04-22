def get_cleanup_score(items):
    earth_dict = {
        "bottle": 10,
        "can": 6,
        "bag": 8,
        "tire":	35,
        "straw": 4,
        "cardboard": 3,
        "newspaper": 3,
        "shoe": 12,
        "electronics": 25,
        "battery": 18,
        "mattress": 38,
        
    }

    score = 0
    last_item = None
    streak_count = 0

    for index, item in enumerate(items):
        count = index + 1
        
        if isinstance(item, str):
            current_value = earth_dict[item]

            if item == last_item:
                streak_count += 1
            else:
                streak_count = 0

            current_value += streak_count

            last_item = item
        
        else:

            current_value = item[1]
            streak_count = 0
            last_item = None

        if count % 5 == 0:
            
            multiplier = (count // 5) + 1
            
            current_value *= multiplier
            
        
        score += current_value

    return score