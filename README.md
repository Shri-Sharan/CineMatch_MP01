# CineMatch_MP01
Is a repository for the mini project related to cine match a simple application made using python where users can search, sort, delete, add movies and also recommend top N movies based on the rating.
The following are the components of main.py file:
1. CineMatch Class
Purpose: Manages a collection of movies and provides operations to add, search, recommend, and delete movies.
Functions:
__init__(): Initializes the class with empty lists and dictionaries.
add_movie(title, genre, rating): Adds a movie to movies_list and categorizes it in genre_dict.
search_by_title(title): Searches for a movie by its title in movies_list.
search_by_genre(genre): Retrieves movies of a specific genre from genre_dict.
recommend_top_n(n): Recommends the top n highest-rated movies from movies_list.
delete_movie(title): Deletes a movie from both movies_list and its genre list in genre_dict.
2. CineMatchGUI Class
Purpose: Provides a graphical interface using Tkinter for users to interact with the CineMatch movie management system.
Functions:
__init__(root): Initializes the GUI, sets up input fields, buttons, and result display.
add_movie(): Handles adding a movie through user input.
search_movie(): Handles searching for movies by title or genre.
recommend_top_n(): Handles recommending top movies based on user input.
delete_movie(): Handles deleting a movie by title.
Other functions handle setting up GUI components and managing user interactions.
![image](https://github.com/Shri-Sharan/CineMatch_MP01/assets/146396309/89208db8-d87b-4606-994c-5436a24584b5)


