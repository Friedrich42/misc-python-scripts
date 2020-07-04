filename_original = input("Input filename for backup\n")
filename_of_copy = "backup_" + filename_original
step_of_reading_file = 1024 * 100

try:
	original_file = open(filename_original, "rb")
	copy_of_file = open(filename_of_copy, "ab")

	original_file_length = len(original_file.read())
	original_file.seek(0)

	for i in range(0, original_file_length, step_of_reading_file):
	    copy_of_file.write(original_file.read(step_of_reading_file))

	print("File backuped")
except FileNotFoundError:
	print("Original file not found.\n")
except MemoryError:
	print("MemError")
except NameError:
    	print("You did something wrong. Please, try it again.")
finally:
	original_file.close()
	copy_of_file.close()
