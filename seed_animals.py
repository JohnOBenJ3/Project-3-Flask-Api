from models import Animal
def seed_animals():
    Animal.create(
        name = 'Rover',
        breed= 'Golden Retriever',
        shelter= 1,
        age=2,
        gender= 'male',
        photo= '',
        description = "Rover is a runner, give him room to run!"

    )
if __name__ == "main":
    seed_animals()