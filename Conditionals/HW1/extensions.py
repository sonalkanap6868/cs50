# Get and normalize user input by making it lowercase and stripping whitespace.
file_name = input("File name:").lower().strip()

# A dictionary to map file extensions to their corresponding MIME types.
mime_types = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip",
}

# Find the extension and print the MIME type, or the default if not found.
for extension, mime_type in mime_types.items():
    if file_name.endswith(extension):
        print(mime_type)
        break
else:  # This 'else' belongs to the 'for' loop.
    print("application/octet-stream")




#Basic Code Tried by Me

# user_input = input("File name:")

# if user_input.endswith(".pdf"):
#     print("image/pdf")

# elif user_input.endswith(".jpg"):
#     print("image/jpg")

# elif user_input.endswith(".jpeg"):
#     print("image/jpeg")

# elif user_input.endswith(".png"):
#     print("image/png")

# elif user_input.endswith(".pdf"):
#     print("image/pdf")

# elif user_input.endswith(".txt"):
#     print("image/txt")

# elif user_input.endswith(".txt"):
#     print("image/txt")

# elif user_input.endswith(".txt"):
#     print("image/txt")

# elif user_input.endswith(".zip"):
#     print("image/zip")

# else:
#     print("application/octet-stream")