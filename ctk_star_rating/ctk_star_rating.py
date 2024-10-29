import customtkinter as ctk
from PIL import Image

FULL_STAR = ctk.CTkImage(Image.open("assets/full_star.png"), size=(24, 24))
EMPTY_STAR = ctk.CTkImage(Image.open("assets/empty_star.png"), size=(24, 24))
FULL_HOVER_STAR = ctk.CTkImage(Image.open("assets/full_star_hover.png"), size=(24, 24))
HOVER_STAR = ctk.CTkImage(Image.open("assets/hover_star.png"), size=(24, 24))


class CtkStar(ctk.CTkLabel):
    def __init__(self, master, index):
        super().__init__(master, text="")
        self.index = index
        self.configure(image=EMPTY_STAR)
        self.state = "EMPTY_STAR"

    def set_full(self):
        self.configure(image=FULL_STAR)
        self.state = "FULL_STAR"

    def set_empty(self):
        self.configure(image=EMPTY_STAR)
        self.state = "EMPTY_STAR"

    def set_full_hover(self):
        self.configure(image=FULL_HOVER_STAR)
        self.state = "FULL_HOVER_STAR"

    def set_hover(self):
        self.configure(image=HOVER_STAR)
        self.state = "HOVER_STAR"


class CtkStarRating(ctk.CTkFrame):
    def __init__(
        self,
        master,
        number_of_stars: int = 5,
        current_value: int = 1,
        title: str | None = None,
        current_value_label: str | None = None,
    ):
        super().__init__(master)
        self.number_of_stars = number_of_stars
        self.current_value = current_value
        self.stars = []
        self.title = title
        self.current_value_label = current_value_label

        if self.title is not None and self.title != "":
            self.title_label = ctk.CTkLabel(self, text=self.title)
            self.title_label.grid(
                row=0,
                column=0,
                padx=4,
                pady=(4, 0),
                sticky="W",
                columnspan=number_of_stars,
            )
            self.grid_rowconfigure((0, 1), weight=1)

        if self.current_value_label is not None and self.current_value_label != "":
            self.value_label = ctk.CTkLabel(
                self, text=f"{self.current_value} {self.current_value_label}"
            )
            self.value_label.grid(
                row=0,
                padx=4,
                pady=(4, 0),
                sticky="E",
                columnspan=number_of_stars,
            )

        self.create_stars()
        self.setup_bindings()
        self.update_stars()

    def create_stars(self):
        for i in range(self.number_of_stars):
            star = CtkStar(self, i)
            if self.title is not None and self.title != "":
                star.grid(row=1, column=i, padx=4, pady=(0, 4))
            else:
                star.grid(row=0, column=i, padx=4, pady=4)
            self.rowconfigure(i, weight=1)
            self.stars.append(star)

    def setup_bindings(self):
        for star in self.stars:
            star.bind("<Enter>", self.on_enter)
            star.bind("<Leave>", self.on_leave)
            star.bind("<Button-1>", self.on_click)

    def update_stars(self):
        for i, star in enumerate(self.stars):
            if i < self.current_value:
                star.set_full()
            else:
                star.set_empty()

    def on_enter(self, event):
        widget = event.widget.master
        hover_index = widget.index

        for i, star in enumerate(self.stars):
            if i <= hover_index:
                if star.state == "EMPTY_STAR":
                    star.set_hover()
                else:
                    star.set_full_hover()
            else:
                if star.state == "FULL_STAR":
                    star.set_full()
                else:
                    star.set_empty()

    def on_leave(self, event):
        self.update_stars()

    def on_click(self, event):
        widget = event.widget.master
        clicked_index = widget.index

        if clicked_index < self.current_value - 1:
            self.current_value = clicked_index + 1
        else:
            self.current_value = clicked_index + 1
        if self.value_label is not None and self.value_label != "":
            self.value_label.configure(
                text=f"{self.current_value} {self.current_value_label}"
            )
        self.update_stars()

    def get_value(self):
        return self.current_value


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("CtkStarRating")
        self.geometry("400x200")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        central_frame = ctk.CTkFrame(self)
        central_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        central_frame.grid_rowconfigure(0, weight=1)
        central_frame.grid_columnconfigure(0, weight=1)

        self.star_rating = CtkStarRating(
            central_frame,
            number_of_stars=5,
            current_value=3,
            title="Rating:",
            current_value_label="/5",
        )
        self.star_rating.grid(row=0, column=0, padx=10, pady=10)

        self.value_label = ctk.CTkLabel(
            central_frame, text=f"Valeur: {self.star_rating.get_value()}"
        )
        self.value_label.grid(row=1, column=0, pady=10)

        def update_label(event):
            self.value_label.configure(text=f"Valeur: {self.star_rating.get_value()}")

        for star in self.star_rating.stars:
            star.bind("<Button-1>", lambda e: update_label(e))


if __name__ == "__main__":
    app = App()
    app.mainloop()
