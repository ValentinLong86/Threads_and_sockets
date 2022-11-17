import time
import threading
import requests
import concurrent.futures
import multiprocessing
import sys
from statistics import mean

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

def using_Treads() -> float:
    start_thread_counter = time.perf_counter()
    Thread_list = []
    
    for i in range(3):
        Thread_list.append(threading.Thread(target=download_image, args=[img_urls[i]]))

    for i in range(len(Thread_list)):
        Thread_list[i].start()

    for i in range(len(Thread_list)):
        Thread_list[i].join()

    end_thread_counter = time.perf_counter()
    return round(end_thread_counter - start_thread_counter, 2)

def using_Multiprocessing() -> float:
    start_multiprocess_counter = time.perf_counter()
    Process_list = []
    
    for i in range(3):
        Process_list.append(multiprocessing.Process(target=download_image, args=[img_urls[i]]))
    
    for i in range(len(Process_list)):
        Process_list[i].start()

    for i in range(len(Process_list)):
        Process_list[i].join()

    end_thread_counter = time.perf_counter()

    end_multiprocess_counter = time.perf_counter()
    return round(end_multiprocess_counter - start_multiprocess_counter, 2) 

def using_Pool() -> float:
    start_pool_counter = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_image, img_urls)

    end_pool_counter = time.perf_counter()
    return round(end_pool_counter - start_pool_counter, 2)

def test_all_methods(numberOfTest:int = 1):
    thread_result_list = []
    multiprocessing_result_list = []
    pool_result_list = []

    for i in range(0, numberOfTest):
        thread_result = using_Treads()
        multiprocessing_result = using_Multiprocessing()
        pool_result = using_Pool()

        thread_result_list.append(thread_result)
        multiprocessing_result_list.append(multiprocessing_result)
        pool_result_list.append(pool_result)

    meanThread = mean(thread_result_list)
    meanMultiprocessing = mean(multiprocessing_result_list)
    meanPool = mean(pool_result_list)

    return meanThread, meanMultiprocessing, meanPool

if __name__ == "__main__":
    try:
        nb = sys.argv[1]
    except:
        print("La valeur de nb doit être spécifiée ou est incorrecte")
        sys.exit(-1)

    if sys.argv[1] == "--nb":
        try:
            nb = int(sys.argv[2])
            nb = abs(nb)
        except ValueError:
            print("La valeur spécifiée est incorrecte")
            sys.exit(-1)
        except:
            print("Valeur incorrecte")
            sys.exit(-1)
    else:
        print("Argument incorrect")
        sys.exit(-1)

    meanThread, meanMultiprocessing, meanPool = test_all_methods(nb)
    
    print(f"Threads : {meanThread:.2f}s\n"
        f"Multiprocessing : {meanMultiprocessing:.2f}s\n"
        f"Pool : {meanPool:.2f}s\n")