def is_valid_isbn_13(s):
    count = 0
    total = 0
    for value in s:
        if value not in "0123456789-":
            return False
        else:
            if value.isdigit():
                count += 1
                
                if count % 2 == 0:
                    total += 3 * int(value)
                    
                else:
                    total += int(value)
                        
    return count == 13 and (total % 10 == 0)