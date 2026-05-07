def get_greeting(s):
    hour = int(s[:2])
    
    if not 0 <= hour <= 23:
        return "Input not a time!"
        
    if 5 <= hour < 12:
        return "Good morning"
    if 12 <= hour < 18:
        return "Good afternoon"
    if 18 <= hour < 22:
        return "Good evening"
        
    return "Good night"