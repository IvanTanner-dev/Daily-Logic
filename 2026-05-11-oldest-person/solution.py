def get_oldest(people):
    if not people:
        return []
    max_age = max(person['age'] for person in people)
    oldest_people = [person['name'] for person in people if person['age'] == max_age]
    return oldest_people