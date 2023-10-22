from pathlib import Path
from PIL import Image, ImageTk
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,ttk
from pathlib import Path

from prompt_maker import get_outfit_recommendation, collect_user_profile, test_user_profile
from image_generator import generate_images, open_latest_images, get_latest_directory


OUTPUT_PATH = Path("D:\PythonDevelopment\EasyFit")
IMAGES_PATH = OUTPUT_PATH / "images"
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"

image_references = []
image_coordinates = []
def load_image_with_pil(canvas, image_id, image_path, x, y):
    
    try:
        # Delete the previous image (if it exists)
        if image_id is not None:
            canvas.delete(image_id)

        # Create the new image
        pil_image = Image.open(image_path)
        width, height = pil_image.size
        width = int(width / 3)
        height = int(height / 3)
        pil_image = pil_image.resize((width, height), Image.LANCZOS)
        tk_image = ImageTk.PhotoImage(pil_image)
        image_id = canvas.create_image(x, y, image=tk_image)

        # Keep a reference to the new image to prevent garbage collection
        canvas.image = tk_image
        print("Image displayed: ", image_path, "with id: ", image_id, " at coordinates: ", x, y, " with width and height of: ", width, height)

        
    except Exception as e:
        print(f"An error occurred: {e}")


def load_images(event):
    # Show the loading popup
    show_loading_popup(window)
    window.after(3000, load_imagesDelay)
def load_imagesDelay():
    # Update the images
    latest_dir = get_latest_directory(IMAGES_PATH)
    image_paths = [
        Path(latest_dir) / "image_1.png",
        Path(latest_dir) / "image_2.png",
        Path(latest_dir) / "image_3.png"
    ]


    for (image_id, image_path), (x, y) in zip(zip(image_references, image_paths), image_coordinates):
        load_image_with_pil(canvas, image_id, image_path, x, y)
        print("Image loaded: ", image_path, "with id: ", image_id, " at coordinates: ", x, y)
            
#LOADING POPUP
from tkinter import Toplevel, Label
def show_loading_popup(parent_window):
    popup = Toplevel(parent_window)
    popup.title("Loading")
    
    # Window dimensions
    width = 200
    height = 100
    
    # Parent window dimensions and position
    parent_x = parent_window.winfo_x()
    parent_y = parent_window.winfo_y()
    parent_width = parent_window.winfo_width()
    parent_height = parent_window.winfo_height()
    
    # Calculate position of popup window (to center it within parent window)
    x = parent_x + (parent_width // 2) - (width // 2)
    y = parent_y + (parent_height // 2) - (height // 2)
    
    # Set the dimensions and position
    popup.geometry(f"{width}x{height}+{x}+{y}")

    label = Label(popup, text="Loading...")
    label.pack()

    # Close the popup after 3000 milliseconds (3 seconds)
    popup.after(3000, popup.destroy)








def on_mousewheel(event):
    if event.num == 5 or event.delta == -120:
        direction = 1
    else:
        direction = -1
    canvas.yview_scroll(direction, "units")



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("375x700")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 3843,
    width = 375,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.bind("<MouseWheel>", on_mousewheel)
#scrollbar 
# Initialize the scrollbar
scrollbar = ttk.Scrollbar(window, orient='vertical', command=canvas.yview)
scrollbar.pack(side="right", fill="y")  # Using pack layout manager for this example

# Set the canvas y-scrolling to respond to the scrollbar
canvas.config(yscrollcommand=scrollbar.set)


canvas.place(x = 0, y = 0)
canvas.create_text(
    116.0,
    26.0,
    anchor="nw",
    text="Ezzy Fit",
    fill="#000000",
    font=("TenorSans", 20 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    45.0,
    40.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    334.0,
    40.0,
    image=image_image_2
)

canvas.create_rectangle(
    -1.0,
    75.0,
    375.0013427734375,
    76.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    -1.0,
    1601.0,
    375.0013427734375,
    1602.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    -1.0,
    2790.0,
    375.0013427734375,
    2791.0,
    fill="#000000",
    outline="")

canvas.create_text(
    13.0,
    93.0,
    anchor="nw",
    text="Your Virtual Closet ",
    fill="#000000",
    font=("TenorSans", 20 * -1)
)

canvas.create_text(
    4.0,
    1629.0,
    anchor="nw",
    text="Ezzy Personalize Recomendation\n",
    fill="#000000",
    font=("TenorSans", 20 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    269.0,
    224.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    279.0,
    434.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    92.0,
    226.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    98.0,
    433.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    104.0,
    656.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    282.0,
    657.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    97.0,
    851.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    105.0,
    1048.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    270.0,
    1048.0,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    277.0,
    850.0,
    image=image_image_12
)

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    95.0,
    1240.0,
    image=image_image_13
)

image_image_14 = PhotoImage(
    file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(
    275.0,
    1237.0,
    image=image_image_14
)

canvas.create_text(
    15.0,
    293.0,
    anchor="nw",
    text="Suede Salmon Jacket  ",
    fill="#000000",
    font=("TenorSans", 14 * -1)
)

canvas.create_text(
    200.0,
    293.0,
    anchor="nw",
    text="Cotton White Shirt  ",
    fill="#000000",
    font=("TenorSans", 14 * -1)
)

canvas.create_text(
    206.0,
    535.0,
    anchor="nw",
    text="Silk Pink Dress  ",
    fill="#000000",
    font=("TenorSans", 14 * -1)
)

canvas.create_text(
    200.0,
    734.0,
    anchor="nw",
    text="Polyester Blue whit white Dots Shorts ",
    fill="#000000",
    font=("TenorSans", 14 * -1)
)

canvas.create_text(
    198.0,
    938.0,
    anchor="nw",
    text="Leather Pink Small Bag  ",
    fill="#000000",
    font=("TenorSans", 14 * -1)
)

canvas.create_text(
    206.0,
    1134.0,
    anchor="nw",
    text="White heels ",
    fill="#000000",
    font=("TenorSans", 14 * -1)
)

canvas.create_text(
    13.0,
    1304.0,
    anchor="nw",
    text="Blue Espadrilles",
    fill="#000000",
    font=("TenorSans", 14 * -1)
)

canvas.create_text(
    13.0,
    1542.0,
    anchor="nw",
    text="White Flowered Bikini",
    fill="#000000",
    font=("TenorSans", 14 * -1)
)

canvas.create_text(
    195.0,
    1542.0,
    anchor="nw",
    text="Green Flowered Bikini",
    fill="#000000",
    font=("TenorSans", 14 * -1)
)

canvas.create_text(
    192.0,
    1304.0,
    anchor="nw",
    text="Denim Blue Shorts",
    fill="#000000",
    font=("TenorSans", 14 * -1)
)

canvas.create_text(
    19.0,
    1134.0,
    anchor="nw",
    text="Leather Green Small Bag  ",
    fill="#000000",
    font=("TenorSans", 14 * -1)
)

canvas.create_text(
    24.0,
    535.0,
    anchor="nw",
    text="Velvet Burgundy Dress  ",
    fill="#000000",
    font=("TenorSans", 14 * -1)
)

canvas.create_text(
    23.0,
    734.0,
    anchor="nw",
    text="Denim Blue Skinny-Jeans  ",
    fill="#000000",
    font=("TenorSans", 14 * -1)
)

canvas.create_text(
    17.0,
    938.0,
    anchor="nw",
    text="Polyester Blue whit \nRed Dots Shirt",
    fill="#000000",
    font=("TenorSans", 14 * -1)
)

image_image_15 = PhotoImage(
    file=relative_to_assets("image_15.png"))
image_15 = canvas.create_image(
    95.0,
    1442.0,
    image=image_image_15
)

canvas.create_text(
    30.0,
    1669.0,
    anchor="nw",
    text="Generate Ai Outfit Recommendation based on your Scanned Closet  ",
    fill="#000000",
    font=("TenorSans", 13 * -1)
)

canvas.create_text(
    87.0,
    2815.0,
    anchor="nw",
    text="Ezzy Events",
    fill="#000000",
    font=("TenorSans", 20 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    187.5,
    2938.5,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=31.0,
    y=2900.0,
    width=313.0,
    height=75.0
)

canvas.create_text(
    31.0,
    2850.0,
    anchor="nw",
    text="Ai Outfit Recommendations  based on Upcoming events",
    fill="#000000",
    font=("TenorSans", 13 * -1)
)

image_image_16 = PhotoImage(
    file=relative_to_assets("image_16.png"))
image_16 = canvas.create_image(
    182.0,
    1962.0,
    image=image_image_16
)

image_references.append(image_16)
image_coordinates.append((182.0, 1000.0))

image_image_17 = PhotoImage(
    file=relative_to_assets("image_17.png"))
image_17 = canvas.create_image(
    182.0,
    2285.0,
    image=image_image_17
)

image_references.append(image_17)
image_coordinates.append((183.0, 2400.0))


image_image_18 = PhotoImage(
    file=relative_to_assets("image_18.png"))
image_18 = canvas.create_image(
    183.0,
    3605.0,
    image=image_image_18
)


image_references.append(image_18)
image_coordinates.append((183.0, 2000.0))

image_image_19 = PhotoImage(
    file=relative_to_assets("image_19.png"))
image_19 = canvas.create_image(
    182.0,
    2608.0,
    image=image_image_19
)

image_image_20 = PhotoImage(
    file=relative_to_assets("image_20.png"))
image_20 = canvas.create_image(
    183.0,
    3241.0,
    image=image_image_20
)

image_image_21 = PhotoImage(
    file=relative_to_assets("image_21.png"))
image_21 = canvas.create_image(
    276.0,
    1442.0,
    image=image_image_21
)

canvas.create_text(
    39.0,
    2908.0,
    anchor="nw",
text="I am having a semi-formal wedding in Cancun in one \n week. Based on my closet, please provide me\n with some recommendations and suggestions\n on what to wear.",
    fill="#000000",
    font=("TenorSans", 13 * -1)
)

canvas.create_text(
    111.0,
    1745.0,
    anchor="nw",
    text="Generate1",
    tags="button1_tag",
    fill="#000000",
    font=("TenorSans", 20 * -1)
)
# Bind the tag to the function
canvas.tag_bind("button1_tag", "<Button-1>", load_images)

canvas.create_text(
    114.0,
    3018.0,
    anchor="nw",
    text="Generate",
    fill="#000000",
    font=("TenorSans", 20 * -1)
)
window.resizable(False, False)
window.mainloop()