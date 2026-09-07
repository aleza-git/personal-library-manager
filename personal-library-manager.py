import tkinter as tk
from tkinter import messagebox


class PersonalLibrary:

    def __init__(self, root):
        self.root = root
        self.root.title("Personal Library Manager")
        self.root.geometry("950x650")
        self.root.resizable(False, False)
        self.root.configure(bg="#f5f1ea")

        self.books = []

        self.create_ui()
        self.show_home()

    # =========================
    # MAIN UI
    # =========================

    def create_ui(self):

        # Sidebar
        self.sidebar = tk.Frame(
            self.root,
            bg="#263238",
            width=220
        )
        self.sidebar.pack(
            side="left",
            fill="y"
        )
        self.sidebar.pack_propagate(False)

        tk.Label(
            self.sidebar,
            text="PERSONAL",
            font=("Georgia", 11),
            bg="#263238",
            fg="#b9c7c9"
        ).pack(pady=(35, 0))

        tk.Label(
            self.sidebar,
            text="LIBRARY",
            font=("Georgia", 24, "bold"),
            bg="#263238",
            fg="#f5eee2"
        ).pack()

        tk.Label(
            self.sidebar,
            text="your little digital bookshelf",
            font=("Arial", 8, "italic"),
            bg="#263238",
            fg="#849397"
        ).pack(pady=(2, 35))

        self.create_nav_button(
            "⌂   Home",
            self.show_home
        )

        self.create_nav_button(
            "＋   Add Book",
            self.show_add
        )

        self.create_nav_button(
            "▤   My Books",
            self.show_books
        )

        self.create_nav_button(
            "⌕   Search",
            self.show_search
        )

        self.create_nav_button(
            "★   Reading Stats",
            self.show_stats
        )

        tk.Label(
            self.sidebar,
            text="Python + Tkinter",
            font=("Arial", 8),
            bg="#263238",
            fg="#849397"
        ).pack(
            side="bottom",
            pady=20
        )

        # Main content
        self.main = tk.Frame(
            self.root,
            bg="#f5f1ea"
        )
        self.main.pack(
            side="right",
            fill="both",
            expand=True
        )

    def create_nav_button(self, text, command):

        tk.Button(
            self.sidebar,
            text=text,
            font=("Arial", 10, "bold"),
            bg="#263238",
            fg="#dce4e5",
            activebackground="#37474f",
            activeforeground="#ffffff",
            relief="flat",
            anchor="w",
            padx=25,
            pady=12,
            command=command
        ).pack(
            fill="x",
            padx=12,
            pady=3
        )

    def clear_main(self):

        for widget in self.main.winfo_children():
            widget.destroy()

    def heading(self, title, subtitle):

        tk.Label(
            self.main,
            text=title,
            font=("Georgia", 26, "bold"),
            bg="#f5f1ea",
            fg="#263238"
        ).pack(
            anchor="w",
            padx=35,
            pady=(30, 2)
        )

        tk.Label(
            self.main,
            text=subtitle,
            font=("Arial", 10),
            bg="#f5f1ea",
            fg="#7b8587"
        ).pack(
            anchor="w",
            padx=35,
            pady=(0, 25)
        )

    # =========================
    # HOME
    # =========================

    def show_home(self):

        self.clear_main()

        self.heading(
            "Welcome back.",
            "A quiet place for the books you're reading, finished, and waiting for."
        )

        stats = tk.Frame(
            self.main,
            bg="#f5f1ea"
        )
        stats.pack(
            fill="x",
            padx=35
        )

        self.create_stat_card(
            stats,
            "BOOKS",
            str(len(self.books)),
            "#e6ded0"
        )

        self.create_stat_card(
            stats,
            "READ",
            str(self.count_status("Read")),
            "#d7e3dc"
        )

        self.create_stat_card(
            stats,
            "READING",
            str(self.count_status("Reading")),
            "#e2d8e8"
        )

        # Quote / welcome section
        box = tk.Frame(
            self.main,
            bg="#fffdf8"
        )
        box.pack(
            fill="x",
            padx=35,
            pady=35
        )

        tk.Label(
            box,
            text="“A room without books is like a body without a soul.”",
            font=("Georgia", 15, "italic"),
            bg="#fffdf8",
            fg="#455154",
            wraplength=650
        ).pack(
            pady=(28, 5),
            padx=25
        )

        tk.Label(
            box,
            text="— Marcus Tullius Cicero",
            font=("Arial", 9),
            bg="#fffdf8",
            fg="#8b9293"
        ).pack(
            pady=(0, 25)
        )

        tk.Button(
            box,
            text="＋  Add a Book",
            font=("Arial", 10, "bold"),
            bg="#263238",
            fg="white",
            relief="flat",
            command=self.show_add
        ).pack(
            pady=(0, 25),
            ipadx=20,
            ipady=9
        )

    def create_stat_card(
        self,
        parent,
        title,
        value,
        color
    ):

        card = tk.Frame(
            parent,
            bg=color,
            height=110
        )
        card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 12)
        )
        card.pack_propagate(False)

        tk.Label(
            card,
            text=value,
            font=("Georgia", 25, "bold"),
            bg=color,
            fg="#263238"
        ).pack(
            anchor="w",
            padx=18,
            pady=(17, 0)
        )

        tk.Label(
            card,
            text=title,
            font=("Arial", 8, "bold"),
            bg=color,
            fg="#667174"
        ).pack(
            anchor="w",
            padx=18
        )

    # =========================
    # ADD BOOK
    # =========================

    def show_add(self):

        self.clear_main()

        self.heading(
            "Add a Book",
            "Add something new to your collection."
        )

        form = tk.Frame(
            self.main,
            bg="#fffdf8"
        )
        form.pack(
            fill="x",
            padx=35
        )

        self.title_entry = self.create_entry(
            form,
            "Book Title"
        )

        self.author_entry = self.create_entry(
            form,
            "Author"
        )

        self.genre_entry = self.create_entry(
            form,
            "Genre"
        )

        self.rating_entry = self.create_entry(
            form,
            "Rating (1 - 5)"
        )

        tk.Label(
            form,
            text="Reading Status",
            font=("Arial", 9, "bold"),
            bg="#fffdf8",
            fg="#596366"
        ).pack(
            anchor="w",
            padx=25,
            pady=(8, 3)
        )

        self.status_var = tk.StringVar(
            value="Want to Read"
        )

        status_menu = tk.OptionMenu(
            form,
            self.status_var,
            "Want to Read",
            "Reading",
            "Read"
        )

        status_menu.config(
            font=("Arial", 10),
            bg="#eee9e0",
            fg="#263238",
            relief="flat",
            highlightthickness=0
        )

        status_menu.pack(
            anchor="w",
            padx=25
        )

        tk.Button(
            form,
            text="SAVE BOOK",
            font=("Arial", 10, "bold"),
            bg="#263238",
            fg="white",
            relief="flat",
            command=self.add_book
        ).pack(
            pady=25,
            ipadx=30,
            ipady=9
        )

    def create_entry(self, parent, label):

        tk.Label(
            parent,
            text=label,
            font=("Arial", 9, "bold"),
            bg="#fffdf8",
            fg="#596366"
        ).pack(
            anchor="w",
            padx=25,
            pady=(10, 3)
        )

        entry = tk.Entry(
            parent,
            font=("Arial", 11),
            bg="#f1ede6",
            fg="#263238",
            relief="flat"
        )

        entry.pack(
            fill="x",
            padx=25,
            ipady=8
        )

        return entry

    def add_book(self):

        title = self.title_entry.get().strip()
        author = self.author_entry.get().strip()
        genre = self.genre_entry.get().strip()
        rating = self.rating_entry.get().strip()
        status = self.status_var.get()

        if not title or not author or not genre:

            messagebox.showwarning(
                "Missing Information",
                "Please enter the title, author and genre."
            )
            return

        if rating:

            try:
                rating = float(rating)

                if rating < 1 or rating > 5:
                    raise ValueError

            except ValueError:

                messagebox.showerror(
                    "Invalid Rating",
                    "Rating must be between 1 and 5."
                )
                return

        else:
            rating = 0

        self.books.append({
            "title": title,
            "author": author,
            "genre": genre,
            "rating": rating,
            "status": status
        })

        messagebox.showinfo(
            "Book Added",
            f'"{title}" was added to your library.'
        )

        self.show_books()

    # =========================
    # BOOKS
    # =========================

    def show_books(self):

        self.clear_main()

        self.heading(
            "My Books",
            f"{len(self.books)} book(s) in your library."
        )

        if not self.books:

            tk.Label(
                self.main,
                text="Your bookshelf is empty.",
                font=("Georgia", 16, "italic"),
                bg="#f5f1ea",
                fg="#8a9293"
            ).pack(pady=70)

            return

        container = tk.Frame(
            self.main,
            bg="#f5f1ea"
        )
        container.pack(
            fill="both",
            expand=True,
            padx=35
        )

        for index, book in enumerate(self.books):

            self.create_book_card(
                container,
                book,
                index
            )

    def create_book_card(
        self,
        parent,
        book,
        index
    ):

        card = tk.Frame(
            parent,
            bg="#fffdf8",
            height=95
        )
        card.pack(
            fill="x",
            pady=5
        )
        card.pack_propagate(False)

        # Book number
        tk.Label(
            card,
            text=f"{index + 1:02}",
            font=("Georgia", 15, "bold"),
            bg="#e6ded0",
            fg="#455154",
            width=4
        ).pack(
            side="left",
            fill="y"
        )

        info = tk.Frame(
            card,
            bg="#fffdf8"
        )
        info.pack(
            side="left",
            fill="both",
            expand=True,
            padx=18,
            pady=12
        )

        tk.Label(
            info,
            text=book["title"],
            font=("Georgia", 13, "bold"),
            bg="#fffdf8",
            fg="#263238"
        ).pack(
            anchor="w"
        )

        rating = "—"

        if book["rating"] > 0:
            rating = f"{book['rating']}/5"

        tk.Label(
            info,
            text=(
                f"{book['author']}  •  "
                f"{book['genre']}  •  Rating: {rating}"
            ),
            font=("Arial", 9),
            bg="#fffdf8",
            fg="#7b8587"
        ).pack(
            anchor="w"
        )

        status_color = self.get_status_color(
            book["status"]
        )

        tk.Label(
            card,
            text=book["status"],
            font=("Arial", 8, "bold"),
            bg=status_color,
            fg="#344044",
            padx=10,
            pady=5
        ).pack(
            side="right",
            padx=15
        )

        tk.Button(
            card,
            text="×",
            font=("Arial", 13),
            bg="#fffdf8",
            fg="#9a7777",
            relief="flat",
            command=lambda i=index:
            self.delete_book(i)
        ).pack(
            side="right",
            padx=5
        )

    def get_status_color(self, status):

        colors = {
            "Read": "#d7e3dc",
            "Reading": "#e2d8e8",
            "Want to Read": "#e6ded0"
        }

        return colors.get(
            status,
            "#eeeeee"
        )

    # =========================
    # SEARCH
    # =========================

    def show_search(self):

        self.clear_main()

        self.heading(
            "Search Library",
            "Find a book by title, author, or genre."
        )

        search_box = tk.Frame(
            self.main,
            bg="#fffdf8"
        )
        search_box.pack(
            fill="x",
            padx=35
        )

        entry = tk.Entry(
            search_box,
            font=("Arial", 12),
            bg="#f1ede6",
            relief="flat"
        )
        entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=20,
            pady=18,
            ipady=9
        )

        results = tk.Frame(
            self.main,
            bg="#f5f1ea"
        )
        results.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=20
        )

        def search():

            for widget in results.winfo_children():
                widget.destroy()

            query = entry.get().lower().strip()

            found = []

            for book in self.books:

                if (
                    query in book["title"].lower()
                    or query in book["author"].lower()
                    or query in book["genre"].lower()
                ):
                    found.append(book)

            if not found:

                tk.Label(
                    results,
                    text="No books found.",
                    font=("Georgia", 15, "italic"),
                    bg="#f5f1ea",
                    fg="#8a9293"
                ).pack(pady=60)

                return

            for book in found:

                card = tk.Frame(
                    results,
                    bg="#fffdf8"
                )
                card.pack(
                    fill="x",
                    pady=4
                )

                tk.Label(
                    card,
                    text=book["title"],
                    font=("Georgia", 13, "bold"),
                    bg="#fffdf8",
                    fg="#263238"
                ).pack(
                    anchor="w",
                    padx=20,
                    pady=(12, 2)
                )

                tk.Label(
                    card,
                    text=(
                        f"{book['author']}  •  "
                        f"{book['genre']}  •  "
                        f"{book['status']}"
                    ),
                    font=("Arial", 9),
                    bg="#fffdf8",
                    fg="#7b8587"
                ).pack(
                    anchor="w",
                    padx=20,
                    pady=(0, 12)
                )

        tk.Button(
            search_box,
            text="SEARCH",
            font=("Arial", 9, "bold"),
            bg="#263238",
            fg="white",
            relief="flat",
            command=search
        ).pack(
            side="right",
            padx=15,
            ipadx=15,
            ipady=8
        )

    # =========================
    # STATISTICS
    # =========================

    def show_stats(self):

        self.clear_main()

        self.heading(
            "Reading Statistics",
            "A small look at your reading habits."
        )

        if not self.books:

            tk.Label(
                self.main,
                text="Add some books to see your statistics.",
                font=("Georgia", 15, "italic"),
                bg="#f5f1ea",
                fg="#8a9293"
            ).pack(pady=70)

            return

        stats = tk.Frame(
            self.main,
            bg="#f5f1ea"
        )
        stats.pack(
            fill="x",
            padx=35
        )

        self.create_stat_card(
            stats,
            "TOTAL",
            str(len(self.books)),
            "#e6ded0"
        )

        self.create_stat_card(
            stats,
            "FINISHED",
            str(self.count_status("Read")),
            "#d7e3dc"
        )

        self.create_stat_card(
            stats,
            "READING",
            str(self.count_status("Reading")),
            "#e2d8e8"
        )

        self.create_stat_card(
            stats,
            "TO READ",
            str(self.count_status("Want to Read")),
            "#eadfce"
        )

        # Reading progress
        box = tk.Frame(
            self.main,
            bg="#fffdf8"
        )
        box.pack(
            fill="x",
            padx=35,
            pady=30
        )

        finished = self.count_status("Read")
        total = len(self.books)

        percentage = (
            finished / total * 100
            if total > 0
            else 0
        )

        tk.Label(
            box,
            text="Reading Progress",
            font=("Georgia", 16, "bold"),
            bg="#fffdf8",
            fg="#263238"
        ).pack(
            anchor="w",
            padx=25,
            pady=(22, 10)
        )

        tk.Label(
            box,
            text=f"{percentage:.0f}% of your library finished",
            font=("Arial", 10),
            bg="#fffdf8",
            fg="#7b8587"
        ).pack(
            anchor="w",
            padx=25
        )

        progress = tk.Canvas(
            box,
            width=600,
            height=18,
            bg="#e9e4db",
            highlightthickness=0
        )
        progress.pack(
            anchor="w",
            padx=25,
            pady=(10, 25)
        )

        progress.create_rectangle(
            0,
            0,
            6 * percentage,
            18,
            fill="#52656b",
            outline=""
        )

    def count_status(self, status):

        return sum(
            1
            for book in self.books
            if book["status"] == status
        )

    # =========================
    # DELETE
    # =========================

    def delete_book(self, index):

        book = self.books[index]

        answer = messagebox.askyesno(
            "Remove Book",
            f'Remove "{book["title"]}" from your library?'
        )

        if answer:

            self.books.pop(index)
            self.show_books()


# =========================
# RUN
# =========================

root = tk.Tk()

app = PersonalLibrary(root)

root.mainloop()