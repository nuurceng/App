# Control
Terminalden 1'den 6'ya kadar rakam olarak input alan bir programda,

     - Tüm inputlar kontrollü olarak alınır.
     - 1 inputu -> matplotlib kullanılarak oluşturulan bir grafiği ekranda gösterir.
     - 2 inputu -> home directory'sinde autodrive_stajyer klasörü içerisindeki txt dosyalarını bulup terminale yazdırır. 2'nin katı olan txt dosyaları içerisine map'te dosya ismine karşılık gelen key'in value değerini yazdırır. (glob kütüphanesi kullanılacak).
     - 3 inputu -> yeni bir thread başlatır. Bu thread ilk olarak 3 saniye bekler (sleep). İşlem iptal edilmedi ise map içerisinde bulunan değerleri excel olarak kaydeder (pandas kullan).
     - 4 inputu -> eğer 3 inputu girilmişse, yapılacak olan işi iptal eder. (lock kullanılmalı.)
     - 5 inputu -> opencv kütüphanesi kullanarak deneme klasörü içerisinde bulunan png'yi x ve y' de yarı yarıya resize ederek ekranda gösterir.
     - 6 inputu -> thread açık ise onu bekler ve programı kapatır.

Yukarıda belirtilen program OOP'ye uygun olarak python dili (versiyon >= 3.6) ile kodlanmalı. İşlemler sırasında kullanıcı sürekli bilgilendirilmeli. Her işlem sonunda input beklemeye geri dönülmeli.
