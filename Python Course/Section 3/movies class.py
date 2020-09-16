# Define a Movie class that has two properties: name and director
class Movies:
    def __init__(self, new_title, new_director):
        self.title = new_title
        self.director = new_director

    def print_info(self):
        print(f"<<{self.title}>> by {self.director}")

movie_one = Movies("The Matrix", "Wachowski")
movie_two = Movies("Inception", "Christopher Nolan")

print(f"{movie_one.title} by {movie_one.director}")
print(f"{movie_two.title} by {movie_two.director}")
