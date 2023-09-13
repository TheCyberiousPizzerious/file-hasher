import hashlib
import binascii

# Things thats outside everything
while True:
	algorithm = input("Choose algorithm (crc or SHA256): ")
	if algorithm in ['crc', 'SHA256']:
		print(f"Algorithm chosen: {algorithm}")
		break
	else:
		print("Invalid hashing algorithm, try again")

while True:
	operation_choice = input("Choose an operation (hash or compare): ").lower()
	if operation_choice in ['hash', 'compare']:
		print(f"Operation chosen: {operation_choice}")
		break
	else:
		print("Invalid operation choice, try again")

def calculate_hash(file_path, algorithm):
	try:
		if algorithm == 'SHA256':
			hash_object = hashlib.sha256()
		elif algorithm == 'crc':
			hash_object = 0
		else:
			print("Invalid algorithm choice.")
			return None

		with open(file_path, 'rb') as file:
			for chunk in iter(lambda: file.read(4096), b''):
				if algorithm == 'SHA256':
					hash_object.update(chunk)
				elif algorithm == 'crc':
					hash_object = binascii.crc32(chunk, hash_object)

		if algorithm == 'SHA256':
			hash_value = hash_object.hexdigest()
		elif algorithm == 'crc':
			hash_value = hex(hash_object & 0xFFFFFFFF)[2:].zfill(8)

		return hash_value

	except FileNotFoundError:
		print("File not found")
		return None


if operation_choice == 'hash':
	file_path = input("From your current directory write the path to your file: ")

	hash_value = calculate_hash(file_path, algorithm)

	if hash_value:
		print(f"Hash value ({algorithm.upper()}) of '{file_path}': {hash_value}")

elif operation_choice == 'compare':
	compare_choice = input("Compare str and file or file and file (str_f or f_f): ").lower()

	if compare_choice == 'str_f':
		file_path = input("From your working directory write the path to your file: ")         
		str_input = input("Write the string that you want to compare: ")
		
		hash_value = calculate_hash(file_path, algorithm)

		if hash_value and str_input:
			print(f"The hash provided: \n{str_input}")
			print(f"The {algorithm.upper()} hash from file: \n{hash_value}")
			if hash_value == str_input:
				print("The hash and the file provided match")
			else:
				print("The file and string does not match")
		else:
			print("Missing string or path")

	elif compare_choice == 'f_f':
		file_path1 = input("From your current directory choose the path to the first file: ")
		file_path2 = input("From your current directory choose the path to the second file: ")

		hash_value1 = calculate_hash(file_path1, algorithm)
		hash_value2 = calculate_hash(file_path2, algorithm)
		if hash_value1 and hash_value2:
			print(f"hash of file 1: {hash_value1}")
			print(f"hash of file 2: {hash_value2}")
			if hash_value1 == hash_value2:
				print("The files MATCH")
			else: 
				print("The files does not match")
		else:
			print("Hash fail try again")
	else:
		print("Invalid choice")
else:
	print("Somethings ammis XD")