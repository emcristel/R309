
import time
import threading
import concurrent.futures
import requests
import multiprocessing
import statistics

img_urls=['https://cdn.pixabay.com/photo/2017/03/31/15/34/cactus-2191647_1280.jpg',
        'https://cdn.pixabay.com/photo/2021/06/22/14/55/girl-6356393_1280.jpg',
        'https://cdn.pixabay.com/photo/2017/09/02/15/10/lighthouse-2707528_1280.jpg']


def download_image(img_url):
        img_bytes= requests.get(img_url).content
        img_name= img_url.split ('/')[9] #neuf correspond nombre / que 
        with open (img_name,'wb') as img_file:
            img_file.write(img_bytes)
            print(f"{img_name} was downlaod")


def thread():

    i1=threading.Thread(target=download_image,args=[img_urls[0]]) #création thread
    i1.start() #démarrage thread
    i2=threading.Thread(target=download_image,args=[img_urls[1]])
    i2.start()
    i3=threading.Thread(target=download_image,args=[img_urls[2]])
    i3.start()

    i1.join() #attente que ke thread se termine
    i2.join()
    i3.join()


def pool():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_image, img_urls)


def multi():

    for img in img_urls:    
        t= multiprocessing.Process(target=download_image, args=(img,))
        t.start()
        t.join()




if __name__ == "__main__":

    print()
    print("Thread:")
    start= time.perf_counter()# démarrage du timer
    thread()
    end = time.perf_counter()# fin du timer
    print()
    valeur = end - start
    print(f"Tasks ended in {round(valeur, 2)} second(s)") #montre le temps pour finir les thread avec 2 chiffres après virgule


    print()
    print("Pool:")
    start= time.perf_counter()# démarrage du timer
    pool()
    end = time.perf_counter()# fin du timer
    print()
    valeur1 = end - start
    print(f"Tasks ended in {round(valeur1, 2)} second(s)")#montre le temps pour finir les thread avec 2 chiffres après virgule


    print()
    print("multi:")
    start= time.perf_counter()# démarrage du timer
    multi()
    end = time.perf_counter()# fin du timer
    print()
    valeur2 = end - start
    print(f"Tasks ended in {round(valeur2, 2)} second(s)")#montre le temps pour finir les thread avec 2 chiffres après virgule
