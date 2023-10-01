import hashlib

def calculate_sha512(file_path):
    sha512 = hashlib.sha512()

    with open(file_path, 'rb') as file:
        while True:
            data = file.read(65536)
            if not data:
                break
            sha512.update(data)

    return sha512.hexdigest()

def print_cpp_hex_array(hash_string):
    print("unsigned char sha512Hash[] = {")
    for i in range(0, len(hash_string), 2):
        print(f"    0x{hash_string[i:i+2]},")
    print("};")

if __name__ == "__main__":
    print_cpp_hex_array(calculate_sha512('idrix_codeSign.cer'))
    print_cpp_hex_array(calculate_sha512('idrix_Sha256CodeSign.cer'))