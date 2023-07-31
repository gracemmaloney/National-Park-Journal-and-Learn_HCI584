
from tkinter import *
from tkinter import ttk
from tkinter import filedialog 
import pandas as pd
from PIL import Image,ImageTk
import os
import webbrowser
#from docx import Document
#from docx.shared import Inches

JOURNAL_DIR = "./Journal Entries" # directory folder for journal entries to be saved in
PHOTOS_DIR = "./Journal Photos" # directory folder for images to be saved in for image display on Journal tab


class App(Frame):
    def __init__(self, master):     
        '''main application window setup for journal and learn tabs and their content'''
        self.master = master # store link to master window, use as frame to put all other widgets into
        
        # Part 1a Tabular Journal (Default) vs. Learn Notebook Windows Set Up
        self.notebook = ttk.Notebook(self.master, width=850, height=800)

        # Frame widgets for notebook tabs
        self.frame1 = Frame(self.notebook)
        self.frame2 = Frame(self.notebook)
        self.frame1.pack(padx=10, pady=10)
        self.frame2.pack(padx=10, pady=10)

        # Notebook tabs
        self.notebook.add(self.frame1, text="Journal")
        self.notebook.add(self.frame2, text="Learn")
        self.notebook.pack(padx=10, pady=10)

        # Label widgets with initial instructions for user to review upon viewing the Journal and Learn tabs
        self.frame1_label = Label(self.frame1, text="To create a new journal entry, click the Create new journal entry button below. If ou want to insert an image, place it into the Journal Photos folder now.")
        self.frame2_label = Label(self.frame2, text="To learn about a US National Park, select the appropriate National Park from the dropdown menu.")
        self.frame1_label.pack(padx=10, pady=(10,5), anchor=W)
        self.frame2_label.pack(padx=10, pady=(10), anchor=W)

        # Create new journal entry button widget
        self.journal_button = Button(self.frame1, text="Create new journal entry", command=self.enter_new_journal_entry)
        self.journal_button.pack(padx=10, pady=(0,5), anchor=W)

        # Existing entries label widget
        self.ext_entries_label = Label(self.frame1, text="To view an existing journal entry, click on the Open a journal entry button or double click on an entry from the list below.")
        self.ext_entries_label.pack(padx=10, pady=(15,5), anchor=W)

        # Listbox widget for listing existing entries
        self.entries_list = Listbox(self.frame1, width=50, height=10, selectmode=SINGLE)
        self.entries_list.bind("<Double-Button-1>", self.double_click_journal)

        # Open a journal entry button widget
        self.open_journal_button = Button(self.frame1, text="Open a journal entry",  command=self.open_journal_entry) 
        self.open_journal_button.pack(padx=10, pady=0, anchor=W)
        
        # Existing entries inserted into listbox
        self.entries_list.pack(padx=15, pady=10, anchor=W)
        self.journal_entry_list = os.listdir(JOURNAL_DIR)
        for item in self.journal_entry_list: # looping over items in the journal entries folder
            self.entries_list.insert(END, item)

        self.click_journal_file = "" # global
        
        # Dropdown (option menu) menu widget on Learn tab + read in the excel file
        app_data = pd.read_excel("Database - Learn.xlsx") # excel file
        park_names = app_data["Name"] # just need park names from Name column
        self.parks_list = list(park_names)
        self.natpark_learn_var = StringVar()
        self.natpark_learn_var.set("Select a National Park") # default CTA shown before a national park is selected from the dropdown menu
        self.learn_dropdown = OptionMenu(self.frame2, self.natpark_learn_var, *self.parks_list, command=self.new_learn_inquiry) # dropdown menu
        self.learn_dropdown.pack(padx=15, pady=(0,5), anchor=W)

        # Frame widget that will be cleared below each time a user selects a national park to learn about from the dropdown menu
        self.learn_info_frame=Frame(self.frame2) 
        self.learn_info_frame.pack(padx=10, pady=10, anchor=W)

        # Label widget with image display CTA
        #self.pic_CTA_label = Label(self.frame1, text="Have some pictures from your visits to US National Parks? Add them to the Journal Photos folder to see them below!")
        #self.pic_CTA_label.pack(padx=10, pady=(15,0), anchor=W)
        

    def scroll_forward(self):
        '''method for scrolling through image display viewer using the forward button'''
        self.current_pic += 1
        if self.current_pic == len(self.pic_list):
            self.current_pic = 0
        self.pic_display_label.configure(image=self.pic_list[self.current_pic])

        
    # Part 1c Image Scroll Backward Button Function 
    def scroll_backward(self):
        self.current_pic -= 1
        if self.current_pic < 0:
            self.current_pic = len(self.pic_list) -1
        self.pic_display_label.configure(image=self.pic_list[self.current_pic])



       
    # Part 2a New Journal Entry Function
    def enter_new_journal_entry(self):
        '''method for creating a new journal entry'''
        self.journal_entry = Toplevel() # new window

      # ---------------------------------------------------------------------------------------------------------------------------------
      # SCROLLBAR WIDGETS
      # First frame widget
        self.textframe=Frame(self.journal_entry) 
        self.textframe.pack(fill=BOTH, expand=1)

      # Canvas widget
        self.journal_canvas = Canvas(self.textframe, height=800, width=700)
        self.journal_canvas.pack(side=LEFT, fill=BOTH, expand=1)

      # Scrollbar widget
        self.journal_scrollbar = Scrollbar(self.textframe, orient=VERTICAL, command=self.journal_canvas.yview)
        self.journal_scrollbar.pack(side=RIGHT, fill=Y)

      # Configure the canvas with the scrollbar
        self.journal_canvas.configure(yscrollcommand=self.journal_scrollbar.set)
        self.journal_canvas.bind('<Configure>', lambda e: self.journal_canvas.configure(scrollregion=self.journal_canvas.bbox("all")))

      # Second frame widget
        self.second_frame = Frame(self.journal_canvas) # widgets go here

      # Add second frame widget to a window in canvas widget
        self.journal_canvas.create_window((0,0), window=self.second_frame, anchor="nw")
      # ---------------------------------------------------------------------------------------------------------------------------------
        
        # Label widget with instructions for completing a new journal entry
        self.journal_label = Label(self.second_frame, text="To complete a new journal entry and log the details of your national park experience, select the appropriate\nnational park from the dropdown menu and then record your memories in the text field. When finished, save\nyour entry by clicking the ‘Save’ button.", justify='left')
        self.journal_label.pack(side=TOP , padx=10, pady=10)

        # Label widget with step-by-step instruction - step 1
        self.dropdown_label = Label(self.second_frame, text="1. Select a US National Park:")
        self.dropdown_label.pack(padx=10, anchor=W)
        
        # OptionMenu widget for drop down menu on new journal entry window
        self.natpark_var = StringVar()
        self.natpark_dropdown = OptionMenu(self.second_frame, self.natpark_var, *self.parks_list)
        self.natpark_dropdown.pack(padx=10, pady=10, anchor=W)

        # Label widget with step-by-step instruction - step 2
        self.text_label = Label(self.second_frame, text="2. Enter the details of your visit:")
        self.text_label.pack(padx=10, anchor=W)

        # Text box widget for entering journal details
        self.text=Text(self.second_frame, width=90, height=10, wrap=WORD)
        self.text.pack(padx=10, pady=10, anchor=W)

        # Label widget with step-by-step instruction - step 3
        self.image_upload_label = Label(self.second_frame, text="3. You can leave this blank, or insert an image from your Journal Photos folder.\n Use the Forward and Back buttons to scroll through the available images")
        self.image_upload_label.pack(padx=10, anchor=W)
        
 
        # read image from photos 
        #global pic_list #WTH??? Why global? just use self
        self.pic_list = []
        files = os.listdir(PHOTOS_DIR) # images in journal photos folder
        self.pic_filename_list = sorted(files, reverse=True, key=lambda f: os.path.getmtime(PHOTOS_DIR+"/"+f))
        for pic in self.pic_filename_list:
            pics_path = os.path.join(PHOTOS_DIR, pic)
            with Image.open(pics_path) as picture:
                picture.thumbnail((300,225))
                displayed_pic = ImageTk.PhotoImage(picture)
                self.pic_list.append(displayed_pic)
        self.current_pic = -1 # so that clicking on forward gives us index 0 i.e. newest pic
        
        # Label widget to display images
        self.pic_display_label = Label(self.second_frame, text="No image used")
        self.pic_display_label.pack(padx=10, pady=(15,0), anchor=W)

        # Navigation button widgets
        self.fwdbck_frame = Frame(self.second_frame)
        self.fwdbck_frame.pack(padx=10, pady=(0,2.5), anchor=W)
        self.back_button = Button(self.fwdbck_frame, text="Back", command=self.scroll_backward)
        self.forward_button = Button(self.fwdbck_frame, text="Forward", command=self.scroll_forward)
        self.forward_button.pack(padx=10, pady=(0,2.5), anchor=W, side=LEFT)
        self.back_button.pack(padx=10, pady=(0,2.5), anchor=W,  side=LEFT) 
  
        # Label widget with step-by-step instruction - step 4
        self.rating_label = Label(self.second_frame, text="4. Rate the selected US National Park:")
        self.rating_label.pack(padx=10, anchor=W)

        # Dropdown (option menu) menu widget for park rating
        self.rating_var = StringVar()
        self.rating_dropdown = OptionMenu(self.second_frame, self.rating_var, "0", "1", "2", "3", "4", "5")
        self.rating_dropdown.pack(padx=10, pady=10, anchor=W)

        # Label widget with step-by-step instruction - step 5
        self.ratingtext_label = Label(self.second_frame, text="5. Optionally, justify your rating:")
        self.ratingtext_label.pack(padx=10, anchor=W)

        # Text box widget for rating details
        self.rating_text=Text(self.second_frame, width=90, height=10, wrap=WORD)
        self.rating_text.pack(padx=10, pady=10, anchor=W)

        # Save button widget
        self.journalentry_button = Button(self.second_frame, text="Save", command=self.save_journal_entry)
        self.journalentry_button.pack(padx=10, pady=10)

        # Cancel button widget
        self.cancel_button = Button(self.second_frame, text="Cancel", command=self.cancel_journal_entry)
        self.cancel_button.pack(padx=10, pady=10)
    
    # Part 2c Save Journal Entry Function - WIP TODO
    def save_journal_entry(self):
        '''method for saving the details of a new journal entry as a file that can be accessed later'''
        self.text_file = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Text File", ".txt")], 
                                                initialdir=JOURNAL_DIR, initialfile=self.natpark_var.get()) # wip TODO
        if self.text_file != "": # empty when cancel was pressed!
            image_file_path = ""
            if len(self.pic_filename_list) > 0:
                image_file_path = self.pic_filename_list[self.current_pic]
            file_text = f"National Park Visited: {self.natpark_var.get()}\nDetails: {self.text.get(1.0, END)}\nRating:{self.rating_var.get()}\nRating Details: {self.rating_text.get(1.0, END)}\n\n{image_file_path}"
            self.text_file.write(file_text)
            self.text_file.close()
            self.journal_entry.destroy() # close window
            self.entries_list.delete(0,END) # clear entries
            self.journal_entry_list = os.listdir(JOURNAL_DIR) # grab list
            for item in self.journal_entry_list: # populate entries list
                self.entries_list.insert(END, item) 
    
    # Part 2d Cancel New Journal Entry Function
    def cancel_journal_entry(self):
        '''method for canceling and discarding the creation of a new journal entry'''
        self.journal_entry.destroy() # close window

    
    # Part 3a Open Existing Journal Entry Function
    def open_journal_entry(self):
        '''method for opening and accessing a journal file entry via the 'Open a journal entry' button'''
        
        # Select file to open for viewing/editing
        journal_file = filedialog.askopenfilename(initialdir=JOURNAL_DIR, title="Open Journal Entry Text File")
        self.load_journal(journal_file)
        
    def load_journal(self, journal_file):

        ''' method that does the actual loading after give a file name'''
        self.journal_file = journal_file

        # New window for frame and text box widgets below
        self.open_journal_entry = Toplevel() # new window
        
        # Frame widget for text box
        self.open_journal_frame=Frame(self.open_journal_entry)
        self.open_journal_frame.pack(padx=10, pady=10)   
        
        # Text box widget for journal entry file contents to appear in when opened
        self.open_text_file = Text(self.open_journal_frame, width=90, height=20)
        self.open_text_file.pack(padx=10, pady=10)

        # load text and image data
        journal_txt, journal_img_path = self.get_text_and_image_from_journal(self.journal_file)

        # show text/img in self.open_text_file widget
        self.open_text_file.delete("1.0", END)
        self.open_text_file.insert(END, journal_txt)
        if journal_img_path != None:
            self.img_in_journal = ImageTk.PhotoImage(journal_img_path)
            self.open_text_file.image_create("end -2 lines", image=self.img_in_journal) # puts the image just above the file name
       

        # Save button widget
        self.journal_save_entry_button = Button(self.open_journal_frame, text="Save Journal", command=self.save_journal_after_dialog_view)
        self.journal_save_entry_button.pack(padx=10, pady=5)

        # Cancel button widget
        self.cancel_journal_button = Button(self.open_journal_frame, text="Close Journal", command=self.cancel_journal_changes)
        self.cancel_journal_button.pack(padx=10, pady=5)

    # Part 3c Save File Menu Function
    def save_journal_after_dialog_view(self):
        self.existing_filename = os.path.basename(self.journal_file) # keep same file name when saving
        self.journal_file_save = filedialog.asksaveasfilename(defaultextension=".*", initialdir=JOURNAL_DIR, initialfile=self.existing_filename, title="Save Journal Entry Text File")

        # CH: after the image has been placed inside the text area, another /n is placed at the end and
        # that screws up the image file name detection on loading. So im removing the 2. \n here
        txt = self.open_text_file.get("1.0", END)
        if txt[-2:] == "\n\n":
            txt = txt[:-1] 

        self.journal_file_save = open(self.journal_file_save, 'w+') 
        self.journal_file_save.write(txt)
        self.journal_file_save.close()
        self.open_journal_entry.destroy() # close window

        # re-do the list of journals b/c we could have save under a different name!
        self.entries_list.delete(0,END) # clear entries
        self.journal_entry_list = os.listdir(JOURNAL_DIR) # grab list
        for item in self.journal_entry_list: # populate entries list
            self.entries_list.insert(END, item) 
    
    def get_text_and_image_from_journal(self, journal_txt_file):
        '''reads in journal_txt_file and returns the text part. If the last line is a image file path a PIL image will also be returned.
           If not image file path was given of if that file could not be read, None is returned instead'''
        file_clicked = open(journal_txt_file, 'r')
        txt = file_clicked.read()
        img = None
        file_clicked.close()

        # CH see if the last line is an image file name
        lines = txt.splitlines()
        last_line = lines[-1]
        if last_line[-4:] == ".png" or last_line[-4:] == ".jpg":
            img_path = os.path.join(PHOTOS_DIR, last_line)
            try:
                img = Image.open(img_path)
            except:
                pass 
            else:
                img.thumbnail((300, 225))  # thumbnail to internally change the image, and not return a changed copy

        return txt, img



    # Part 3d Double Click Open Existing Journal Entry Function
    def double_click_journal(self, event):
        '''method for opening and accessing a journal file entry from the listbox by double clicking on the applicable journal file'''
        journal_file = self.entries_list.get(ACTIVE)
        journal_file = os.path.join(JOURNAL_DIR, journal_file)
        self.load_journal(journal_file)
        
    # Part 3e Cancel Journal Edits Button Function
    def cancel_journal_edits(self):
        '''method for canceling the viewing/editing of an existing journal entry - via double clicked mode'''
        self.click_journal_entry.destroy()

    # Part 3f Cancel Journal Changes Button Function
    def cancel_journal_changes(self):
        '''method for canceling the viewing/editing of an existing journal entry - via 'Open a journal entry' button mode'''
        self.open_journal_entry.destroy()
        
    # Part 3h Save File Function for Double Click Mode 
    def save_clicked_file(self):
        '''method for saving an existing journal entry via file menu 'Save' option or 'Save' button for double clicked mode'''
        try: # for simply saving the same journal file that was opened directly from the listbox
            self.click_existing_filename = os.path.basename(self.click_journal_file) # keep the same filename as initially opened entry
            self.click_journal_file_save = filedialog.asksaveasfilename(defaultextension=".*", initialdir=JOURNAL_DIR, initialfile=self.click_existing_filename, title="Save Journal Entry Text File")

            with open(self.click_journal_file_save, 'w+') as self.click_journal_file_save:
                self.click_journal_file_save.write(self.click_text_file.get("1.0", END))

                self.click_journal_file_save.close()
        except: # for saving a different journal file that is opened with the 'Open' file menu option after initially opening a journal file from the listbox (still a WIP TODO, but without this, this function was not working at all)
            self.clicked_existing_filename = os.path.basename(self.clicked_journal_file) # keep the same filename as currently opened entry - wip TODO
            self.click_journal_file_saved = filedialog.asksaveasfilename(defaultextension=".*", initialdir=JOURNAL_DIR, initialfile=self.clicked_existing_filename, title="Save Journal Entry Text File")

            with open(self.click_journal_file_saved, 'w+') as self.click_journal_file_saved:
                self.click_journal_file_saved.write(self.click_text_file.get("1.0", END))

                self.click_journal_file_saved.close()


    # Part 4 New Learn Inquiry Function
    def new_learn_inquiry(self, event):
        '''method for learning about a national park after selecting one from the dropdown menu'''

        # Destroy frame widget created above to clear contents of the frame
        self.learn_info_frame.destroy() 
        
        # Recreate frame widget to display widgets below
        self.learn_info_frame=Frame(self.frame2) 
        self.learn_info_frame.pack(padx=10, pady=10, anchor=W)
        
        # Read in excel file and get selected item from drop down menu
        learn_excel = pd.read_excel("Database - Learn.xlsx")
        park_from_list = self.natpark_learn_var.get() # selected item

        park_info = learn_excel[learn_excel['Name'] == park_from_list]
        park_info_list = park_info.values.tolist() 

        # Label widget with image displayed
        img_open = Image.open(park_info_list[0][2])
        img_resize = img_open.resize((300, 225), Image.LANCZOS)
        park_pic = ImageTk.PhotoImage(img_resize)
        self.image_label = Label(self.learn_info_frame, image=park_pic)
        self.image_label.image = park_pic
        self.image_label.pack(padx=10, pady=5, anchor=W)

        # label widget with location of park
        self.location_label = Label(self.learn_info_frame, text=("Location: "+park_info_list[0][1]))
        self.location_label.pack(padx=10, pady=5, anchor=W)
        self.location_label.configure(wraplength=800, justify=LEFT)

        # label widget with description of park
        self.desc_label = Label(self.learn_info_frame, text="Description: "+park_info_list[0][7])
        self.desc_label.pack(padx=10, pady=5, anchor=W)
        self.desc_label.configure(wraplength=800, justify=LEFT)

        # label widget with NPS page link
        self.link_label = Label(self.learn_info_frame, text="National Park Service Official Web Page", fg="blue", cursor="hand2", font=('TkDefaultFont', 13, 'underline'))
        self.link_label.pack(padx=10, pady=(0,5), anchor=W)
        self.link_label.bind("<Button-1>", lambda e: webbrowser.open_new(park_info_list[0][3]))

        # label widget with nature and wildlife details
        self.wildlife_label = Label(self.learn_info_frame, text="Common wildlife to be seen in the park includes: "+park_info_list[0][10]+ ", and more! For more information about nature and wildlife, please visit:")
        self.wildlife_label.pack(padx=10, pady=0, anchor=W)
        self.wildlife_label.configure(wraplength=800, justify=LEFT)

        # label widget with nature and wildlife URL
        self.nw_link_label = Label(self.learn_info_frame, text=str(park_info_list[0][11]) , fg="blue", cursor="hand2", font=('TkDefaultFont', 13, 'underline'))
        self.nw_link_label.pack(padx=10, pady=(0,10),anchor=W)
        self.nw_link_label.bind("<Button-1>", lambda e: webbrowser.open_new(park_info_list[0][11]))

        # label widget with activities details
        self.activities_label = Label(self.learn_info_frame, text="Common activities throughout the park include: "+park_info_list[0][12]+ ", and more! For more information about nature and wildlife, please visit:")
        self.activities_label.pack(padx=10, pady=0, anchor=W)
        self.activities_label.configure(wraplength=800, justify=LEFT)

        # label widget with activities URL
        self.act_link_label = Label(self.learn_info_frame, text=str(park_info_list[0][13]) , fg="blue", cursor="hand2", font=('TkDefaultFont', 13, 'underline'))
        self.act_link_label.pack(padx=10, pady=(0,10), anchor=W)
        self.act_link_label.bind("<Button-1>", lambda e: webbrowser.open_new(park_info_list[0][13]))

        # label widget with operating hours and seasons details
        self.ops_label = Label(self.learn_info_frame, text="Operating hours: "+park_info_list[0][8]+ ". For more information about hours and holiday closures, please visit:")
        self.ops_label.pack(padx=10, pady=0, anchor=W)
        self.ops_label.configure(wraplength=800, justify=LEFT)

        # label widget with operating hours and seasons URL
        self.ops_link_label = Label(self.learn_info_frame, text=str(park_info_list[0][9]) , fg="blue", cursor="hand2", font=('TkDefaultFont', 13, 'underline'))
        self.ops_link_label.pack(padx=10, pady=(0,10), anchor=W)
        self.ops_link_label.bind("<Button-1>", lambda e: webbrowser.open_new(park_info_list[0][9]))
        
        # label widget with cost per vehicle details
        self.costv_label = Label(self.learn_info_frame, text="Cost of Entry Per Vehicle: $"+str(park_info_list[0][4]))
        self.costv_label.pack(padx=10, pady=(5,0), anchor=W)
        
        # label widget with cost per person details
        self.costp_label = Label(self.learn_info_frame, text="Cost of Entry Per Person: $"+str(park_info_list[0][5]))
        self.costp_label.pack(padx=10, anchor=W)

        # label widget with cost per motorcyle details
        self.costm_label = Label(self.learn_info_frame, text="Cost of Entry Per Motorcycle: $"+str(park_info_list[0][6]))
        self.costm_label.pack(padx=10, anchor=W)
        
       
        
# WIP TODO parts:
# Part 2c - incorporating uploaded image from part 2b in a filetype that supports both images and text
# Part 3h - system error preventing currently opened filename from autopopulating after a different entry is opened using the part 3g function




master = Tk()  # create a Tk window called master
master.title("National Park Journal for Outdoor Enthusiasts TkInter GUI")
myapp = App(master) # create App object within master (Tk) windowmaster.mainloop() # draw master window, react to events only
master.mainloop() # draw master window, react to events 
print("Done")


