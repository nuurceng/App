import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path.remove("/opt/ros/kinetic/lib/python2.7/dist-packages")
import cv2
import glob

import threading
import time

import argparse
import pandas as pd


parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('-v', '--version', action='version',
                    version='%(prog)s 1.0', help="Show program's version number and exit.")
parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                    help='Show this help message and exit.')
parser.parse_args()

class App ():

    def __init__(self) -> None:
        self.excel_iptal = False
        self.excel_iptal_lock = threading.Lock()
        self.excel_thread = threading.Thread(name="Birinci servis", target=self.g)
      

    def images(self):
        img=cv2.imread("./2.jpg")
        resize=cv2.resize(img,None, fx=0.5, fy=0.5)
        print(resize.shape)

        cv2.imshow("image",img)
        cv2.imshow("resize",resize)
        if cv2.waitKey(0) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
        

    def g(self):
        print(threading.currentThread().getName(), "Basliyor")
        time.sleep(3)
       
        self.excel_iptal_lock.acquire()
        if (self.excel_iptal):
            print('iptal edildi.')
            return
        else :
            data = {
                'isim': ['Muhammed','Nazli','Fatma','Cem','Faruk','Duygu','Ahmet','Mustafa'],
                 'sehir':['Bolu','Eskisehir','Istanbul','Sakarya','Duzce','Istanbul','Sakarya','Duzce'],
                 'yas':[22,21,23,22,20,22,21,22],
                 'puan':[95,80,82,90,90,84,80,75]}
    
            df = pd.DataFrame(data=data)
            df.to_excel('./states.xlsx')
            print("Basari ile kaydedildi...")

        self.excel_iptal_lock.release()
        print(threading.currentThread().getName(), "Bitiyor")

    def excel_iptal_et(self):
        self.excel_iptal_lock.acquire()
        self.excel_iptal = True
        self.excel_iptal_lock.release()

    def baslatExcel(self):
        self.excel_thread.start()
       

    def dosya(self):
        dict = {1: 'Good', 
        2: 'Font', 
        3: 'Mood', 
        4:'Activate', 
        5:'Deactivate'}

        #print("\nInteger Keys and Values: ")
        #print(dict)
    
        metin_dosyalari= glob.glob("./*.txt") #/home/autodrive/autodrive_stajyer
        for dosya in metin_dosyalari:
            print(dosya)
        
        metin_dosya= glob.glob("./[2468]*.txt")
        for files in metin_dosya:
            #filess = files[-5:]
            print(files)
            """
            for key, value in dict.items(): 
                if(key % 2==0):
                    print(key, value) 
                    with open(files,"w") as file:
                        file.write(f" {value}")
                    file.close()"""

            with open(files,"w") as file:
                for key, value in dict.items(): 
                    if(key % 2==0):
                        print(key, value) 
                        file.write(f" {value}")
            file.close()
       
        """
        with open("/home/autodrive/autodrive_stajyer/2.txt", "w") as file:
            for i in dict: 
                if(i == 2) : 
                    print ("Aranan Deger Mevcut")
                    file.write(f" {dict[2]}")
        file.close()
                """

       
    def grafik(self):
        x = np.array([0, 1, 2, 3])
        y = np.array([3, 8, 1, 10])
        plt.subplot(2, 1, 1)
        plt.plot(x,y)

        x = np.array([0, 1, 2, 3])
        y = np.array([10, 20, 30, 40])
        plt.subplot(2, 1, 2)
        plt.plot(x,y)

        plt.show()

    def stop(self):
        print ("Exiting Main Thread")
        self.excel_thread.join()
        print("cikis yapiliyor")
    
    
    def helper_string(self):
        print("-----------------------------------------------------------")
        print("***** Uygulama Menusu *****")
        print("1 - matplotlib grafigi  \n2 - txt islemi \n3 - excel \n4 - iptal \n5 - resize islemi \n6 - cikis ")
        print("-----------------------------------------------------------")


    def loop(self):
        tmp = 0
        while (tmp != 6):
            self.helper_string()
            option = int(input("\nLutfen 1-6 Arasi Bir Secenek Seciniz : "))
            if option == 1:
               self.grafik()
                
            elif option == 2:
                self.dosya()
                
            elif option == 3:
                self.baslatExcel()

            elif option == 4:
                 self.excel_iptal_et()

            elif option == 5:
                self.images()
            
            elif option == 6:
                self.stop()
                return
                
            else:
                print("gecersiz islem")
            

if __name__=='__main__':

    b=App()
    b.loop()

