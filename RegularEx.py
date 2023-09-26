import tkinter as tk
import tkinter.ttk as ttk
import re #Import Regular Expression
from PIL import Image, ImageTk  # Import PIL

# Function to find email addresses in the text
def find_emails():
    email_pattern = r'\S+@\S+'
    emails = re.findall(email_pattern, text_input.get(1.0, tk.END))
    result_display.delete(1.0, tk.END)
    for email in emails:
        result_display.insert(tk.END, f"Email: {email}\n")

# Function to find dates and subject lines
def find_dates_subjects():
    date_subject_pattern = r'Subject: (.*?)\nDate: (.*?)\n'
    matches = re.findall(date_subject_pattern, text_input.get(1.0, tk.END))
    result_display.delete(1.0, tk.END)
    for match in matches:
        subject, date = match
        result_display.insert(tk.END, f"Subject: {subject}\nDate: {date}\n")

# Function to find URLs and hyperlinks
def find_urls():
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    urls = re.findall(url_pattern, text_input.get(1.0, tk.END))
    result_display.delete(1.0, tk.END)
    for url in urls:
        result_display.insert(tk.END, f"URL: {url}\n")

# Function to find specific keywords
def find_keywords():
    keywords = ["innovative", "limited-time offer" ]
    result_display.delete(1.0, tk.END)
    text = text_input.get(1.0, tk.END).lower()
    for keyword in keywords:
        if keyword in text:
            result_display.insert(tk.END, f"Keyword: {keyword}\n")

# Function to extract the "Dear all" message body
def extract_message_body():
    text = text_input.get(1.0, tk.END)
    start_index = text.find("Dear all")
    if start_index != -1:
        message_body = text[start_index:]
        result_display.delete(1.0, tk.END)
        result_display.insert(tk.END, f"Message Body:\n{message_body}")



# Create the main window
root = tk.Tk()
root.title("Email Information Extractor")

# Icon of window
icon = tk.PhotoImage(file='Email.png')
root.iconphoto(False, icon)

root.geometry('1250x700')  # Window size
root.configure(background="#20262E")

# Load and display the background image
background_image = Image.open("bg.png")
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)

# Create input field
text_input = tk.Text(root, height=17, width=150)
text_input.grid(row=0, column=0, columnspan=4, padx=15, pady=(10,10))


# Custom buttons for tasks
style = ttk.Style()
style.configure("Bold.TButton", font=('Helvetica', 12, 'bold'))
style.map("Bold.TButton",
          foreground=[('pressed', '#FF6969'), ('active', 'black')],
          background=[('pressed', '!disabled', 'yellow'), ('active', 'red')])

find_urls_button = ttk.Button(root, text="Find URLs", command=find_urls, style="Bold.TButton")
find_urls_button.grid(row=1, column=0, pady=(10,10))

find_emails_button = ttk.Button(root, text="Find Emails", command=find_emails, style="Bold.TButton")
find_emails_button.grid(row=1, column=1, pady=(10,10))

find_keywords_button = ttk.Button(root, text="Find Keywords", command=find_keywords, style="Bold.TButton")
find_keywords_button.grid(row=1, column=2, pady=(10,10))

find_dates_subjects_button = ttk.Button(root, text="Find Dates & Subjects", command=find_dates_subjects, style="Bold.TButton")
find_dates_subjects_button.grid(row=1, column=3, pady=(10,10))

extract_message_body_button = ttk.Button(root, text="Extract Message Body", command=extract_message_body, style="Bold.TButton")
extract_message_body_button.grid(row=2, column=2, pady=(10, 10))

# Create result display area
result_display = tk.Text(root, height=12, width=100, bg="#D8D9DA", fg="#0E21A0", font=("Bold", 15))
result_display.grid(row=3, column=0, columnspan=4, padx=10, pady=(10,20),)

# Start the main loop
root.mainloop()
