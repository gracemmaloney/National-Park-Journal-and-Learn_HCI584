# National-Park-Journal-and-Learn_HCI584
This repository will host my HCI 584X course project, a national park journaling and learning GUI for outdoor enthusiasts. This GUI will enable users of the application to digitally store their memories from national parks in the US and record the details of their visits. Additionally, users can learn about different national parks in the US.

Project Repo Structure:
- Docs folder: folder containing developer's documentation and project specification
- Main_Final.py: .py file to be ran
- Database - Learn.xlsx: data for Learn tab of GUI and for dropdown menu lists of US National Parks
- National Park Photos: folder containing a photo of each US national park (via NPS)
- Journal Entries: folder containing existing journal entries
- Journal Photos: folder containing images that can be uploaded into new journal entries
-------------------
# Usage
1. Clone or download the National-Park-Journal-and-Learn_HCI584 repo to the desired location on your computer
2. Refer to requirements.txt for the non-standard modules required for this project. Many of the modules included in this project are part of the standard Python library, so they should already be available as part of your Python installation and won't require additional installations. But if not already included or installed in your Python environment, the following install dependencies will be needed:
   - pillow
   - pandas
   - To install these required packages, you can use this pip command: pip install -r requirements.txt
4. Run/execute Main_Final.py in the python 3 environment (I use interpreter version 3.11 and utilize VSCode)
-------------------
# How to Use
If you prefer to view a step-by-step video walkthrough, one can be found here: https://www.loom.com/share/3d0665c7175446b391256df25da30729

1. Once Main_Final.py has been executed, the application will open with the Journal tab displayed by default.
<img width="926" alt="Screenshot 2023-07-31 at 3 51 54 PM" src="https://github.com/gracemmaloney/National-Park-Journal-and-Learn_HCI584/assets/133996701/07650c2c-d6da-49c6-9396-f69f489a69f2">

2. From the Journal tab, you can create a new journal entry by clicking the 'Create new journal entry' button. If you plan to upload an image, make sure to first save the image in the Journal Photos folder.
<img width="926" alt="Screenshot 2023-07-31 at 3 51 54 PM" src="https://github.com/gracemmaloney/National-Park-Journal-and-Learn_HCI584/assets/133996701/648ae105-2ae6-4346-8a0d-92383c25c533">

3. A new window will appear where you can select the national parked visited, enter details and memories from your visit, select an image to upload from your visit, rate the national parked visited, and justify your rating. In order to upload an image, make sure to first save the image in the Journal Photos folder. Also, if the contents of this window appear cut off, resize the height of the window with your mouse and a scrollbar will appear!
<img width="725" alt="Screenshot 2023-07-31 at 3 56 17 PM" src="https://github.com/gracemmaloney/National-Park-Journal-and-Learn_HCI584/assets/133996701/4160397f-185b-4b34-8dd0-ba411921d3f2">

4. Once the journal entry has been completed, you can click the 'Save' button to save your journal entry. If you begin to enter a new journal entry and wish to discard it, you can click the 'Cancel' button.
<img width="723" alt="Screenshot 2023-07-31 at 4 01 01 PM" src="https://github.com/gracemmaloney/National-Park-Journal-and-Learn_HCI584/assets/133996701/0e549384-24fe-4e88-9442-f4d3ebc764da">

5. Upon clicking the 'Save' button, a filedialog window will appear for you to save your journal entry in the Journal Entries folder. By default, the park name populates as the initial filename, but this can be adjusted if you prefer an alternative filename.
<img width="804" alt="Screenshot 2023-07-31 at 4 01 32 PM" src="https://github.com/gracemmaloney/National-Park-Journal-and-Learn_HCI584/assets/133996701/93ea4759-89ae-4de9-b36a-05e55197b87d">

6. The new journal entry, along with any other existing entries, will appear in the listbox on the Journal tab.
<img width="927" alt="Screenshot 2023-07-31 at 4 06 34 PM" src="https://github.com/gracemmaloney/National-Park-Journal-and-Learn_HCI584/assets/133996701/4143bfeb-d071-4bb2-b811-250bd82531c7">

7. To view or edit an existing journal entry, you can click the 'Open a journal entry' button or double click an entry from the listbox.
<img width="927" alt="Screenshot 2023-07-31 at 4 06 34 PM" src="https://github.com/gracemmaloney/National-Park-Journal-and-Learn_HCI584/assets/133996701/08c783a5-18e2-4be0-b2a4-e50a9a9b65ac">

8. If using the button, a filedialog window will appear for you to select the applicable journal entry from the Journal Entries folder.
<img width="807" alt="Screenshot 2023-07-31 at 4 09 19 PM" src="https://github.com/gracemmaloney/National-Park-Journal-and-Learn_HCI584/assets/133996701/3b92a317-8ad5-4a3f-96f5-6bbad4eb4db1">

9. Once the applicable journal entry is selected and opened, the contents of the entry will appear in a new window, where the entry can be viewed, edited, and saved, as needed. Saving can be done by clicking the 'Save Journal' button at the bottom of the entry window
<img width="680" alt="Screenshot 2023-07-31 at 4 11 49 PM" src="https://github.com/gracemmaloney/National-Park-Journal-and-Learn_HCI584/assets/133996701/91b5b1e4-02c9-4a89-98ec-3753abb57560">

10. If you open a journal entry and wish to close out of the window, you can simply press the close button in the top left corner of the window, or click the 'Close Journal' button.
<img width="682" alt="Screenshot 2023-07-31 at 4 13 25 PM" src="https://github.com/gracemmaloney/National-Park-Journal-and-Learn_HCI584/assets/133996701/2a939e67-82e0-4ef9-9152-0b4de4f51f2d">

11. To access the Learn tab of the application, click on the 'Learn' tab at the top of the main application window.
<img width="929" alt="Step 13" src="https://github.com/gracemmaloney/National-Park-Journal-and-Learn_HCI584/assets/133996701/6c4065bf-d174-433d-8199-87312843ca66">

12. To learn about a US National Park, navigate to the dropdown menu list and select the appropriate park.
<img width="928" alt="Step 14" src="https://github.com/gracemmaloney/National-Park-Journal-and-Learn_HCI584/assets/133996701/13d918e3-5471-4f2f-bac0-223b87aed4b2">

13. After selecting a park from the dropdown menu, information about the park will be displayed on the Learn tab, including an image, the park's location, a description, and a link to the park's official National Park Service (NPS) web page. Additionally, details on common wildlife in the park and popular activities will be provided, along with NPS links that can be accessed directly from the GUI that will offer additional details. Operating hours and cost of entry details are also provided, along with supporting NPS links.
<img width="928" alt="Step 15" src="https://github.com/gracemmaloney/National-Park-Journal-and-Learn_HCI584/assets/133996701/2482b88c-e609-4b12-b5db-a6733117068a">

-------------------
# Acknowledgements
The database of information for this application (Database - Learn.xlsx) contains information from Wikipedia (park descriptions) and the National Park Service (all other information and images). 
