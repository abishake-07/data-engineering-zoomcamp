"""

Goal is to execute this scipt from the docker container: proving that docker maintains state

"""
from pathlib import Path
curr_dir = Path(".")
curr_file = Path(__file__).name

print(f'Files in the {curr_dir}:')

for filepath in curr_dir.iterdir():
   if filepath.name  == curr_file:
       continue 
   
   print(filepath.name)
   
   if filepath.is_file():
       content = filepath.read_text(encoding="utf-8")
       if content == "": 
           print ("--------Empty file------")
       else: 
        print(f'Content of {filepath.name}:')
        print(content)

