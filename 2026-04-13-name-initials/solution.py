def get_initials(name):
    words = name.split()
    initials = []
    for word in words:
        initials.append(word[0]+".")
    result = "".join(initials)
    return(result)