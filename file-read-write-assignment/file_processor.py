def process_file():
    filename = input("Enter filename to read: ")
    
    try:
        with open(filename, 'r') as file:
            content = file.read()
        
        # Modify content (convert to uppercase)
        modified_content = content.upper()
        
        # Write to new file
        output_filename = f"modified_{filename}"
        with open(output_filename, 'w') as file:
            file.write(modified_content)
        
        print(f"File processed successfully! Output saved to: {output_filename}")
        
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    process_file()
