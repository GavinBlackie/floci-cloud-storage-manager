# app.py
from s3_manager import S3Manager

def main():
    storage = S3Manager()
    storage.create_bucket()

    # Upload the sample file
    storage.upload_file(
        "uploads/sample.txt",
        "documents/sample.txt"
    )

    # list all the files!!
    storage.list_files()

    # download the sample text file
    storage.download_file(
        "documents/sample.txt",
        "downloads/sample_downloaded.txt"
    )


if __name__ == "__main__":

    main()
