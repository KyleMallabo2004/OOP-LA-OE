class AnimeCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability

    def introduce(self, func):
        def wrapper(*args, **kwargs):
            print("Introducing...")
            func(*args, **kwargs)
            print("This character is amazing!")
        return wrapper

naruto = AnimeCharacter("Naruto", "Shadow Clone Jitsu")

@naruto.introduce
def character_info(anime_info):
    print(anime_info)

character_info(f"I am {naruto.name} and I can use {naruto.ability}.")