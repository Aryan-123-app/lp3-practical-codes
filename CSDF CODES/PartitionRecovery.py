import subprocess

print("----- PARTITION RECOVERY SCRIPT -----")

# Display connected devices
print("\nList of devices:")
subprocess.run(["lsblk", "-o", "NAME,SIZE,FSTYPE,TYPE,MOUNTPOINTS"])

# Get device name
devname = input("\nEnter device path (e.g. /dev/sdb): ")

# Display partition table
print("\nShowing partition table:")
subprocess.run(["sudo", "fdisk", "-l", devname])

# Scan for lost partitions
print("\nStarting partition recovery inspection...")
print("TestDisk will help identify lost partitions.")

subprocess.run(["sudo", "testdisk", devname])

print("\nPartition recovery inspection completed.")
print("Verify partition boundaries before writing any changes.")