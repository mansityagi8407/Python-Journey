"""  That provides functions to interacting with the OS. it allows to perform a wide variety of tasks,such as reading and writing files. interacting with the system,and runnning system commands."""
import os

# if(not os.path.exists("data")):
#  os.mkdir("data")

# for i in range(0, 10):
#   os.mkdir(f"data/Day{i+1}")


# For RENAME
for i in range(0, 10):
  os.rename(f"data/Day{i+1}",f"data/Tutorial{i+1}")