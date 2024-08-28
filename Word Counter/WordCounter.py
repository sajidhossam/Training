def count_file_stats(filename):

    try:
        num_lines =0
        num_words = 0
        num_chars = 0

        with open(filename, 'r') as file:
            for line in file:
                num_lines += 1
                num_chars += len(line)
                num_words += len(line.split())
        print(f"Lines: {num_lines}")
        print (f"Words: {num_words}")
        print(f"Characters: {num_chars}")
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except PermissionError:
        print(f"Error: Permission denied to read file '{filename}'.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

while  True:

    filename = input("Enter file name: ")
    count_file_stats(filename)

    response  = input("Do you want to continue? (yes/no): ")
    if response.lower() != "yes":
        break