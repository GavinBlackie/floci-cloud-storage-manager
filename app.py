# app.py
from s3_manager import S3Manager

# def main():
#     storage = S3Manager()
#     storage.create_bucket()

#     # Upload the sample file
#     storage.upload_file(
#         "uploads/sample.txt",
#         "documents/sample.txt"
#     )

#     # list all the files!!
#     storage.list_files()

#     # download the sample text file
#     storage.download_file(
#         "documents/sample.txt",
#         "downloads/sample_downloaded.txt"
#     )

#     # View infomation about the file!!
#     storage.file_information(
#         "documents/sample.txt"
#     )

#     # delete the sample file
#     storage.delete_file("documents/sample.txt")

# Display the CLI menu
def display_menu():

    print("\n==============================")
    print(" CLOUD FILE STORAGE MANAGER")
    print("==============================")

    print("1. Create S3 Bucket")
    print("2. Upload File")
    print("3. List Files")
    print("4. Download File")
    print("5. Delete File")
    print("6. File Information")
    print("7. Exit")

# Run the CLI program
def main():

    storage = S3Manager()

    while True:

        display_menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":

            storage.create_bucket()

        elif choice == "2":

            file_path = input("Enter local file path: ")

            object_name = input("Enter S3 object key: ")

            storage.upload_file(
                file_path,
                object_name
            )

        elif choice == "3":

            storage.list_files()

        elif choice == "4":

            object_name = input("Enter S3 object key: ")

            download_path = input("Enter download path: ")

            storage.download_file(
                object_name,
                download_path
            )

        elif choice == "5":

            object_name = input("Enter S3 object key: ")

            storage.delete_file(object_name)

        elif choice == "6":

            object_name = input("Enter S3 object key: ")

            storage.file_information(object_name)

        elif choice == "7":

            print("Exiting application.")

            break

        else:

            print("Invalid choice. Try again.")


if __name__ == "__main__":

    main()

