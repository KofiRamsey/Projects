import os

# path
path = "D:\\Games\\Grand Theft Auto V\\mods\\update\\x64\\dlcpacks"

obj = os.scandir(path)

# List all files and directories in the specified path
print("Files and Directories in '% s':" % path)
for entry in obj:
	if entry.is_dir() or entry.is_file():
		print(f'		<string>{entry.name}</string>')




