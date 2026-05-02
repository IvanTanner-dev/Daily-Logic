def get_deepest_brackets(a):
    current_depth = 0
    max_depth = 0
    deepest_content = ""
    openers, closers = "([{", ")]}"
    for char in a:
           
        if char in openers:
            current_depth += 1 
            if current_depth > max_depth:
                max_depth = current_depth
                deepest_content = ""    
        
        elif char in closers:
            current_depth -= 1
        
        else:
            if current_depth == max_depth:
                deepest_content += char

    return deepest_content