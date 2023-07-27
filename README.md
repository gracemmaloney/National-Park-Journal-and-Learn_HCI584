# National-Park-Journal-and-Learn_HCI584
This repository will host my HCI 584X course project, a national park journaling and learning GUI for outdoor enthusiasts. This GUI will enable users of the application to digitally store their memories from national parks in the US and record the details of their visits. Additionally, users can learn about different national parks in the US.

Project Repo Structure:
- Docs folder: folder containing developer's documentation and initial project specification
- Main.py: .py file to be ran
- Database - Learn.xlsx: data for Learn tab of GUI and for dropdown menu lists of US National Parks
- National Park Photos: folder containing a photo of each US national park (via NPS)
- Journal Entries: folder containing existing journal entries
- Journal Photos: folder containing images to be displayed on default tab of application
-------------------
# Usage
1. Clone or download the National-Park-Journal-and-Learn_HCI584 repo to the desired location on your computer
2. Refer to requirements.txt for the non-standard modules required for this project. Many of the modules included in this project are part of the standard Python library, so they should already be available as part of your Python installation and won't require additional installations. But if not already included or installed in your Python environment, the following install dependencies will be needed:
   - pillow
   - pandas
   - To install these required packages, you can use this pip command: pip install -r requirements.txt
4. Run/execute Main.py in the python 3 environment (I use interpreter version 3.11 and utilize VSCode)
-------------------
# How to Use
If you prefer to view a step-by-step video walkthrough, one can be found here: https://www.loom.com/share/cda160aee29949a6b9775eba417c7d2f

1. Once Main.py has been executed, the application will open with the Journal tab displayed by default.
<img width="928" alt="Step 1" src="https://github.com/gracemmaloney/National-Park-Journal-and-Learn_HCI584/assets/133996701/eb346e1f-db1b-4a9f-89d6-453d419e7370">

2. From the Journal tab, you can create a new journal entry by clicking the 'Create new journal entry' button.
<img width="928" alt="Step 2" src="https://github.com/gracemmaloney/National-Park-Journal-and-Learn_HCI584/assets/133996701/66cf239f-d7d6-41a7-b05c-bae29707bd6b">

3. A new window will appear where you can select the national parked visited, enter details and memories from your visit, upload an image from your visit, rate the national parked visited, and justify your rating. Optionally, for easy uploading of images, I would first save the image in the Journal Photos folder. Also, if the contents of this window appear cut off, resize the height of the window with your mouse and a scrollbar will appear!
<img width="726" alt="Step 3" src="https://github.com/gracemmaloney/National-Park-Journal-and-Learn_HCI584/assets/133996701/29b0a924-e7b9-45a7-847d-cc14cc297ab6">

4. Once the journal entry has been completed, you can click the 'Save' button to save your journal entry. If you begin to enter a new journal entry and wish to discard it, you can click the 'Cancel' button.
<img width="726" alt="Step 4" src="https://github.com/gracemmaloney/National-Park-Journal-and-Learn_HCI584/assets/133996701/23d5d641-1d35-4253-869f-b8706d748d40">

5. Upon clicking the 'Save' button, a filedialog window will appear for you to save your journal entry in the Journal Entries folder. By default, the park name populates as the initial filename, but this can be adjusted if you prefer an alternative filename.
<img width="805" alt="Step 5" src="https://github.com/gracemmaloney/National-Park-Journal-and-Learn_HCI584/assets/133996701/6739b93b-a594-4cfc-a61f-a57398ac4438">

6. The new journal entry, along with any other existing entries, will appear in the listbox on the Journal tab.
<img width="928" alt="Step 6" src="https://github.com/gracemmaloney/National-Park-Journal-and-Learn_HCI584/assets/133996701/33d03c00-6ffc-4eb7-8257-f86c97acc7d4">

7. To view or edit an existing journal entry, you can click the 'Open a journal entry' button or double click an entry from the listbox.
<img width="928" alt="Step 7" src="https://github.com/gracemmaloney/National-Park-Journal-and-Learn_HCI584/assets/133996701/8477456d-6eeb-4884-a32f-07a9514d8add">

8. If using the button, a filedialog window will appear for you to select the applicable journal entry from the Journal Entries folder.
<img width="807" alt="Step 8" src="https://github.com/gracemmaloney/National-Park-Journal-and-Learn_HCI584/assets/133996701/1684275a-33d8-4bd4-ba76-e1353219ac6e">

9. Once the applicable journal entry is selected and opened, the contents of the entry will appear in a new window, where the entry can be viewed, edited, and saved, as needed. Saving can be done by clicking the 'Save' button at the bottom of the entry window, or by navigating to the File Menu and selecting the 'Save' option.
<img width="683" alt="Step 9a" src="https://github.com/gracemmaloney/National-Park-Journal-and-Learn_HCI584/assets/133996701/07576b27-b2db-49ab-b7f2-1a33a07dc60d">
<img width="197" alt="Step 9b" src="https://github.com/gracemmaloney/National-Park-Journal-and-Learn_HCI584/assets/133996701/337598a9-8d58-436d-b2b6-9f2f83e63377">

10. From the File Menu, you can also open different existing journal entries for viewing, editing, and saving as needed. If a different entry is opened via the 'Open' File Menu option, it will similarly populate in the journal entry window.
<img width="197" alt="Step 10" src="https://github.com/gracemmaloney/National-Park-Journal-and-Learn_HCI584/assets/133996701/2227f6a1-c89e-44bd-b78f-f7cc52b1e6d7">

11. If you open a journal entry and wish to close out of the window, you can simply press the close button in the top left corner of the window, or click the 'Cancel' button.
<img width="683" alt="Step 11" src="https://github.com/gracemmaloney/National-Park-Journal-and-Learn_HCI584/assets/133996701/2b712c99-9810-47d6-b3a0-30750e0e958c">

12. From the Journal tab, you can also scroll through an image viewer by clicking the 'Forward' and 'Back' buttons. The images displayed are saved in the Journal Photos folder. If you wish to display additional photos or change the photos being displayed, simply add images to the Journal Photos folder or edit the images in the folder by removing undesired images.
<img width="928" alt="Step 12" src="https://github.com/gracemmaloney/National-Park-Journal-and-Learn_HCI584/assets/133996701/5772204d-7a89-4fb8-adc8-567e3f7a52b5">

13. To access the Learn tab of the application, click on the 'Learn' tab at the top of the main application window.
<img width="929" alt="Step 13" src="https://github.com/gracemmaloney/National-Park-Journal-and-Learn_HCI584/assets/133996701/6c4065bf-d174-433d-8199-87312843ca66">

14. To learn about a US National Park, navigate to the dropdown menu list and select the appropriate park.
<img width="928" alt="Step 14" src="https://github.com/gracemmaloney/National-Park-Journal-and-Learn_HCI584/assets/133996701/13d918e3-5471-4f2f-bac0-223b87aed4b2">

15. After selecting a park from the dropdown menu, information about the park will be displayed on the Learn tab, including an image, the park's location, a description, and a link to the park's official National Park Service (NPS) web page. Additionally, details on common wildlife in the park and popular activities will be provided, along with NPS links that can be accessed directly from the GUI that will offer additional details. Operating hours and cost of entry details are also provided, along with supporting NPS links.
<img width="928" alt="Step 15" src="https://github.com/gracemmaloney/National-Park-Journal-and-Learn_HCI584/assets/133996701/2482b88c-e609-4b12-b5db-a6733117068a">

-------------------
# Known Limitations
There are a couple parts of this project that are currently not working as intended, despite my attempts to implement the functionality, including:
1. Images uploaded as part of new journal entries are not displayed when a user opens the journal entry for viewing and editing. While .txt files do not support image displaying, I was also unable to implement this functionality using other filetypes, including .doc, .docx, and .pdf while still maintaining the functionality for easy editing of existing journal entries within the application.
2. When accessing an existing journal entry via double clicking on an entry from the listbox and then using the 'Open' File Menu option to open a different journal entry, there is a known code error/limitation preventing the filename from autopopulating with the park name when clicking 'Save' via both the 'Save' button and the 'Save' File Menu option. Users that encounter this will need to manually select or type in the desired filename, being careful not to overwrite the wrong journal entry.

Apologies in advance for any inconvenience these limitations may cause, but if you come across a solution for either of these limitations, I'd appreciate your help! 

-------------------
# Acknowledgements
The database of information for this application (Database - Learn.xlsx) contains information from Wikipedia (park descriptions) and the National Park Service (all other information and images). 
