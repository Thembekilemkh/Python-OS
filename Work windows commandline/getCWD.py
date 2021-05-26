import os

terminal_dir = ["AppData", "Roaming", "MetaQuotes", "Terminal"]

# Get current working directory
cwd = os.getcwd()

# Put the directory in a list 
full_dir = []
curr_dir = ""
for dir_ in cwd:
	if dir_ is not "\\":
		curr_dir = curr_dir + dir_
	elif dir_ == "\\":
		full_dir.append(curr_dir)
		curr_dir = ""

full_dir.append(curr_dir)

# Get the part of the current working dir that is share with the mql5 terminals
mql_dir = ""
for dir_ in range(len(full_dir)):
	if full_dir[dir_] == "Users":
		mql_dir = mql_dir+full_dir[dir_]+"\\"+full_dir[dir_+1]+"\\"
		break
	else:
		mql_dir = mql_dir+full_dir[dir_]+"\\"

# Add the MQL5 dirs to the extracted dir
for dir_ in terminal_dir:
	mql_dir = mql_dir+dir_+"\\"

# List out all available terminals in mql5
all_mql_dir = os.listdir(mql_dir)

# Send to file to all mql dirs
for terminal in all_mql_dir:
	if len(terminal) > 20:
		cwt = mql_dir + terminal + "\\MQL5\\Experts\\"

		with open(cwt+"we_in.txt", "w") as file:
			file.write("Mama i made it.")

print("File sent to all terminals")