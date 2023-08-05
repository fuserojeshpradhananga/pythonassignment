def read_file(filename):
    try:
        with open(filename, "r") as file:
            contents = file.read()
            print("File Contents:")
            print(contents)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

if __name__ == "__main__":
    filename = input("Enter the filename: ")

    read_file(filename)
