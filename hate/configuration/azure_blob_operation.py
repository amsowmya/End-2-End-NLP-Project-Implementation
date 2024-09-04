import os


# TODO: Replace <storage-account-name> with your actual storage account name
account_url = "https://<storage-account-name>.blob.core.windows.net"
credential = DefaultAzureCredential()

# Create the BlobServiceClient object
blob_service_client = BlobServiceClient(account_url, credential=credential)

def download_blob_to_file(self, blob_service_client: BlobServiceClient, container_name):
    blob_client = blob_service_client.get_blob_client(container=container_name, blob="sample-blob.txt")
    with open(file=os.path.join(r'filepath', 'filename'), mode="wb") as sample_blob:
        download_stream = blob_client.download_blob()
        sample_blob.write(download_stream.readall())

======================================

azcopy copy 'https://<storage-account-name>.<blob or dfs>.core.windows.net/<container-name>/<blob-path>' '<local-file-path>'


azcopy copy 'https://mystorageaccount.blob.core.windows.net/mycontainer/myTextFile.txt' 'C:\myDirectory\myTextFile.txt'