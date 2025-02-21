from pathlib import Path
new_folder = Path.home() / 'documents' / 'python_automation'

new_folder.mkdir(exist_ok=True)
# exist_ok prevents error when folder already exists

another_folder = new_folder / 'fun_with_folders' / 'my_3rd_folder'

# another_folder.mkdir(exist_ok=True)
# FileNotFoundError: [WinError 3] The system cannot find the path
# specified: 'C:\\Users\\olivi\\documents\\python_automation\\
# fun_with_folders\\my_3rd_folder'
# trying to create 2 new folders at once

another_folder.mkdir(exist_ok=True, parents=True)
# the parents=True parameter will create multiple folders at once

five_folders_down = another_folder / 'my_4th_folder' / 'my_5th_folder'

five_folders_down.mkdir(exist_ok=True, parents=True)

