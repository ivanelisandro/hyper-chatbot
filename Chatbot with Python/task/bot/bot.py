class Astro:
    def __init__(self):
        self.name = "Astro"
        self.birth_year = 2026
        self.username = ""

    def run(self):
        print(f"Hello! My name is {self.name}.")
        print(f"I was created in {self.birth_year}.")
        self.remind_name()
        self.greet()

    def remind_name(self):
        print("Please, remind me your name.")
        self.username = input()

    def greet(self):
        print(f"What a great name you have, {self.username}!")


if __name__ == "__main__":
    astro = Astro()
    astro.run()