import tkinter as tk
import tkinter.ttk as ttk
import re
from PIL import Image, ImageTk

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
root.configure(background="#303030")  # Set a dark gray background color

# Create input field
text_input = tk.Text(root, height=17, width=150)
text_input.grid(row=0, column=0, columnspan=5, padx=15, pady=(10, 10))

# Create a frame to contain the label with padding
task_frame = ttk.Frame(root)
task_frame.grid(row=1, column=0, columnspan=5, padx=15, pady=(10, 10))

# Create a label for the task selection inside the frame
task_label = ttk.Label(task_frame, text="Choose Your Task", font=('Helvetica', 14), style="Bold.TButton", foreground="#64CCC5")
task_label.pack(padx=10, pady=5)

# Custom buttons for tasks
style = ttk.Style()
style.configure("Bold.TButton", font=('Helvetica', 12, 'bold'))
style.map("Bold.TButton",
          foreground=[('pressed', '#FF6969'), ('active', 'black')],
          background=[('pressed', '!disabled', 'yellow'), ('active', 'red')])

find_urls_button = ttk.Button(root, text="Find URLs", command=find_urls, style="Bold.TButton")
find_urls_button.grid(row=2, column=0, padx=(10, 0), pady=(10, 10))

find_emails_button = ttk.Button(root, text="Find Emails", command=find_emails, style="Bold.TButton")
find_emails_button.grid(row=2, column=1, padx=10, pady=(10, 10))

find_keywords_button = ttk.Button(root, text="Find Keywords", command=find_keywords, style="Bold.TButton")
find_keywords_button.grid(row=2, column=2, padx=10, pady=(10, 10))

find_dates_subjects_button = ttk.Button(root, text="Find Dates & Subjects", command=find_dates_subjects, style="Bold.TButton")
find_dates_subjects_button.grid(row=2, column=3, padx=10, pady=(10, 10))

extract_message_body_button = ttk.Button(root, text="Extract Message Body", command=extract_message_body, style="Bold.TButton")
extract_message_body_button.grid(row=2, column=4, padx=(0, 10), pady=(10, 10))

# Create result display area
result_display = tk.Text(root, height=12, width=100, bg="#D8D9DA", fg="#1AACAC", font=("Bold", 15))
result_display.grid(row=3, column=0, columnspan=5, padx=10, pady=(10, 20))

# Start the main loop
root.mainloop()
