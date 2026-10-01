extension = input("file name: ").strip().lower()

if extension.endswith(".gif"):
    print("image/gif")
elif extension.endswith(".jpg") or extension.endswith(".jpeg"):
    print("image/jpeg")
elif extension.endswith(".png"):
    print("image/png")
elif extension.endswith(".pdf"):
    print("image/pdf")
elif extension.endswith(".txt"):
    print("image/txt")
elif extension.endswith(".zip"):
    print("image/zip")
else:
    print("application/octet-stream")