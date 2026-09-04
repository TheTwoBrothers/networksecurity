import os

class S3Sync:
    def sync_folder_to_s3(self, folder_path: str, bucket_name: str, s3_folder: str):
        """
        Syncs a local folder to an S3 bucket.

        Args:
            folder_path (str): The local folder path to sync.
            bucket_name (str): The name of the S3 bucket.
            s3_folder (str): The destination folder in the S3 bucket.
        """
        try:
            import boto3
            from botocore.exceptions import NoCredentialsError

            s3_client = boto3.client('s3')

            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    local_file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(local_file_path, folder_path)
                    s3_file_path = os.path.join(s3_folder, relative_path).replace("\\", "/")

                    s3_client.upload_file(local_file_path, bucket_name, s3_file_path)
                    print(f"Uploaded {local_file_path} to s3://{bucket_name}/{s3_file_path}")

        except NoCredentialsError:
            print("Credentials not available.")
        except Exception as e:
            print(f"An error occurred: {e}")