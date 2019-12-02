from models import Animal
def seed_animals():
    Animal.create(
        name = 'Rover',
        breed= 'Golden Retriever',
        shelter= 1,
        age=2,
        gender= 'male',
        photo= 'https://images.unsplash.com/photo-1536809188428-e8ecf663d0be?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
        description = "Rover is a runner, give him room to run!"

    )
    Animal.create(
        name = 'Leela',
        breed= 'Husky',
        shelter= 1,
        age= 4,
        gender= 'female',
        photo= 'https://images.unsplash.com/photo-1491604612772-6853927639ef?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
        description = "I'm active, you should be too."

    )
    Animal.create(
        name = 'Tangy',
        breed= 'Pit',
        shelter= 1,
        age= 3,
        gender= 'female',
        photo= 'https://images.unsplash.com/photo-1561984142-7fabd0b4c9b4?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
        description = "I'll be your bestfriend & your guard dog."

    )
    Animal.create(
        name = 'Slinky',
        breed= 'Dachshund',
        shelter= 1 ,
        age= 2,
        gender= 'male',
        photo= 'https://images.unsplash.com/photo-1520087619250-584c0cbd35e8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
        description = "I'll make sure you feel loved when you come home."

    )
    Animal.create(
        name = 'Kalli',
        breed= 'Sheep Dog',
        shelter= 1,
        age= 5,
        gender= 'female',
        photo= 'https://images.unsplash.com/photo-1503256207526-0d5d80fa2f47?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
        description = "Momma says I'm sweet & special."

    )
    Animal.create(
        name = 'Coco',
        breed= 'Chocolate Lab',
        shelter= 1,
        age= 4,
        gender= 'female',
        photo= 'https://images.unsplash.com/photo-1518717758536-85ae29035b6d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
        description = "I love licks & I hope you love licks."

    )
    Animal.create(
        name = 'Erkel',
        breed= 'Pug',
        shelter= 1,
        age= 4,
        gender= 'male',
        photo= 'https://images.unsplash.com/photo-1518020382113-a7e8fc38eac9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
        description = "Wanna play dressup?"

    )
    Animal.create(
        name = 'Spots',
        breed= 'Dalmation',
        shelter= 1,
        age= 6,
        gender= 'male',
        photo= 'https://images.unsplash.com/photo-1544838395-536d74f37082?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
        description = "I'm retired."

    )
    Animal.create(
        name = 'Sandy',
        breed= 'Golden Retriever',
        shelter= 2,
        age= 6,
        gender= 'female',
        photo= 'https://images.unsplash.com/photo-1501472193205-56ffb66400f0?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
        description = "Let's play outside."

    )
     Animal.create(
        name = 'Chief',
        breed= 'Chocolate Lab',
        shelter= 2,
        age= 8,
        gender= 'male',
        photo= 'https://images.unsplash.com/photo-1562317305-58a17fe2c09e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
        description = "They say I'm old, but not too old to be adopted."

    )
    Animal.create(
        name = 'Caramel',
        breed= 'Mix',
        shelter= 2,
        age= 4,
        gender= 'male',
        photo= 'https://images.unsplash.com/photo-1500206859124-9f13895ce7da?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
        description = "I'm good with kids & other pups!"

    )
    Animal.create(
        name = 'Snuggles',
        breed= 'Pug',
        shelter= 2,
        age= 4,
        gender= 'male',
        photo= 'https://images.unsplash.com/photo-1488830006793-1fb328d93241?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
        description = "I'll drool all over you to tell you that I love you."

    )
    Animal.create(
        name = 'Rusty',
        breed= 'Sheepdog',
        shelter= 2,
        age= 8,
        gender= 'male',
        photo= 'https://images.unsplash.com/photo-1487341290491-1081724e5844?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
        description = "Let's be friends."

    )
    Animal.create(
        name = 'Shelly',
        breed= 'Schnauzer',
        shelter= 2,
        age= 7,
        gender= 'female',
        photo= 'https://images.unsplash.com/photo-1498534928137-473daa67f5c4?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
        description = "I can prove em all wrong, you can teach an old dog new tricks!"

    )
    Animal.create(
        name = 'Evie',
        breed= 'Tabby',
        shelter= 3,
        age= 4,
        gender= 'female',
        photo= 'https://images.unsplash.com/photo-1518791841217-8f162f1e1131?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
        description = "I'll let you pet me only when I want."

    )
    Animal.create(
        name = 'Joker',
        breed= 'Tabby',
        shelter= 3,
        age= 2,
        gender= 'male',
        photo= 'https://images.unsplash.com/photo-1543852786-1cf6624b9987?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
        description = "They say I'm funny looking."

    )
    Animal.create(
        name = 'Bluebell',
        breed= 'Siamese',
        shelter= 3,
        age= 2,
        gender= 'female',
        photo= 'https://images.unsplash.com/photo-1488740304459-45c4277e7daf?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
        description = "They tell me I'm pretty, but I wouldn't know."

    )
    Animal.create(
        name = 'Garfield',
        breed= 'Tabby',
        shelter= 3,
        age= 5,
        gender= 'male',
        photo= 'https://images.unsplash.com/photo-1548546738-8509cb246ed3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
        description = "I like to be outside"

    )
    Animal.create(
        name = 'Stripes',
        breed= 'Tabby',
        shelter= 3,
        age=4,
        gender= 'male',
        photo= 'https://images.unsplash.com/photo-1549221987-25a490f65d34?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
        description = "I'm active, you should be too."

    )
    Animal.create(
        name = 'Sunshine',
        breed= 'Tabby',
        shelter= 4,
        age= 3,
        gender= 'female',
        photo= 'https://images.unsplash.com/photo-1511044568932-338cba0ad803?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
        description = "I like to subathe."

    )
    Animal.create(
        name = 'Ole Yeller',
        breed= 'Mix',
        shelter= 4,
        age= 5,
        gender= 'male',
        photo= 'https://images.unsplash.com/photo-1568480524008-e01b3be104bb?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
        description = "Barking is kind of my thing."

    )
    Animal.create(
        name = 'Gracie',
        breed= 'Shih Tzu',
        shelter= 4,
        age= 2,
        gender= 'female',
        photo= 'https://images.unsplash.com/photo-1571325639049-c8ff0761afef?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80',
        description = "Let's play outside."

    )
    Animal.create(
        name = 'Phoenix',
        breed= 'Bombay',
        shelter= 4,
        age= 5,
        gender= 'male',
        photo= 'https://images.unsplash.com/photo-1516280030429-27679b3dc9cf?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
        description = "I better get let outside."

    )
    Animal.create(
        name = 'Grayson',
        breed= 'German Shepherd mix',
        shelter= 4 ,
        age= 5,
        gender= 'male',
        photo= 'https://images.unsplash.com/photo-1562221440-aba53beefed2?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
        description = "I'm a good boy."

    )    
    Animal.create(
        name = 'McCaw',
        breed= 'Cockatiel',
        shelter= 5,
        age= 3,
        gender= 'male',
        photo= 'https://images.unsplash.com/photo-1458410489211-ba19aa2f2902?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
        description = "I'm a quiet birdy."

    ) 
    Animal.create(
        name = 'Louise',
        breed= 'Macaw',
        shelter= 5,
        age= 5,
        gender= 'male',
        photo= 'https://images.unsplash.com/photo-1497941818502-94b842b7ec0f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
        description = "Let's dance."

    ) 
    Animal.create(
        name = 'Ross',
        breed= 'Rooster',
        shelter= 5,
        age= 3,
        gender= 'male',
        photo= 'https://images.unsplash.com/photo-1549027032-1977c20d11ff?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
        description = "I'll bring the ladies home."

    ) 
   
if __name__ == "main":
    seed_animals()