"""
This code takes urls from a file named as url.txt
and download the url content as as .zip
"""

# importing the requests module
import requests

with open("url.txt","rt") as file:
    list_urls= [url.strip() for url in file.readlines()]
file.close()

# Downloading the file by sending the request to the URL
print('Downloading started')

for url in list_urls:
    req = requests.get(url)
# Split URL to get the file name
    filename = url.split('/')[3]
    filename+='.zip'
    print(filename)
# Writing the file to the local file system
    with open(filename,'wb') as output_file:
        output_file.write(req.content)

print('Downloading Completed')