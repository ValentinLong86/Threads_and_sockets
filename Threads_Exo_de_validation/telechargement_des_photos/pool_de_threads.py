import time
import concurrent.futures
import requests

img_urls = [
    "https://pixabay.com/get/ged6acbd44e74bdd933c8c7af8e11440d90d6bf0468ffcb42072df0350131a9fb4410923d8884fe99728f29c3c21bb720df88e7bd01aff81e244aaa1dcd0682999326dcf0e865e3e4b3425a94b3193fdf_1920.jpg",
    "https://pixabay.com/get/g849e7752b55320aa0989798e07911200a1b3bcc4dc74efd5424db911a57cfcb6316d9b57064f63852ec3a08ba8320e3fffa2a7cad46cf36be1c1e16de20bf2fe808b77a537e5e7dc67d69e21c23d3ed2_1920.jpg",
    "https://pixabay.com/get/gf363f79af2be7b04b9f14717fd7d87959e3e8519f52e3510a7ffa0bef5b52c2cc262fb9e4932db6c191b8c21b56c5b89d4b3f9cbff199cc55aae66400961df3b36d667bda60c14e7830a422856fbdf95_1920.jpg"
]

def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[4]
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")

start = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)

end = time.perf_counter()

print(f"Tasks ended in {round(end - start, 2)} second(s)")