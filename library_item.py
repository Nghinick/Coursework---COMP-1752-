class LibraryItem:
    def __init__(self, name, director, rating=0):  # Initialize a LibraryItem object with the given attributes
        self.name = name  # Assign the name of the library item
        self.director = director  # Assign the director of the library item
        self.rating = rating  # Assign the rating of the library item (default is 0)
        self.play_count = 0  # Initialize the play count of the library item to zero

    def info(self):  # Get information about the library item
        return f"{self.name} - {self.director} {self.stars()} (Plays: {self.play_count})"  # Concatenate the name, director, stars representing rating, and play count into a string

    def stars(self):  # Generate stars based on the rating of the library item
        stars = ""  # storing stars representing the rating of the library item
        for i in range(self.rating):  # Append a star for each rating point
            stars += "*"  # adding one star to the rating of the library item
        return stars  # representing the rating of the library item

    def increment_play_count(self):  # Increment the play count of the library item by 1
        self.play_count += 1  # Increment the play count by 1
