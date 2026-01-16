class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people.clear()

    created_list = [Person(d["name"], d["age"]) for d in people]

    for inst, person_dict in zip(created_list, people):
        wife_name = person_dict.get("wife")
        if wife_name:
            wife_obj = Person.people.get(wife_name)
            if wife_obj:
                inst.wife = wife_obj

        husband_name = person_dict.get("husband")
        if husband_name:
            husband_obj = Person.people.get(husband_name)
            if husband_obj:
                inst.husband = husband_obj

    return created_list
