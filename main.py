import tkinter as tk
from tkinter import messagebox

class CineMatch:
    def __init__(self):
        self.movies_list = []
        self.genre_dict = {}
    
    def add_movie(self, title, genre, rating):
        movie = {"title": title, "genre": genre, "rating": rating}
        self.movies_list.append(movie)
        if genre in self.genre_dict:
            self.genre_dict[genre].append(movie)
        else:
            self.genre_dict[genre] = [movie]
    
    def search_by_title(self, title):
        for movie in self.movies_list:
            if movie['title'].lower() == title.lower():
                return movie
        return None
    
    def search_by_genre(self, genre):
        return self.genre_dict.get(genre, [])
    
    def recommend_top_n(self, n):
        sorted_movies = sorted(self.movies_list, key=lambda x: x['rating'], reverse=True)
        return sorted_movies[:n]
    
    def delete_movie(self, title):
        self.movies_list = [movie for movie in self.movies_list if movie['title'].lower() != title.lower()]
        for genre in self.genre_dict:
            self.genre_dict[genre] = [movie for movie in self.genre_dict[genre] if movie['title'].lower() != title.lower()]

class CineMatchGUI:
    def __init__(self, root):
        self.cine_match = CineMatch()
        self.root = root
        self.root.title("CineMatch Movie Recommendation System")

        # Add Movie
        self.label_title = tk.Label(root, text="Title")
        self.label_title.grid(row=0, column=0)
        self.entry_title = tk.Entry(root)
        self.entry_title.grid(row=0, column=1)

        self.label_genre = tk.Label(root, text="Genre")
        self.label_genre.grid(row=1, column=0)
        self.entry_genre = tk.Entry(root)
        self.entry_genre.grid(row=1, column=1)

        self.label_rating = tk.Label(root, text="Rating")
        self.label_rating.grid(row=2, column=0)
        self.entry_rating = tk.Entry(root)
        self.entry_rating.grid(row=2, column=1)

        self.button_add = tk.Button(root, text="Add Movie", command=self.add_movie)
        self.button_add.grid(row=3, column=0, columnspan=2)

        # Search Movie
        self.label_search = tk.Label(root, text="Search by Title or Genre")
        self.label_search.grid(row=4, column=0)
        self.entry_search = tk.Entry(root)
        self.entry_search.grid(row=4, column=1)

        self.search_option = tk.StringVar(value="title")
        self.radio_title = tk.Radiobutton(root, text="Title", variable=self.search_option, value="title")
        self.radio_title.grid(row=5, column=0)
        self.radio_genre = tk.Radiobutton(root, text="Genre", variable=self.search_option, value="genre")
        self.radio_genre.grid(row=5, column=1)

        self.button_search = tk.Button(root, text="Search", command=self.search_movie)
        self.button_search.grid(row=6, column=0, columnspan=2)

        # Recommend Top N Movies
        self.label_top_n = tk.Label(root, text="Recommend Top N Movies")
        self.label_top_n.grid(row=7, column=0)
        self.entry_top_n = tk.Entry(root)
        self.entry_top_n.grid(row=7, column=1)
        self.button_top_n = tk.Button(root, text="Recommend", command=self.recommend_top_n)
        self.button_top_n.grid(row=8, column=0, columnspan=2)

        # Delete Movie
        self.label_delete_title = tk.Label(root, text="Delete Movie by Title")
        self.label_delete_title.grid(row=9, column=0)
        self.entry_delete_title = tk.Entry(root)
        self.entry_delete_title.grid(row=9, column=1)
        self.button_delete = tk.Button(root, text="Delete", command=self.delete_movie)
        self.button_delete.grid(row=10, column=0, columnspan=2)

        # Results Area
        self.text_results = tk.Text(root, height=15, width=50)
        self.text_results.grid(row=11, column=0, columnspan=2)

    def add_movie(self):
        title = self.entry_title.get()
        genre = self.entry_genre.get()
        rating = self.entry_rating.get()
        if title and genre and rating:
            try:
                rating = float(rating)
                self.cine_match.add_movie(title, genre, rating)
                self.text_results.insert(tk.END, f"Added movie: {title}\n")
                self.entry_title.delete(0, tk.END)
                self.entry_genre.delete(0, tk.END)
                self.entry_rating.delete(0, tk.END)
            except ValueError:
                messagebox.showerror("Invalid Input", "Rating must be a number.")
        else:
            messagebox.showerror("Invalid Input", "All fields are required.")

    def search_movie(self):
        search_term = self.entry_search.get()
        search_type = self.search_option.get()
        if search_term:
            if search_type == "title":
                result = self.cine_match.search_by_title(search_term)
                if result:
                    self.text_results.insert(tk.END, f"Search by Title '{search_term}':\n")
                    self.text_results.insert(tk.END, f"Title: {result['title']}, Genre: {result['genre']}, Rating: {result['rating']}\n")
                else:
                    self.text_results.insert(tk.END, f"Movie '{search_term}' not found.\n")
            elif search_type == "genre":
                results = self.cine_match.search_by_genre(search_term)
                if results:
                    self.text_results.insert(tk.END, f"Search by Genre '{search_term}':\n")
                    for movie in results:
                        self.text_results.insert(tk.END, f"Title: {movie['title']}, Genre: {movie['genre']}, Rating: {movie['rating']}\n")
                else:
                    self.text_results.insert(tk.END, f"No movies found in genre '{search_term}'.\n")
            self.entry_search.delete(0, tk.END)
        else:
            messagebox.showerror("Invalid Input", "Search term is required.")

    def recommend_top_n(self):
        n = self.entry_top_n.get()
        if n:
            try:
                n = int(n)
                results = self.cine_match.recommend_top_n(n)
                self.text_results.insert(tk.END, f"Top {n} Movies:\n")
                for movie in results:
                    self.text_results.insert(tk.END, f"Title: {movie['title']}, Genre: {movie['genre']}, Rating: {movie['rating']}\n")
                self.entry_top_n.delete(0, tk.END)
            except ValueError:
                messagebox.showerror("Invalid Input", "N must be an integer.")
        else:
            messagebox.showerror("Invalid Input", "N is required.")

    def delete_movie(self):
        title = self.entry_delete_title.get()
        if title:
            self.cine_match.delete_movie(title)
            self.text_results.insert(tk.END, f"Deleted movie: {title}\n")
            self.entry_delete_title.delete(0, tk.END)
        else:
            messagebox.showerror("Invalid Input", "Title is required.")

if __name__ == "__main__":
    root = tk.Tk()
    gui = CineMatchGUI(root)
    root.mainloop()
