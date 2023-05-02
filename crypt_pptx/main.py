import msoffcrypto


def fn_brute_force():
    for line in file_password:
        try:
            file_encrypted = open(path_file, "rb")
            file = msoffcrypto.OfficeFile(file_encrypted)
            file.load_key(password=line)
            with open("decrypted.pptx", "wb") as f:
                file.decrypt(f)
            file_encrypted.close()
            print("Password found: " + line)
            break
        except:
            print("Password not found :(")


if __name__ == '__main__':
    path_file = "C:\\x\\x\\x\\x\\x\\x.pptx"
    file_password = open("passwords", "r")
    fn_brute_force()
