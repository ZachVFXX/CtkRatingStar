# CtkRatingStar

A customizable star rating widget for CustomTkinter applications. This widget provides an intuitive and visually appealing way to implement rating functionality in your CustomTkinter projects.

![{318EAF2F-AE07-4A1A-91C1-E1E98727C51B}](https://github.com/user-attachments/assets/95bb8a5f-c907-4d1d-aaef-87c397a340dc)

## Features

- Customizable number of stars
- Smooth hover effects
- Current value display
- Optional title and rating label
- Easy integration with existing CustomTkinter applications

## Installation

```bash
pip install CTkRatingStar
```

## Usage

Here's a simple example of how to use the `CtkStarRating` widget:

```python
import customtkinter as ctk
from ctk_star_rating import CtkStarRating

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Create the star rating widget
        star_rating = CtkStarRating(
            self,
            number_of_stars=5,     # Number of stars to display
            current_value=3,       # Initial rating value
            title="Rating:",       # Optional title
            current_value_label="/5" # Optional value label
        )
        star_rating.pack(pady=10)
        
        # Get the current rating value
        value = star_rating.get_value()

if __name__ == "__main__":
    app = App()
    app.mainloop()
```

## Customization Options

The `CtkStarRating` widget accepts the following parameters:

- `number_of_stars` (int): Number of stars to display (default: 5)
- `current_value` (int): Initial rating value (default: 1)
- `title` (str, optional): Title text to display above the stars
- `current_value_label` (str, optional): Label to display after the current value

## Required Assets

The widget requires the following image assets in the `assets` directory:
- `full_star.png`: Filled star image
- `empty_star.png`: Empty star image
- `full_star_hover.png`: Filled star hover state
- `hover_star.png`: Empty star hover state

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- [ZachVFXX](https://github.com/ZachVFXX)

## Acknowledgments

- Built with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- Uses [Pillow](https://python-pillow.org/) for image handling
