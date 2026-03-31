def count_words_in_file(filename):
    try:
        # File open
        with open(filename, 'r') as file:
            content = file.read()

        # Words split 
        words = content.split()
        total_words = len(words)

        print("\nTotal number of words:", total_words)

    except FileNotFoundError:
        print("Error: File not found. Please check the file name.")
    
    except Exception as e:
        print("Something went wrong:", e)



file_name = input("Enter the file name (with .txt): ")

# Function call
count_words_in_file(file_name)