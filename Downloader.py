#!/usr/bin/env python3

# File Downloader
import requests

# Modify URL
url = 'https://www.example.com/folder/file.txt'
r = requests.get(url, allow_redirects=True)
open('file.txt', 'wb').write(r.content)
