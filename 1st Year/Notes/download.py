import os

import requests

url_pattern = "https://assets.leetcode.com/static_assets/public/images/badges/2024/gif/2024-{month:02d}.gif"

directory = "leetcode_gifs"
if not os.path.exists(directory):
    os.makedirs(directory)

for month in range(1, 2):
    url = url_pattern.format(month=month)
    filename = os.path.join(directory, f"2024-{month:02d}.gif")
    response = requests.get(url)

    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Downloaded: {filename}")
    else:
        print(f"Failed to download: {filename}")
