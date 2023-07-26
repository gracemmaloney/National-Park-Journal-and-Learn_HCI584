# National Park Journal & Learn GUI for Outdoor Enthusiasts: Developer’s Doc
------------------
# Overview
To help users capture memories from their adventures in national parks, this application enables a user to journal about their travels to national parks in the US. The primary interaction users can complete includes creating journal entries by selecting a national park they’ve visited, logging details about their experiences and memories at the selected national park, such as the hikes and activities they completed at the selected park, and rating the national park. Additionally, this application will also provide the capability to help a user learn information about different national parks, so a user could decide which national park(s) to visit next! There are also a couple small features offering additional functionality throughout the application, including an image viewer that users can add images to and methods for viewing, editing, and saving existing journal entries.

The primary users of this interface are individuals who enjoy traveling to and visiting national parks in the US and want a way to digitally capture, or log, details of their memories at the national parks they visit that can be accessed later. Additionally, users of this application include individuals seeking to learn about various national parks. The application will help users digitally record and store their memories in one place, preventing the need to record their experiences by hand on paper and store the record somewhere with the potential to be lost or misplaced.

This application is programmed as a desktop GUI application using Tkinter, which supports much of the heavy lifting, within a Python (.py) file. Data for this application project is stored in an Excel file (Database – Learn.xlsx). For the primary interactions involved with this project, I put together the dataset to include a list of US national parks, their location by state, images, cost of entry details, National Park Service (NPS) web page links, descriptions, and details about operating hours, activities, and wildlife. 

# Task Flows
Please refer to README.md (User's Guide) for a video walkthrough and supplemental screenshots of the application.

**Task 1: Create a new journal entry and log details from a visit to a national park**

Functions involved: __init__, enter_new_journal_entry, upload_image, save_journal_entry, cancel_journal_entry

1.	User launches application
2.	Application window is split between two tabs (Journal and Learn) but opens on the Journal tab by default
3.	User presses a button to “Create new journal entry”
4.	An updated interface is displayed to the user and a new window is available where they can identify a national park and jot down details of their experience
5.	User selects the appropriate national park from the dropdown menu
6.	User navigates to the textbox entry field, where they type in the desired details of their experience
7.	User can upload a picture from their visit to the selected national park
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

Functions involved: __init__, open_journal_entry, open_file, save_file, double_click_journal, cancel_journal_edits, cancel_journal_changes, open_clicked_file, save_clicked_file

1.	User navigates to Journal tab of main application window
2.	User clicks the ‘Open a journal entry’ button or double clicks on a journal entry from the listbox
3.	If using the button, a file dialog window will appear for the user to select the applicable journal entry to open from the Journal Entries folder
4.	Once the applicable journal entry is selected and opened, the contents of the entry will appear in a new window, where the entry can be viewed and edited as needed
5.	User can save the journal entry by clicking the 'Save' button at the bottom of the entry window, or by navigating to the File Menu and selecting the 'Save' option
6.	From the File Menu, the user can also open different existing journal entries for viewing, editing, and saving by clicking the File Menu ‘Open’ option. If a different entry is opened via the 'Open' File Menu option, its content will similarly populate in the existing journal entry window
7.	If the user opens a journal entry and wishes to close out of the window, they can simply press the close button specific to their operating system in the top left corner of the existing journal entry window, or click the 'Cancel' button at the bottom of the window

**Task 4: Scroll through image viewer on Journal tab**

Functions involved: __init__, scroll_forward, scroll_backward

1.	From the Journal tab, a user can also scroll through an image viewer by clicking the 'Forward' and 'Back' buttons below the image display
2.	The images displayed are saved in the Journal Photos folder. If the user wishes to display additional photos or change the photos being displayed, they can simply add images to the Journal Photos folder or edit the images in the folder by removing undesired images

**Task 5: Learn about a national park**

Functions involved: __init__, new_learn_inquiry

1.	User navigates to Learn tab of application
2.	Application loads interface with a dropdown menu of US national parks
3.	User selects a national park from the dropdown menu
4.	Application interface updates with the park’s location, an image, a park description, cost of entry details, operating hours, common activities, wildlife, and various National Park Service (NPS) links, including a link to the National Park Service web page dedicated to the selected national park

<img width="735" alt="Screenshot 2023-07-25 at 4 20 43 PM" src="https://github.com/gracemmaloney/National-Park-Journal-and-Learn_HCI584/assets/133996701/3f49e704-b287-4b6a-81ed-acd0327e8b67">

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
    - Also included within this function is an image display viewer label and supporting buttons enabling a user to browse through the images on display, which are saved in the Journal Photos folder

**def scroll_forward(self, pic_number):**

    - When the ‘Forward’ button is clicked, this function is called, enabling the functionality for clicking the ‘Forward’ button to scroll forward through the images being displayed in the image viewer on the Journal tab
    - Clicking the ‘Forward’ button to scroll through the images can be done in a continuous manner

**def scroll_backward(self, pic_number):**

    - When the ‘Back’ button is clicked, this function is called, enabling the functionality for clicking the ‘Back’ button to scroll backward through the images being displayed in the image viewer on the Journal tab
    - Clicking the ‘Back’ button to scroll through the images can be done in a continuous manner

**def enter_new_journal_entry(self):**

    - When the “Create new journal entry” button is clicked by the user on the Journal tab, this function is called
    - The interface will open a new window with the dropdown menu list of US national parks and a text entry field for the user to input details about their visit
    - This function also includes programming to populate the dropdown menu with the list of national parks by reading in this information from the dataset excel spreadsheet file using pandas
    - The national park rating dropdown menu, as well as the optional rating text entry field, is also displayed to the user at this stage
    - This function also hosts a button enabling a user to upload an image as part of a new journal entry by bringing up a file dialog window where the user can select a picture to upload
    - The “Save” button will need to be incorporated here as well, processing the data saving method and prompting the system to store the user’s inputted data, which will be stored as a text file and can be accessed later
    - The interface will also display instructions (in the form of labels) to prompt the user to select the national park, input details, upload an image, rate the park, justify their rating, and save (or cancel/discard) their entry
    - Because there is a quite a few widget within this function’s window, a scrollbar has also been configured and can be utilized if any of the widgets appear to be cut off and not visible

**def upload_image(self):**

    - When the ‘Upload image’ button is clicked by the user, this function is called
    - A file dialog window is presented to the user, allowing them to locate and select an image to upload as part of a new journal entry
    - The image uploaded is displayed to the user within a label contained in the journaling window

**def save_journal_entry(self):**

    - When the “Save” button is clicked by the user within the journaling window, this function is called
    - This function prompts the user’s system file manager to present a file dialog window so the user can enter a filename for their entry (if something other than the default park name is preferred) and save it as a text file on their computer
    - This function also prompts the listbox on the Journal tab to update with the list of existing journal entries, including the newly created journal entry

**def cancel_journal_entry(self):**

    - When the ‘Cancel’ button is clicked within the journaling window, this function is called and cancels/discards the creation of a new journal entry

**def open_journal_entry(self):**

    - When the “Open a journal entry” button is clicked by the user on the default Journal tab, this function is called
    - This function prompts the user’s system file manager to present a file dialog window so the user can select which journal entry to open from the Journal Entries folder
    - A new window is presented to the user and the contents of the opened journal entry populate in the window
    - This function also hosts the File Menu options (‘Open’ and ‘Save) for opening and saving a journal entry. ‘Open’ is linked to the open_file function and ‘Save’ is linked to the save_file function below
    - This function also includes ‘Save’ and ‘Cancel’ buttons, with ‘Save’ being linked to the save_file function and ‘Cancel’ being linked to the cancel_journal_changes function below

**def open_file(self):**

    - When the ‘Open’ File Menu option is clicked, this function is called
    - This function prompts the user’s system file manager to open a file dialog window so the user can select another journal entry text file to open, in case they want to view or edit another entry before closing out of the window
    - The selected journal entry file populates within the textbox window
    - Here, users can view and, if needed, edit and save another existing journal entry

**def save_file(self):**

    - When the ‘Save’ File Menu option is clicked, this function is called
    - When the ‘Save’ button is clicked on the window, this function is called
    - This function prompts the user’s system file manager to open a file dialog window so the user can confirm the filename for their revised entry (by default it remains as the park name) and save it as a text file on their computer within the Journal Entries folder

**def double_click_journal(self, event):**

    - When an item from the listbox on the Journal tab is double clicked by the user, this function is called
    - A new window is presented to the user and the contents of the selected journal entry populate in the window within a textbox within a frame widget
    - This function also hosts another set of File Menu options (‘Open’ and ‘Save) for opening and saving a journal entry. ‘Open’ is linked to the open_clicked_file function and ‘Save’ is linked to the save_clicked_file function below.
    - This function also includes another set of ‘Save’ and ‘Cancel’ buttons, with ‘Save’ being linked to the save_clicked_file function and ‘Cancel’ being linked to the cancel_journal_edits function below

**def cancel_journal_edits(self):**

    - When the ‘Cancel’ button is clicked within the window created as part of the double_click_journal function, this function is called
    - The journal entry contents window is closed

**def cancel_journal_changes(self):**

    - When the ‘Cancel’ button is clicked within the window created as part of the open_journal_entry function, this function is called
    - The journal entry contents window is closed

**def open_clicked_file(self):**

    - When the ‘Open’ File Menu option within the window created as part of the double_click_journal function, this function is called
    - This function prompts the user’s system file manager to open a file dialog window so the user can select another journal entry text file to open, in case they want to view or edit another entry (after viewing the one they double clicked on) before closing out of the window
    - The selected journal entry file populates within the textbox window
    - Here, users can view and, if needed, edit another existing journal entry

**def save_clicked_file(self):**

    - When the 'Save' File Menu option or 'Save' button within the window created as part of the double_click_journal function (double clicked mode) is clicked, this function is called
    - Function for saving an existing journal entry
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

# Known Issues
There are a couple parts of this project that are currently not working as intended, despite my attempts to implement the functionality, which include the following minor issues:
1.	Part 2c - save_journal_entry(self): Images uploaded as part of a new journal entry are not displayed when a user opens the journal entry for viewing and editing. While .txt files do not support image displaying, I was also unable to implement this functionality using other filetypes, including .doc, .docx, and .pdf, while still maintaining the functionality for easy editing of existing journal entries within the application.
<img width="682" alt="Screenshot 2023-07-26 at 10 58 42 AM" src="https://github.com/gracemmaloney/National-Park-Journal-and-Learn_HCI584/assets/133996701/36117c87-b6fe-419f-9934-98aaaf87439c">

2.	Part 3h (in connection with Part 3g) - save_clicked_file(self): When accessing an existing journal entry via double clicking on an entry from the listbox and then using the 'Open' File Menu option to open a different journal entry, there is a known code error/limitation preventing the filename from auto populating with the park name when clicking 'Save' via both the 'Save' button and the 'Save' File Menu option. Users that encounter this will need to manually select or type in the desired filename, being careful not to overwrite the wrong journal entry. Below are some screenshots illustrating this issue:
<img width="1228" alt="Screenshot 2023-07-26 at 10 43 07 AM" src="https://github.com/gracemmaloney/National-Park-Journal-and-Learn_HCI584/assets/133996701/fc23ef76-d004-417d-99a9-c4d7dd460071">
<img width="1234" alt="Screenshot 2023-07-26 at 10 43 36 AM" src="https://github.com/gracemmaloney/National-Park-Journal-and-Learn_HCI584/assets/133996701/072d1766-28c9-4de7-945a-01b45b19c793">

# Future Work
Although this application is simple, I think there is room for future development and improvements. Most importantly, I know the known issues mentioned above could be addressed and solved with more time, especially if addressed by a programmer with more expertise or even just a fresh perspective and set of eyes. With the issue of images uploaded as part of a new journal entry not being displayed when a user opens the journal entry for viewing and editing, I would like to see the programming tweaked to support filetypes, such as Word documents (.docx or .doc), that allow for easy editing internally within the application and externally on the user’s computer, depending on their preference, while also supporting the display of images. I tried to implement the code for several different filetypes I thought would solve the issue, but I was unable to identify and understand a solution that would work well enough and display an image. With the Part 3h issue, I suspect it might be a result of me not having enough knowledge about file system operations and lacking an understanding of the operations that are completed by the operating system in the background when opening and saving files. I think a more experienced programmer would have an easier time addressing this issue. 

Additionally, I had intended to style this GUI application in an effort to make it look more modern. The application looks okay on a Mac, but it looks quite dated on other computer systems. While I think the dated look is a bit cool and retro, I do think styling the GUI to appear more modern would be more in line with the expectations of users today, so future work for this application could include more modern styling. 

In my initial specification document, I had also noted that one enhancement for the application could involve allowing users to track which national parks they have visited, with the results represented as a visual (an image, a chart, or graph) or a percentage that is calculated and presented to the user within the GUI. Perhaps this would involve creating a third tab for the application, with this third tab dedicated to tracking which parks a user has visited and other data from their travels to National Parks in the US. I ended up not having quite enough time to tackle this feature enhancement, but future work could attempt to implement this idea, which I think could be really cool!

