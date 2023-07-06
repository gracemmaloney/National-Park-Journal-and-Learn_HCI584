
from tkinter import * # so we can use Tk() instead of Tkinter.Tk() ...
from tkinter import ttk
from tkinter import filedialog 
import tkinter.messagebox
import pandas as pd
from PIL import Image,ImageTk
import os
import datetime
from tkcalendar import *
import webbrowser

JOURNAL_DIR = "./Journal Entries"


class App(Frame):
    def __init__(self, master):     
        self.master = master # store link to master window, use as frame to put all other widgets into
        
        # Part 1) Tabular Journal (default) vs. Learn Windows Set Up
        self.notebook = ttk.Notebook(self.master, width=700, height=700)

        self.frame1 = Frame(self.notebook)
        self.frame2 = Frame(self.notebook)
        self.frame1.pack(padx=10, pady=10)
        self.frame2.pack(padx=10, pady=10)

        self.notebook.add(self.frame1, text="Journal")
        self.notebook.add(self.frame2, text="Learn")
        self.notebook.pack(padx=10, pady=10)

        # Initial instructions for user to review upon viewing each tab
        self.frame1_label = Label(self.frame1, text="To create a new journal entry, click the Create new journal entry button.")
        self.frame2_label = Label(self.frame2, text="To learn about a national park, select the appropriate national park from the dropdown menu.")
        self.frame1_label.pack(padx=10, pady=10, anchor=W)
        self.frame2_label.pack(padx=10, pady=10, anchor=W)

        # Create new journal button
        self.journal_button = Button(self.frame1, text="Create new journal entry", command=self.enter_new_journal_entry)
        self.journal_button.pack(padx=10, pady=10, anchor=W)

        # Existing entries label
        self.ext_entries_label = Label(self.frame1, text="Existing entries:")
        self.ext_entries_label.pack(padx=10, pady=5, anchor=W)

        # Listbox listing existing entries
        # CH made this single select mode so it's clear which entry has been selected when 2 x clicking
        self.entries_list = Listbox(self.frame1, width=50, selectmode=SINGLE)
        self.entries_list.bind("<Double-Button-1>", self.double_click_journal)  
        
        self.entries_list.pack(padx=10, pady=10, anchor=W)
        self.journal_entry_list = os.listdir(JOURNAL_DIR)
        for item in self.journal_entry_list:
            self.entries_list.insert(END, item)

        # Open a journal entry button
        self.open_journal_button = Button(self.frame1, text="Open a journal entry",  command=self.open_journal_entry) 
        self.open_journal_button.pack(padx=10, pady=5, anchor=W)

        # Drop down menu on Learn tab + read in excel file
        self.learn_dropdown_label = Label(self.frame2, text="Select a US National Park:")
        self.learn_dropdown_label.pack(padx=10, anchor=W)

        app_data = pd.read_excel("Database - Learn.xlsx")
        park_names = app_data["Name"]
        self.parks_list = list(park_names)
        self.natpark_learn_var = StringVar()
        self.learn_dropdown = OptionMenu(self.frame2, self.natpark_learn_var, *self.parks_list)
        self.learn_dropdown.pack(padx=10, pady=10, anchor=W)

        # Learn about this park button
        self.learn_button = Button(self.frame2, text="Learn about this park", command=self.new_learn_inquiry)
        self.learn_button.pack(padx=10, pady=5, anchor=W)

        # Frame that will be cleared below each time a user selects a park to learn about
        self.learn_info_frame=Frame(self.frame2) 
        self.learn_info_frame.pack(padx=10, pady=10, anchor=W)


    # Part 2 New Journal Entry Function
    def enter_new_journal_entry(self):
        self.journal_entry = Toplevel() # new window
        
        self.textframe=Frame(self.journal_entry)
        self.textframe.pack(padx=10, pady=10)
        
        # Instructions
        self.journal_label = Label(self.textframe, text="To complete a new journal entry and log the details of your national park experience, select the appropriate\nnational park from the dropdown menu and then record your memories in the text field. When finished, save\nyour entry by clicking the ‘save’ button.", justify='left')
        self.journal_label.pack(side=TOP , padx=10, pady=10)

        # Step-by-step instruction
        self.dropdown_label = Label(self.textframe, text="1. Select a US National Park:")
        self.dropdown_label.pack(padx=10, anchor=W)
        
        # Drop down menu on Journal window
        self.natpark_var = StringVar()
        self.natpark_dropdown = OptionMenu(self.textframe, self.natpark_var, *self.parks_list)
        self.natpark_dropdown.pack(padx=10, pady=10, anchor=W)

        # Step-by-step instruction
        self.text_label = Label(self.textframe, text="2. Enter the details of your visit:")
        self.text_label.pack(padx=10, anchor=W)

        # Text box for journal details
        self.text=Text(self.textframe, width=90, height=20, wrap=WORD)
        self.text.pack(padx=10, pady=10, anchor=W)

        # Step-by-step instruction
        self.image_upload_label = Label(self.textframe, text="3. Upload a picture from your visit:")
        self.image_upload_label.pack(padx=10, anchor=W)
        
        # Upload Image button
        self.image_button = Button(self.textframe, text="Upload image", command = self.upload_image)
        self.image_button.pack(padx=10, pady=10, anchor=W)

        # Step-by-step instruction
        self.rating_label = Label(self.textframe, text="4. Rate the selected National Park:")
        self.rating_label.pack(padx=10, anchor=W)

        # Drop down menu for rating
        self.rating_var = StringVar()
        self.rating_dropdown = OptionMenu(self.textframe, self.rating_var, "0", "1", "2", "3", "4", "5")
        self.rating_dropdown.pack(padx=10, pady=10, anchor=W)

        # Step-by-step instruction
        self.ratingtext_label = Label(self.textframe, text="5. Optionally, justify your rating:")
        self.ratingtext_label.pack(padx=10, anchor=W)

        # Text box for rating details
        self.rating_text=Text(self.textframe, width=90, height=10, wrap=WORD)
        self.rating_text.pack(padx=10, pady=10, anchor=W)

        # Save button
        self.journalentry_button = Button(self.textframe, text="Save", command=self.save_journal_entry)
        self.journalentry_button.pack(padx=10, pady=10)

        # Cancel button
        self.cancel_button = Button(self.textframe, text="Cancel", command=self.cancel_journal_entry)
        self.cancel_button.pack(padx=10, pady=10)
    
    # Part 3a Upload an Image - WIP
    def upload_image(self):
        self.upload_img_file = filedialog.askopenfilename(title="Select an image to upload", filetypes=[("Image Files", ".png .jpeg .jpg")]) # - potential issue
        image_open = Image.open(self.upload_img_file)
        image_resize = image_open.resize((300, 225), Image.LANCZOS)
        selected_pic = ImageTk.PhotoImage(image_resize)
        self.pic_label = Label(self.textframe, image=selected_pic)
        self.pic_label.image=selected_pic # for garbage collection - potential issue
        self.pic_label.pack(padx=10, pady=0, anchor=W)
    
    # Part 3b Save Journal Entry Function
    def save_journal_entry(self):
        #current_date = datetime.datetime.now()
        self.text_file = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Text File", ".txt")], initialdir=JOURNAL_DIR, initialfile=self.natpark_var.get())
        file_text = str("National Park Visited: " + self.natpark_var.get() + "\n" + "Details: " + self.text.get(1.0, END) + "\n" + "Rating: " + self.rating_var.get() + "\n" + "Rating Details: " + self.rating_text.get(1.0, END))
        self.text_file.write(file_text)
        self.text_file.close()
        self.journal_entry.destroy()
        self.entries_list.delete(0,END)
        self.journal_entry_list = os.listdir(JOURNAL_DIR)
        for item in self.journal_entry_list:
            self.entries_list.insert(END, item)
    
    # Part 3c Cancel Journal Entry Function
    def cancel_journal_entry(self):
        self.journal_entry.destroy()


    # Part 4a Open Journal Entry Function
    def open_journal_entry(self):
        #self.open_text_file.delete("1.0", END)

        # Select file to open
        self.journal_file = filedialog.askopenfilename(initialdir=JOURNAL_DIR, title="Open Journal Entry Text File")
        self.journal_file = open(self.journal_file, 'r')
        read_journal = self.journal_file.read()
        
        # New window for frame and text box
        self.open_journal_entry = Toplevel() # new window
        
        # frame for text file
        self.open_journal_frame=Frame(self.open_journal_entry)
        self.open_journal_frame.pack(padx=10, pady=10)   
        
        # Text box for text file to appear in when opened
        self.open_text_file = Text(self.open_journal_frame, width=90, height=20)
        self.open_text_file.pack(padx=10, pady=10)
       
        # Insert file contents
        self.open_text_file.insert(END, read_journal)
        self.journal_file.close()
        
        # Menu for opening and saving files
        self.file_menu = Menu(self.open_journal_entry)
        self.open_journal_entry.config(menu=self.file_menu)
        self.entry_menu = Menu(self.file_menu)
        self.file_menu.add_cascade(label="File", menu=self.entry_menu)
        self.entry_menu.add_command(label="Open", command=self.open_file)
        self.entry_menu.add_command(label="Save", command=self.save_file)

    # Part 4b Open File Function
    def open_file(self):
        self.open_text_file.delete("1.0", END)
        self.journal_file = filedialog.askopenfilename(initialdir=JOURNAL_DIR, title="Open Journal Entry Text File")
        self.journal_file = open(self.journal_file, 'r')
        read_journal = self.journal_file.read()
        self.open_text_file.insert(END, read_journal)
        self.journal_file.close()

    # Part 4c Save File Function
    def save_file(self):
        self.existing_filename = os.path.basename(self.journal_file.name)
        self.journal_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir=JOURNAL_DIR, initialfile=self.existing_filename, title="Save Journal Entry Text File")
        self.journal_file = open(self.journal_file, 'w')
        self.journal_file.write(self.open_text_file.get("1.0", END))
        self.journal_file.close()

    # Part 4d Double Click Opening Journal Entry
    def double_click_journal(self, event):
        '''method to show how to get the clicked on entry in a listbox'''

        # New window for frame and text box
        self.click_journal_entry = Toplevel() # new window
        
        # frame for text file
        self.click_journal_frame=Frame(self.click_journal_entry)
        self.click_journal_frame.pack(padx=10, pady=10)   
        
        # Text box for text file to appear in when opened
        self.click_text_file = Text(self.click_journal_frame, width=90, height=20)
        self.click_text_file.pack(padx=10, pady=10)

        self.click_journal_file = self.entries_list.get(ACTIVE)
        folder_path = JOURNAL_DIR
        file_path = os.path.join(folder_path, self.click_journal_file)
        file_clicked = open(file_path, 'r')
        read_journal_clicked = file_clicked.read()
        self.click_text_file.insert(END, read_journal_clicked)
        file_clicked.close()

        # Menu for opening and saving files
        self.option_menu = Menu(self.click_journal_entry)
        self.click_journal_entry.config(menu=self.option_menu)
        self.entry_menu = Menu(self.option_menu)
        self.option_menu.add_cascade(label="File", menu=self.entry_menu)
        self.entry_menu.add_command(label="Open", command=self.open_clicked_file)
        self.entry_menu.add_command(label="Save", command=self.save_clicked_file)

    # Part 4e Open File Function for Double Click Method
    def open_clicked_file(self):
        self.click_text_file.delete("1.0", END)
        self.click_journal_file = filedialog.askopenfilename(initialdir=JOURNAL_DIR, title="Open Journal Entry Text File")
        self.click_journal_file = open(self.click_journal_file, 'r')
        read_journal = self.click_journal_file.read()
        self.click_text_file.insert(END, read_journal)
        self.click_journal_file.close()

    # Part 4f Save File Function for Double Click Method
    def save_clicked_file(self):
        self.click_existing_filename = os.path.basename(self.click_journal_file)
        self.click_journal_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir=JOURNAL_DIR, initialfile=self.click_existing_filename, title="Save Journal Entry Text File")
        self.click_journal_file = open(self.click_journal_file, 'w')
        self.click_journal_file.write(self.click_text_file.get("1.0", END))
        self.click_journal_file.close()
        
    
    # Part 5 New Learn Inquiry Function
    def new_learn_inquiry(self):
        # Destroy frame created above to clear contents of the frame
        self.learn_info_frame.destroy() 
        
        # Recreate frame to show widgets
        self.learn_info_frame=Frame(self.frame2) 
        self.learn_info_frame.pack(padx=10, pady=10, anchor=W)
        
        # Read in excel file and get selected item from drop down menu
        learn_excel = pd.read_excel("Database - Learn.xlsx")
        park_from_list = self.natpark_learn_var.get()

        park_info = learn_excel[learn_excel['Name'] == park_from_list]
        park_info_list = park_info.values.tolist() 
        
        # Location
        self.location_label = Label(self.learn_info_frame, text=("Location: "+park_info_list[0][1]))
        self.location_label.pack(padx=10, pady=5, anchor=W)
        self.location_label.configure(wraplength=700, justify=LEFT)

        # Image
        img_open = Image.open(park_info_list[0][2])
        img_resize = img_open.resize((300, 225), Image.LANCZOS)
        park_pic = ImageTk.PhotoImage(img_resize)
        self.image_label = Label(self.learn_info_frame, image=park_pic)
        self.image_label.image = park_pic
        self.image_label.pack(padx=10, pady=5, anchor=W)

        # Description
        self.desc_label = Label(self.learn_info_frame, text="Description: "+park_info_list[0][7])
        self.desc_label.pack(padx=10, pady=5, anchor=W)
        self.desc_label.configure(wraplength=600, justify=LEFT)

        # Link
        self.link_label = Label(self.learn_info_frame, text="National Park Service Official Web Page", fg="blue", cursor="hand2", font=('TkDefaultFont', 13, 'underline')) # Link: "+park_info_list[0][3])
        self.link_label.pack(padx=10, pady=10, anchor=W)
        self.link_label.bind("<Button-1>", lambda e: webbrowser.open_new(park_info_list[0][3]))
        
        # Cost per vehicle
        self.costv_label = Label(self.learn_info_frame, text="Cost of Entry Per Vehicle: $"+str(park_info_list[0][4]))
        self.costv_label.pack(padx=10, anchor=W)
        
        # Cost per person
        self.costp_label = Label(self.learn_info_frame, text="Cost of Entry Per Person: $"+str(park_info_list[0][5]))
        self.costp_label.pack(padx=10, anchor=W)

        # Cost per motorcyle
        self.costm_label = Label(self.learn_info_frame, text="Cost of Entry Per Motorcycle: $"+str(park_info_list[0][6]))
        self.costm_label.pack(padx=10, anchor=W)
        
       
        
# TO DO LIST
# work on proposed learn tab enhancements (Thursday)
# ask CH for help with Part 3a (Friday)
# add doc strings for each function


master = Tk()  # create a Tk window called master
master.title("National Park Journal for Outdoor Enthusiasts TkInter GUI - WIP")
myapp = App(master) # create App object within master (Tk) windowmaster.mainloop() # draw master window, react to events only
master.mainloop() # draw master window, react to events 
print("Done")


