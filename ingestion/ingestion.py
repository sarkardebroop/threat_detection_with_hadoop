from hdfs import InsecureClient
import os

hdfs_url = 'http://localhost:9000'  
hdfs_user = 'debroop' 

# Define HDFS and local paths
hdfs_path = '/user/debroop/logs/syslog.log' 
local_log_file = 'C:/logs/syslog.log'  

client = InsecureClient(hdfs_url, user=hdfs_user)

def upload_log():
    if not os.path.exists(local_log_file):
        print(f"File not found")
        return

    with open(local_log_file, 'rb') as reader:
        client.write(hdfs_path, reader, overwrite=True)
    print(f"Uploaded")

if __name__ == '__main__':
    upload_log()
