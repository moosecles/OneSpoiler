import tkinter as tk


def display(chapters):
    window = tk.Tk()
    window.title("Chapter Information")

    # Create a frame to hold the title label and the text widget
    frame = tk.Frame(window)
    frame.pack()

    # Create a label to display the title
    title_label = tk.Label(frame, text=("Chapter " + str(next(iter(chapters)))))
    title_label.pack()

    # Create a scrollbar to use with the text widget
    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Create a text widget to display the pages
    text = tk.Text(frame, wrap=tk.WORD, yscrollcommand=scrollbar.set)
    text.pack()
    scrollbar.config(command=text.yview)

    # Populate the text widget with the pages from the dictionary
    for chapter, pages in chapters.items():
        text.insert(tk.END, f"Chapter {chapter}\n")
        for page in pages:
            text.insert(tk.END, f"{page}\n")

    # Run the Tkinter event loop
    window.mainloop()