def iterate_file(file_path):
    """Iterate over a file and print each line using next and iter functions."""
    try:
        with open(file_path, 'r') as file:
            file_iterator = iter(file)
            while True:
                try:
                    line = next(file_iterator)
                    print(line.strip())
                except StopIteration:
                    break
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":

    file_path = "Generators and Iterators/data.txt"
    iterate_file(file_path)
