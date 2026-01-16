class Person:
    people = {}

    def  __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

def create_person_list(people: list) -> list:
    # Спочатку створюємо всіх людей
    created_list = []
    for person_dict in people:
        name = person_dict["name"]
        age = person_dict["age"]
        person = Person(name, age)
        created_list.append(person)
    for i, person_dict in enumerate(people):
        inst = created_list[i]
        wife_name = person_dict.get("wife")
        if wife_name is not None:
            wife_obj = Person.people.get(wife_name)
            if wife_obj is not None:
                inst.wife = wife_obj
        husband_name = person_dict.get("husband")
        if husband_name is not None:
            husband_obj = Person.people.get(husband_name)
            if husband_obj is not None:
                inst.husband = husband_obj
    return created_list