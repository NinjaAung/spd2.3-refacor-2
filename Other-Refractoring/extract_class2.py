# by Kami Bigdely
# Extract class

class Actor():
    movies = []
    def __init__(self,first_name,last_name,birth_year,email):
        self.first_name = first_name
        self.last_name  = last_name
        self.birth_year = birth_year
        self.email      = email

    def add_star_movies(self,movies):
        self.movies += movies

    def send_hiring_email(self):
        print("email sent to: ", self.email)

    
    @property
    def full_name(self):
        return self.first_name + "" +   self.last_name



elizabeth = Actor('elizabeth','debicki',1990,'deb@makeschool.com')
elizabeth.add_star_movies(['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'])

jim = Actor('Jim','Carrey',1962,'jim@makeschool.com')
jim.add_star_movies(['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man'])

actors = [jim,elizabeth]
for actor in actors:
    if actor.birth_year > 1985:
        print(actor.full_name)
        print("Moves PLayed in:")
        for movie in actor.movies:
            print(movie, end=",")
        actor.send_hiring_email()
