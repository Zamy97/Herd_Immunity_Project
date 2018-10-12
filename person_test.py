from person import Person
from virus import Virus

def test_infected_and_died():
    person = Person(924, False, True)
    person.did_survive_infection()

    assert person._id = 924
    assert person.is_vaccinated = False
    assert person.infected = True

    virus = Virus("ebola", 0.4, 0.8)
