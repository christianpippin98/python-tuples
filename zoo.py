zoo = (
    "Bengal Tiger",
    "African Meerkat",
    "Arctic Wolf",
    "Peregrine Falcon",
    "American Bison",
    "Polar Bear",
    "Japanese Macaque",
    "Snowy Owl",
    "Arctic Fox",
    "Red Panda"
    )

print(zoo.index("Arctic Wolf"))

animal_to_find = "Japanese Macaque"

if animal_to_find in zoo:
    print(f"{animal_to_find} is in the zoo.")

(first_animal, second_animal, third_animal, fourth_animal, fifth_animal, sixth_animal, seventh_animal, eighth_animal, ninth_animal, tenth_animal) = zoo

print(second_animal)
print(fourth_animal)
print(sixth_animal)
print(eighth_animal)

zoo_list = list(zoo)

zoo_list.extend(["King Penguin", "Asian Water Monitor", "Gigantopithecus"])

zoo = tuple(zoo_list)