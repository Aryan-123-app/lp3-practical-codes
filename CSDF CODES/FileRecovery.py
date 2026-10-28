import os
import subprocess

print("----- FILE RECOVERY SCRIPT -----")

# Display available devices
print("\nList of devices:")
subprocess.run(["lsblk"])

# Get device and image names
devname = input("\nEnter device path (e.g. /dev/sdb1): ")
imgname = input("Enter image filename: ")

# Create forensic image
print("\nCreating disk image...")

with open(imgname, "wb") as image:
    subprocess.run(
        ["dd", "if=" + devname, "bs=512", "status=progress"],
        stdout=image,
        check=True
    )

print("\nDisk image created successfully.")

# Display inode numbers
print("\nShowing deleted files and inode numbers:")
subprocess.run(["fls", "-d", imgname])

# Get inode number
inodeno = input("\nEnter inode of deleted file: ")

# Display inode information
print("\nFile information:")
subprocess.run(["istat", imgname, inodeno])

# Recover file
newfile = input("\nEnter recovered filename with extension: ")

with open(newfile, "wb") as recovered:
    subprocess.run(
        ["icat", imgname, inodeno],
        stdout=recovered,
        check=True
    )

print("\nFile recovered successfully.")
print("Recovered file:", newfile)
print("File size:", os.path.getsize(newfile), "bytes")