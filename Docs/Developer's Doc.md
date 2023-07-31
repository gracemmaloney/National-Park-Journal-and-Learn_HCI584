# National Park Journal & Learn GUI for Outdoor Enthusiasts: Developer’s Doc
------------------
# Overview
To help users capture memories from their adventures in national parks, this application enables a user to journal about their travels to national parks in the US. The primary interaction users can complete includes creating journal entries by selecting a national park they’ve visited, logging details about their experiences and memories at the selected national park, such as the hikes and activities they completed at the selected park, and rating the national park. Additionally, this application will also provide the capability to help a user learn information about different national parks, so a user could decide which national park(s) to visit next! There are also a couple small features offering additional functionality throughout the application, including methods for viewing, editing, and saving existing journal entries.

The primary users of this interface are individuals who enjoy traveling to and visiting national parks in the US and want a way to digitally capture, or log, details of their memories at the national parks they visit that can be accessed later. Additionally, users of this application include individuals seeking to learn about various national parks. The application will help users digitally record and store their memories in one place, preventing the need to record their experiences by hand on paper and store the record somewhere with the potential to be lost or misplaced.

This application is programmed as a desktop GUI application using Tkinter, which supports much of the heavy lifting, within a Python (.py) file. Data for this application project is stored in an Excel file (Database – Learn.xlsx). For the primary interactions involved with this project, I put together the dataset to include a list of US national parks, their location by state, images, cost of entry details, National Park Service (NPS) web page links, descriptions, and details about operating hours, activities, and wildlife. 

# Task Flows
Please refer to README.md (User's Guide) for a brief video walkthrough and supplemental screenshots of the application.

**Task 1: Create a new journal entry and log details from a visit to a national park**

Functions involved: __init__, enter_new_journal_entry, scroll_forward, scroll_backward, save_journal_entry, cancel_journal_entry

1.	User launches application
2.	Application window is split between two tabs (Journal and Learn) but opens on the Journal tab by default
3.	User presses a button to “Create new journal entry”
4.	An updated interface is displayed to the user and a new window is available where they can identify a national park and jot down details of their experience
5.	User selects the appropriate national park from the dropdown menu
6.	User navigates to the textbox entry field, where they type in the desired details of their experience
7.	User can upload a picture from their visit to the selected national park by scrolling through available images from the Journal Photos folder using the back and forward buttons
8.	[Task 2 completed - see below]
9.	User navigates to the ‘Save’ button towards the bottom of the interface to save the journal entry
      - If a user wishes to discard a new journal entry, the user navigates to the ‘Cancel’ button at the bottom of the interface
11.	Upon clicking the 'Save' button, a file dialog window appears for the user to save their journal entry in the Journal Entries folder. By default, the park name populates as the initial filename, but this can be adjusted if the user prefers an alternative filename
12.	Journal entry window closes and the Journal tab listbox updates with the user’s new entry displayed for them to view, edit, and save later, as needed

**Task 2: Rate the national park visited**

Function involved: enter_new_journal_entry

1.	After the user records their memories in the primary textbox, the user has the option to rate the selected national park on a scale from 0-5 in the form of another dropdown menu
2.	User selects a rating from the dropdown menu
3.	User justifies the rating by inputting a rating justification description in the rating textbox field

**Task 3: View, edit, and save an existing journal entry**

Functions involved: __init__, open_journal_entry, double_click_journal, load_journal, save_journal_after_dialog_view, get_text_and_image_from_journal, cancel_journal_changes

1.	User navigates to Journal tab of main application window
2.	User clicks the ‘Open a journal entry’ button or double clicks on a journal entry from the listbox
3.	If using the button, a file dialog window will appear for the user to select the applicable journal entry to open from the Journal Entries folder
4.	Once the applicable journal entry is selected and opened, the contents of the entry will appear in a new window, where the entry can be viewed and edited as needed
5.	User can save the journal entry by clicking the 'Save Journal' button at the bottom of the entry window
7.	If the user opens a journal entry and wishes to close out of the window, they can simply press the close button specific to their operating system in the top left corner of the existing journal entry window, or click the 'Close Journal' button at the bottom of the window

**Task 4: Learn about a national park**

Functions involved: __init__, new_learn_inquiry

1.	User navigates to Learn tab of application
2.	Application loads interface with a dropdown menu of US national parks
3.	User selects a national park from the dropdown menu
4.	Application interface updates with the park’s location, an image, a park description, cost of entry details, operating hours, common activities, wildlife, and various National Park Service (NPS) links, including a link to the National Park Service web page dedicated to the selected national park


<img width="846" alt="Screenshot 2023-07-31 at 5 15 42 PM" src="https://github.com/gracemmaloney/National-Park-Journal-and-Learn_HCI584/assets/133996701/b86d0ed2-18cb-4a71-994d-c4d3e482aa6c">


# Technical Flow
For this GUI application programmed using Tkinter, the necessary data is stored in an Excel file. The data includes a list of US national parks, their location by state, images, cost of entry details, various National Park Service (NPS) web page links, descriptions, and details about operating hours, activities, and wildlife specific to each park. To work with this data and enable it to fit the needs of this project, the pandas module is utilized. UI elements include many widgets, such as a master window, frames, tabs, labels, text entry fields, buttons, a listbox, and dropdown menus.

**Application functions:**

**Class App(Frame):**

    - Frame for all functions and widgets below

**def __init__(self, master):**

    - This is the primary window to host the application’s two tabs, Journal and Learn, and their widgets
    - The app will launch with the Journal tab and its widgets displayed by default
    - This function will also host the “Create new journal entry” button (Journal tab), with the command registered with a left button click callback to the enter_new_journal_entry function below
    - Labels will also be included to provide the user with guidance on entering a new journal entry (Journal tab) and how to learn about various national parks (Learn tab)
    - A listbox for existing journal entry will also be displayed on the default Journal tab, including a button enabling a user to open an existing journal entry on their computer or open an existing journal entry by double clicking on an entry from the listbox
    - Within this function, there is also the default widgets of the Learn tab, including a dropdown menu of parks and a frame that will populate with information about each park, which will later clear each time a user selects a different park to learn about from the dropdown menu

**def scroll_forward(self, pic_number):**

    - When the ‘Forward’ button is clicked, this function is called, enabling the functionality for clicking the ‘Forward’ button to scroll forward through the images being displayed in the image viewer selector on the new journal entry window
    - Clicking the ‘Forward’ button to scroll through the images can be done in a continuous manner

**def scroll_backward(self, pic_number):**

    - When the ‘Back’ button is clicked, this function is called, enabling the functionality for clicking the ‘Back’ button to scroll backward through the images being displayed in the image viewer selector on the new journal entry window
    - Clicking the ‘Back’ button to scroll through the images can be done in a continuous manner

**def enter_new_journal_entry(self):**

    - When the “Create new journal entry” button is clicked by the user on the Journal tab, this function is called
    - The interface will open a new window with the dropdown menu list of US national parks and a text entry field for the user to input details about their visit
    - This function also includes programming to populate the dropdown menu with the list of national parks by reading in this information from the dataset excel spreadsheet file using pandas
    - The national park rating dropdown menu, as well as the optional rating text entry field, is also displayed to the user at this stage
    - This function also hosts the backward and forward buttons enabling a user to select an image to upload as part of a new journal entry with the displayed image being the image that will be tied to the new journal entry
    - The “Save” button will be incorporated here as well, processing the data saving method and prompting the system to store the user’s inputted data, which will be stored as a file and can be accessed later
    - The interface will also display instructions (in the form of labels) to prompt the user to select the national park, input details, upload an image, rate the park, justify their rating, and save (or cancel/discard) their entry
    - Because there is a quite a few widget within this function’s window, a scrollbar has also been configured and can be utilized if any of the widgets appear to be cut off and not visible

**def save_journal_entry(self):**

    - When the “Save” button is clicked by the user within the journaling window, this function is called
    - This function prompts the user’s system file manager to present a file dialog window so the user can enter a filename for their entry (if something other than the default park name is preferred) and save it as a file on their computer
    - This function also prompts the listbox on the Journal tab to update with the list of existing journal entries, including the newly created journal entry

**def cancel_journal_entry(self):**

    - When the ‘Cancel’ button is clicked within the journaling window, this function is called and cancels/discards the creation of a new journal entry

**def open_journal_entry(self):**

    - When the “Open a journal entry” button is clicked by the user on the default Journal tab, this function is called
    - This function prompts the user’s system file manager to present a file dialog window so the user can select which journal entry to open from the Journal Entries folder
    - This function also calls the load_journal function

**def load_journal(self, journal_file):**

    - A new window is presented to the user and the contents of the opened journal entry populate in the window, including image data of uploaded image (if applicable)
    - This function also includes the ‘Save Journal’ and ‘Close Journal’ buttons, with ‘Save Journal’ being linked to the save_journal_after_dialog_view function and ‘Close Journal’ being linked to the cancel_journal_changes function

**def save_journal_after_dialog_view(self):**

    - When the ‘Save Journal’ button is clicked on from the journal entry display window, this function is called
    - This function prompts the user’s system file manager to open a file dialog window so the user can confirm the filename for their revised entry (by default it remains as the original filename) and save it as a file on their computer within the Journal Entries folder
    - This function also prompts the listbox on the Journal tab to refresh/update with the list of existing journal entries

**def get_text_and_image_from_journal(self, journal_txt_file):**

    - When this function is called, journal_txt_file is read in, returning the text data part
    - If the last line is an image file path, an image in PIL image format will also be retuned
    - If no image file path is given or if the file can't be read, None is returned
    - Includes method for seeing if last line of text is an image filename

**def double_click_journal(self, event):**

    - When an item from the listbox on the Journal tab is double clicked by the user, this function is called
    - This function also calls the load_journal function

**def cancel_journal_changes(self):**

    - When the ‘Close Journal’ button is clicked within the window created as part of the open_journal_entry function, this function is called
    - The journal entry contents window is closed

**def save_clicked_file(self):**

    - When the 'Save Journal' button is clicked, this function is called
    - This function prompts the user’s system file manager to open a file dialog window so the user can save the file as needed within the Journal Entries folder

**def new_learn_inquiry(self, event):**

    - When the user navigates to the Learn tab of the primary window and selects a national park from the dropdown menu, this function is called
    - This function also includes programming to populate the dropdown menu with the list of national parks by reading in this information from the database Excel spreadsheet file using pandas
    - This portion of the interface will also display instructions (in the form of a label) to prompt the user to select a park from the dropdown menu list in order to learn about the appropriate park
    - This function also clears the frame where national park data appears (for the cases where the user has previously selected a park to learn about) and populates it with information on the currently selected national park by reading in this information from the dataset Excel spreadsheet file using pandas
    - This function then also displays several label widgets, an image, and clickable URL links

# Installation Dependencies
Refer to requirements.txt for the non-standard modules required for this project and installation guidance. If not already included or installed in your Python environment, the following installations will be needed:
1. pillow
2. pandas

# Future Work
Although this application is simple, I think there is room for future development and improvements. Additionally, I had intended to style this GUI application in an effort to make it look more modern. The application looks okay on a Mac, but it looks quite dated on other computer systems. While I think the dated look is a bit cool and retro, I do think styling the GUI to appear more modern would be more in line with the expectations of users today, so future work for this application could include more modern styling. 

In my initial specification document, I had also noted that one enhancement for the application could involve allowing users to track which national parks they have visited, with the results represented as a visual (an image, a chart, or graph) or a percentage that is calculated and presented to the user within the GUI. Perhaps this would involve creating a third tab for the application, with this third tab dedicated to tracking which parks a user has visited and other data from their travels to National Parks in the US. I ended up not having quite enough time to tackle this feature enhancement, but future work could attempt to implement this idea, which I think could be really cool!

