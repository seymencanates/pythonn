import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

# Örnek metin verisi ve yanıtlar
data = {
    "Bugün harika bir gün!": [
        "Ne güzel! Gününü daha da güzelleştirecek bir şey yapmak ister misin?",
        "Harika! Bugünü özel kılacak bir şey yapmayı düşündün mü?",
        "Bu enerjin çok güzel, paylaşmak ister misin?"
    ],
    "Çok üzgünüm, moralim bozuk.": [
        "Üzgün olmana üzüldüm. Seni neyin rahatsız ettiğini paylaşmak ister misin?",
        "Bazen kötü hissetmek normaldir, istersen biraz konuşalım.",
        "Moralini düzeltmek için sevdiğin bir şey yapabilir misin?"
    ],
    "Bu harika bir haber!": [
        "Evet, gerçekten harika! Bunun için nasıl bir kutlama yapmayı düşünüyorsun?",
        "Bunu duyduğuma çok sevindim! Bunu kiminle paylaşmayı düşünüyorsun?",
        "Kutlama yapmanın tam zamanı! Ne yapmayı planlıyorsun?"
    ],
    "Kendimi çok yalnız hissediyorum.": [
        "Yalnız hissetmek zor olabilir... İstersen biraz sohbet edelim?",
        "Bazen yalnızlık insanı düşündürür ama her zaman yanında birileri vardır.",
        "Bunu aşmak için yeni bir hobi edinmeyi düşündün mü?"
    ],
    "Beni mutlu ettin, teşekkürler!": [
        "Bunu duymak beni de mutlu etti! 😊 Başka bir şey yapmak ister misin?",
        "Ne güzel! Daha fazla mutlu olman için ne yapabilirim?",
        "Ben de mutlu oldum! Bugün için başka planların var mı?"
    ],
    "Seni çok özledim.": [
        "Ben de seni özledim!",
        "Özlemek güzel bir his, ama umarım yakında görüşebiliriz.",
        "Beni düşündüğün için teşekkür ederim. Nasıl yardımcı olabilirim?"
    ],
    "Merhaba": [
        "Merhaba!",
        "Selam! Nasılsın?",
        "Günün nasıl gidiyor?"
    ],
    "Teşekkürler": [
        "Rica ederim!",
        "Ne demek, her zaman buradayım!",
        "Senin için yapabileceğim başka bir şey var mı?"
    ],
    "Nasılsın?": [
        "İyiyim, sen nasılsın?",
        "Bugün harika hissediyorum! Sen nasılsın?",
        "Biraz yorgunum ama sohbet etmek iyi gelecek!"
    ],
    "Hava bugün çok güzel!": [
        "Evet, güneş var, ama biraz rüzgar da esiyor.",
        "Gerçekten harika bir hava! Dışarı çıkmayı düşünüyor musun?",
        "Böyle havalar insana enerji veriyor, değil mi?"
    ],
    "Biraz kitap okumak istiyorum.": [
        "Hangi tür kitaplar seviyorsun?",
        "Güzel fikir! Şu an elinde hangi kitap var?",
        "Kitap okumak harika bir alışkanlık! Kütüphanende neler var?"
    ],
    "Yine geç kaldım!": [
        "Merak etme, hepimiz bazen geç kalıyoruz.",
        "Önemli olan varmış olman! Acele etme, her şey yoluna girer.",
        "Bu seferlik sorun değil, bir dahaki sefere daha erken çıkmayı planlayabilirsin."
    ],
    "Çok acıktım.": [
        "Ne yemek istersin?",
        "Açlık en iyi aşçıdır! Canın ne çekiyor?",
        "Güzel bir yemek zamanı gelmiş! Evde bir şeyler hazırlayabilir misin?"
    ],
    "Bugün hiç enerjim yok.": [
        "Bazen böyle günler olur. Belki biraz dinlenmen gerekebilir.",
        "Kendine biraz zaman tanı, vücudun dinlenmeye ihtiyaç duyuyor olabilir.",
        "Düşük enerjiye iyi gelen şeylerden biri sevdiğin bir müziği dinlemek!"
    ],
    "Filmi çok beğendim!": [
        "Hangi filmi izledin?",
        "Süper! Konusu neydi, anlatır mısın?",
        "Etkileyici bir film izlemek çok güzel bir his! En sevdiğin sahne neydi?"
    ],
    "Güzel bir gün geçirdim.": [
        "Bunu duyduğuma sevindim! Hangi aktiviteleri yaptın?",
        "Harika! Gününü daha da güzel yapan şey neydi?",
        "Güzel günler insanın enerjisini artırıyor. Yarın için planın var mı?"
    ],
    "Bu aralar çok yoğunum.": [
        "Bazen işler çok birikiyor. Kendine de zaman ayırmayı unutma!",
        "Yoğun olmak güzel ama biraz mola vermek de önemli.",
        "Her şeyin üstesinden gelebilirsin, ama biraz dinlenmeyi unutma!"
    ],
    "Biraz tatil yapmayı düşünüyorum.": [
        "Harika bir fikir! Nerelere gitmeyi düşünüyorsun?",
        "Tatil planları yapmak her zaman heyecan vericidir! Denize mi, dağa mı gitmek istiyorsun?",
        "Süper! Tatilde dinlenmeyi mi yoksa keşfetmeyi mi daha çok seviyorsun?"
    ],
    "Bugün kafam karışık.": [
        "Ne oldu? Yardımcı olabilir miyim?",
        "Bazen insanın kafası karışır, belki biraz konuşmak iyi gelir.",
        "Aklını toparlamak için bir yürüyüş yapmayı düşündün mü?"
    ],
    "Bana yeni bir hobi öner.": [
        "Sanatla ilgilenmeyi denedin mi? Resim ya da müzik gibi.",
        "Belki bir enstrüman çalmayı deneyebilirsin!",
        "Fotoğrafçılık veya yazı yazmak ilginç olabilir mi?",
        "Doğa yürüyüşleri ve kamp yapmak da güzel bir seçenek olabilir!"
    ],
    "Bana bir soru sor.": [
        "En sevdiğin yemek nedir?",
        "Hayalindeki tatil yeri neresi?",
        "Eğer bir süper gücün olsaydı, ne olurdu?",
        "Bugüne kadar seni en çok etkileyen kitap veya film nedir?"
    ],
    "Gözlerim çok yoruldu.": [
        "Biraz ara vermek iyi olabilir. Belki göz egzersizleri yapabilirsin.",
        "Ekrandan uzaklaşıp bir süre dinlenmek iyi gelebilir.",
        "Biraz gözlerini kapatıp rahatlamayı dene."
    ],
    "Bir kahve içmeye gitmek ister misin?": [
        "Tabii, çok isterim!",
        "Kahve her zaman iyi bir fikir!",
        "Harika fikir! Yanında tatlı da alalım mı?"
    ],
    "Sana çok teşekkür ederim.": [
        "Ne demek, her zaman yardımcı olurum!",
        "Rica ederim, senin için buradayım!",
        "Senin mutlu olman benim için önemli!"
    ],
    "Güzel bir akşam yemeği hazırladım.": [
        "Bunu duymak harika! Ne yaptın?",
        "Muhteşem! Menüyü benimle paylaşır mısın?",
        "Yemek yapmak insanı mutlu eder! Nasıl bir tarif denedin?"
    ],
    "Beni çok düşündürdün.": [
        "Sana nasıl yardımcı olabilirim?",
        "Bu konuda daha fazla konuşmak ister misin?",
        "Bazen düşünmek güzeldir, yeni bakış açıları kazandırır."
    ],
    "Birlikte dışarı çıkalım mı?": [
        "Evet, kesinlikle! Hangi aktiviteleri yapmayı düşünüyorsun?",
        "Harika olur! Nereye gitmek istersin?",
        "Dışarı çıkmak iyi bir fikir! Doğa yürüyüşü yapalım mı?"
    ],
    "Yarını dört gözle bekliyorum!": [
        "Neden? Ne var yarın?",
        "Heyecanlı bir gün mü olacak?",
        "Umarım harika bir gün olur! Neler planladın?"
    ],
    "Bugün biraz yalnız hissediyorum.": [
        "Bunu duyduğuma üzüldüm. Birlikte vakit geçirebiliriz.",
        "Yalnızlık bazen güzel olabilir ama istersen sohbet edebiliriz.",
        "Eğer dışarı çıkmak istersen birlikte güzel bir aktivite düşünebiliriz!"
    ],
    "Yaz tatilini iple çekiyorum.": [
        "Ben de! Güneş, deniz, kum... Harika olacak!",
        "Tatilde neler yapmayı planlıyorsun?",
        "Tatil planların hazır mı, yoksa spontane mi gitmeyi seviyorsun?"
    ],
    "Hangi müzikleri dinlersin?": [
        "Çok çeşit müzik severim! Sen?",
        "Müziğin ruhu beslediğini düşünüyorum. Senin favori türün ne?",
        "Gününe göre değişiyor. Sen bugün hangi türde müzik dinliyorsun?"
    ],
    "Bazen sabahları zor uyanıyorum.": [
        "Belki gece daha erken yatmayı deneyebilirsin.",
        "Birkaç derin nefes alarak güne başlamak iyi gelebilir!",
        "Bir bardak su içmek ve esneme hareketleri yapmak uyanmanı kolaylaştırabilir."
    ],
    "Çok güzel bir gün!": [
        "Evet, gerçekten harika. Hangi planların var?",
        "Güzel havalarda yürüyüş yapmayı sever misin?",
        "Bugünü nasıl değerlendirmeyi düşünüyorsun?"
    ],
    "Spor yapmayı seviyorum.": [
        "Hangi sporu yapıyorsun?",
        "Spor yapmak harika! Düzenli mi yapıyorsun, yoksa arada sırada mı?",
        "Bunu duymak güzel! Spor yaparken müzik dinler misin?"
    ],
    "Bugün hiç keyfim yok.": [
        "Bazen böyle olur. Birlikte bir şeyler yapmayı düşünür müsün?",
        "Kendini iyi hissetmek için küçük bir şey yapmayı deneyebilirsin, mesela sevdiğin bir şarkıyı açabilirsin.",
        "Belki biraz yürüyüş yapmak veya sevdiğin bir şeyle ilgilenmek iyi gelir."
    ],
    "Film izlemeye gitmek ister misin?": [
        "Tabii, hangi filmi izleyelim?",
        "Harika olur! Komedi mi, aksiyon mu, yoksa romantik bir film mi?",
        "Eğer istersek evde de izleyebiliriz, ne dersin?"
    ],
    "Kahve içer misin?": [
        "Evet, çok severim! Lütfen.",
        "Kahve her zaman iyi bir fikirdir!",
        "Bugün farklı bir kahve denemek ister misin?"
    ],
    "Bir oyun oynayalım mı?": [
        "Evet! Hangi oyunu önerirsin?",
        "Oyun oynamak eğlenceli olur! Masa oyunu mu, yoksa bilgisayar oyunu mu?",
        "Ben de isterim! Strateji oyunları mı, yoksa eğlenceli bir şey mi olsun?"
    ],
    "Yavaş yavaş iyileşiyorum.": [
        "Bunu duyduğuma sevindim. Kendine iyi bak!",
        "Harika haber! Kendine zaman tanımayı unutma.",
        "İyileşme süreci bazen yavaş olur ama önemli olan ilerlemek!"
    ],
    "Bana bir öneri verir misin?": [
        "Tabii, belki bir film izlemeyi deneyebilirsin.",
        "Yeni bir şeyler denemek ister misin? Mesela bir kitap ya da yeni bir hobi?",
        "Belki biraz doğaya çıkıp temiz hava almak iyi gelir."
    ],
    "Bugün harika bir gün!": [
        "Ne güzel! Gününü daha da güzelleştirecek bir şey yapmak ister misin?",
        "Harika! Neler yapmayı planlıyorsun?",
        "Evet! Bugün ne yapmak istersin?"
    ],
    "Çok üzgünüm, moralim bozuk.": [
        "Üzgün olmana üzüldüm. Seni neyin rahatsız ettiğini paylaşmak ister misin?",
        "Bunu duyduğuma üzüldüm. Konuşmak ister misin?",
        "Her şey yoluna girecek, belki biraz sohbet edebiliriz?"
    ],
    "Bugün çok mutluyum!": [
    "Ne güzel! Mutluluğunu paylaşmak ister misin?",
    "Harika! Ne oldu da bu kadar mutlusun?",
    "Bunu duyduğuma sevindim! Mutluluğunu nasıl daha da arttırabilirim?"
    ],

    "Çok sıkıldım.": [
        "Sıkılmak zor olabilir. Belki yeni bir şeyler deneyebilirsin?",
        "Sıkıldığını duyduğuma üzüldüm. Birlikte sohbet edebiliriz, istersen.",
        "Bunu duyduğumda üzüldüm. Bir şeyler yaparak bu sıkıntıyı atlatabiliriz."
    ],

    "Yarın sınavım var, çok heyecanlıyım.": [
        "Heyecanlı olmak normal, başarılar dilerim! Hangi konularda zorlanıyorsun?",
        "Yarının sınavı için hazır hissetmek çok önemli. Kendini nasıl hissediyorsun?",
        "Sınav heyecanı yaşamak gerçekten zor olabilir. Belki biraz rahatlatıcı bir şeyler yapmalısın."
    ],

    "Yalnız hissediyorum.": [
        "Yalnız hissetmek zor olabilir... Ben buradayım, istersen biraz sohbet edebiliriz.",
        "Bunu duyduğum için üzgünüm. Yalnız hissettiğini paylaşmak ister misin?",
        "Yalnızlık zorlayıcı olabilir, ama unutma senin için buradayım."
    ],

    "Bugün güzel bir film izlemek istiyorum.": [
        "Harika fikir! Hangi türde bir film izlemek istersin?",
        "Buna bayılırım! Hangi filmi izlemeyi düşünüyorsun?",
        "Bunu duymak çok güzel! Ne tür bir film izlemeyi planlıyorsun?"
    ],

    "Yolculuğa çıkmayı düşünüyorum.": [
        "Bu harika! Nereye gitmek istersin?",
        "Yolculuklar çok eğlenceli olabilir. Hangi yerlere gitmeyi planlıyorsun?",
        "Bunu duyduğuma sevindim! Ne tür bir yolculuk planlıyorsun, iş ya da tatil?"
    ],

    "Çok mutluyum, çünkü çok güzel bir haber aldım.": [
        "Ne harika! Bu güzel haberin ne olduğunu paylaşmak ister misin?",
        "Bunu duyduğuma çok sevindim! Haberin neydi?",
        "Çok mutlu olduğuna sevindim! Haberi benimle paylaşır mısın?"
    ],

    "Bir şeyler değişmeli.": [
        "Değişim bazen zor olabilir ama harika bir fırsattır. Hangi konuda değişiklik yapmak istersin?",
        "Bunu anlıyorum. Değişiklikler hayatı daha ilginç kılabilir. Hangi konuda değişiklik yapmak istiyorsun?",
        "Değişiklikler bazen çok iyi gelir. Ne tür bir değişiklik yapmayı düşünüyorsun?"
    ],

    "Yarını dört gözle bekliyorum.": [
        "Bunu duyduğuma sevindim! Yarın seni ne bekliyor?",
        "Harika! Yarının senin için özel olacağını hissediyorum. Ne yapmayı planlıyorsun?",
        "Yarını beklemek çok heyecan verici olabilir. Yarın için özel bir planın mı var?"
    ],

    "Bugün kendimi yorgun hissediyorum.": [
        "Yorgun hissetmek normaldir, belki biraz dinlenmek iyi olabilir.",
        "Bu durumda biraz dinlenmek gerçekten yardımcı olabilir. Ne yaparak rahatlayabilirsin?",
        "Kendini yorgun hissettiğinde dinlenmek çok önemlidir. Biraz ara vermeyi düşünüyor musun?"
    ],

    "Bir şeyleri değiştirmek istiyorum ama nasıl başlayacağımı bilmiyorum.": [
        "Değişim zor olabilir ama küçük adımlarla başlayabilirsin. Hangi konuda değişiklik yapmak istersin?",
        "Bunu duyduğuma üzüldüm, ama unutma her şeyin bir başlangıcı vardır. Küçük bir adım atmak nasıl olurdu?",
        "Değişim zorlayıcı olabilir, ancak her şey adım adım başlar. Hangi alanda değişim yapmak istersin?"
    ],

    "Bugün dışarı çıkmak istiyorum ama hava kötü.": [
        "Havanın kötü olması seni engellememeli. İç mekan aktiviteleri yapmayı düşündün mü?",
        "Bunu duyduğumda üzülmemek elde değil. Belki başka bir gün dışarı çıkabilirsin.",
        "Bazen hava durumu keyfimizi etkileyebilir. Hangi aktiviteleri içerde yapmayı planlıyorsun?"
    ],

    "Biraz eğlenmek istiyorum.": [
        "Eğlenmek harika bir fikir! Ne tür eğlenceli şeyler yapmak istersin?",
        "Bunu duyduğuma sevindim! Ne yapmak istersin, belki bir oyun oynayabiliriz?",
        "Eğlenceli bir şeyler yapmak harika olabilir. Belki film izlemek ya da oyun oynamak istersin?"
    ],

    "Sevgilimle vakit geçirmek istiyorum.": [
        "Bu çok güzel! Birlikte yapmak istediğiniz bir şey var mı?",
        "Harika! Sevgilinle vakit geçirmek çok özel olabilir. Neler yapmak istersiniz?",
        "Sevdiğinle vakit geçirmek, çok değerli. Ne yapmayı planlıyorsunuz?"
    ],

    "Yarının iş günüm olacağı için biraz tedirginim.": [
        "İş günleri zorlayıcı olabilir. Endişelenmene gerek yok, her şey yolunda gidecek.",
        "Tedirginlik normaldir, ama unutma ki yarın her şeyin üstesinden gelebilirsin.",
        "İş günü öncesi tedirgin olmak yaygındır, ama sakin kalmak her zaman yardımcı olabilir."
    ],

    "Bugün biraz yalnız kalmak istiyorum.": [
        "Yalnız kalmak bazen iyi gelir. Kendine zaman ayırmak çok önemli olabilir.",
        "Yalnız kalmak, kendini toparlamak için güzel bir fırsat olabilir. Kendine nasıl vakit ayıracaksın?",
        "Bazen yalnız kalmak iyi bir şeydir. Bugün yalnız kalmayı nasıl planlıyorsun?"
    ],
    "Çok yorgunum ve dinlenmeye ihtiyacım var.": [
        "Dinlenmek en doğal hakkın. Vücudunu dinlemeli ve kendine iyi bakmalısın.",
        "Yorgunluk, vücudunun sana verdiği bir işarettir. Biraz mola vermek iyi gelebilir.",
        "Dinlenmek, enerjini toplamanın en iyi yoludur. Kendine zaman ayırmaktan çekinme."
    ],
    "Bugün hiç motive değilim.": [
        "Motivasyon eksikliği zaman zaman hepimizin başına gelebilir. Belki küçük bir mola vermek iyi gelebilir.",
        "Motivasyonunu artırmak için sevdiğin bir aktivite yapmayı deneyebilirsin.",
        "Unutma, her gün aynı enerjide olmak zorunda değilsin. Kendine karşı nazik ol."
    ],
    "Biraz endişeliyim.": [
        "Endişelenmek yerine, endişelerini yazmayı deneyebilirsin. Bu, onları daha iyi anlamana yardımcı olabilir.",
        "Derin bir nefes al ve rahatlamaya çalış. Her şeyin üstesinden gelebilirsin.",
        "Endişelerini güvendiğin biriyle paylaşmak, seni rahatlatabilir."
    ],
    "Kendimi çok stresli hissediyorum.": [
        "Stresle başa çıkmak için meditasyon veya yoga gibi rahatlama tekniklerini deneyebilirsin.",
        "Doğada vakit geçirmek, stresi azaltmanın harika bir yoludur.",
        "Stresini azaltmak için sevdiğin müzikleri dinleyebilir veya kitap okuyabilirsin."
    ],
    "Bugün biraz keyifsizim.": [
        "Keyifsiz hissetmek geçici bir durumdur. Kendine karşı sabırlı ol.",
        "Sevdiğin bir film izlemek veya komik bir video izlemek, moralini yükseltebilir.",
        "Kendine küçük bir ödül vermek, keyfini yerine getirebilir."
    ],
    "Hava bugün çok güzel": [
        "Evet, havanın güzel olması insanı mutlu ediyor. Belki biraz dışarı çıkıp yürüyüş yapabilirsin.",
        "Havanın güzel olması enerjimi yükseltiyor. Bugünümü daha verimli geçirebilirim.",
        "Hava güzel olunca içim kıpır kıpır oluyor. Belki arkadaşlarımla bir araya gelip vakit geçirebilirim."
    ],
    "Belirsiz bir huzursuzluk içindeyim.": [
        "İçindeki bu karmaşık duyguyu çözmek için, belki de hiç denemediğin bir sanat dalıyla ilgilenebilirsin.",
        "Bu huzursuzluk, bastırılmış bir yaratıcılığın dışa vurumu olabilir. Kendini ifade etmenin yeni yollarını keşfetmeyi dene.",
        "Bazen belirsizlik, yeni başlangıçların habercisidir. Bu huzursuzluğu, bilinmeyene doğru bir yolculuğa çıkmak için bir fırsat olarak gör."
    ],
     "Zihnimdeki Fırtına": [
    "Fırtına, ruhunun derinliklerinden kopan yaratıcılığın dansıdır; her rüzgar, seni farklı bir hikayeye götürür.",
    "Zihnindeki fırtına, geçici bir kargaşadır; sakinleştiğinde ardında yepyeni bir dünya açılır.",
    "Fırtınanın ortasında, her damla yağmur bir ilham kıvılcımıdır; içindeki enerjiyi serbest bırak."
  ],
  "Kırık Zamanlar": [
    "Zamanın kırık parçaları, geçmişin unutulmuş öykülerini fısıldar; her parça, geleceğin resmini yeniden çizer.",
    "Kırık anlar, seni tam da kim olduğunu hatırlatır; her kırık, yeniden inşa edilecek bir umut taşır.",
    "Zaman kırıldığında, içindeki parçaları topla ve kendi mozaik hikayeni oluştur."
  ],
  "Gölgelerin Dansı": [
    "Gölgeler, ışığın yokluğunda bile seninle dans eder; karanlıkta bile umut dolu adımlar atabilirsin.",
    "Kendi gölgelerinle dans etmek, geçmişin sessiz yankılarını anlamanın en şiirsel yoludur.",
    "Gölgeler, senin içsel dünyanın gizli odalarını aydınlatır; onlarla dans et, saklı hikayelerini keşfet."
  ],
  "Yıldızların Sessiz Fısıltısı": [
    "Gecenin koynunda yıldızlar, unutulmuş umutların sessiz fısıltılarını taşır; onlara kulak ver ve geleceğini dinle.",
    "Her yıldız, evrenin gizemli bir sırrını saklar; onların sessiz çığlıkları, ruhuna dokunan bir melodidir.",
    "Yıldızların parlaklığı, içindeki karanlığı aydınlatır; onların fısıltıları, seni bilinmeyen maceralara davet eder."
  ],
  "Kayıp Rüyalar": [
    "Kayıp rüyalar, unutulmuş masalların tozlu sayfaları gibidir; yeniden keşfet, çünkü her kayıp yeni bir başlangıç demektir.",
    "Rüyaların kaybolduğu an, içindeki özlemin sesini duyarsın; belki de bu, yeniden doğuşunun habercisidir.",
    "Kayıp rüyaların izinde, kendi iç dünyanı yeniden inşa et; her kayıp, geleceğe açılan bir kapıdır."
  ],
  "Biraz rahatlamak istiyorum.": [
        "Rahatlamak için müzik dinleyebilir veya sessiz bir yerde vakit geçirebilirsin.",
        "Belki sıcak bir çay içerek biraz huzur bulabilirsin.",
        "Derin nefes alıp vermek ve kısa bir meditasyon iyi gelebilir."
    ],
    "Bir şeylere odaklanmalıyım.": [
        "Odaklanmak önemli bir şey. Neye odaklanmak istiyorsun?",
        "Derin nefes al, zihnini boşalt ve tek bir şeye yönel.",
        "Küçük bir mola verip zihnini tazelemek odaklanmana yardımcı olabilir."
    ],
    "Bugün sokakta yürürken bir kuşun aniden bana doğru gelmesi, hayatımda yaşadığım en tuhaf anıydı.": [
        "Belki o kuş sana bir mesaj iletmeye çalışıyordu, kim bilir?",
        "Bazen doğa, gizli anlamlar taşır. O anın sende bıraktığı his neydi?",
        "Kuşlar bazen ilginç davranışlar sergiler. Belki de seni selamlamak istedi!"
    ],
    "İçimde birden fazla ben varmış gibi hissediyorum; biri sakin, biri telaşlı, biri ise hep kaybolmuş.": [
        "Bu, bir içsel yolculuğun başlangıcı olabilir.",
        "Belki de hepsi bir bütünün parçasıdır ve birbirlerinden öğrenmeleri gerekiyor.",
        "İnsan bazen kendini birçok farklı ruh hali içinde bulabilir, önemli olan hepsini kabul etmek."
    ],
    "Zamanın akışını bir kenara bırakıp, dünün kararlarını bugüne taşımadan her anı sanki ilk kez yaşıyormuş gibi yaşamak istiyorum.": [
        "Zamanın yokluğu, aslında kendi zamanını yaratmak demek olabilir.",
        "Belki de her anı gerçekten 'ilk' kez yaşamayı seçmek, ruhsal bir yenilenme yoludur.",
        "Bu, hayatı daha derinden hissetmek için harika bir yaklaşım!"
    ],
    "Bir müzik parçasını defalarca dinleyip, aynı melodi içinde farklı anlamlar bulmak beni şaşırtıyor.": [
        "Müzik, bir dil gibi; her dinleyiş, yeni bir anlam katmanı açar.",
        "Belki de şarkı, içinde bir hikaye saklıyor ve her dinleyişte yeni bir sayfa aralanıyor.",
        "Müziğin büyüsü de burada: Her ruh hali için yeni bir anlam taşıyor."
    ],
    "Bir sabah uyandığımda, aynı kişinin yüzüne bakarken, onun kim olduğunu bir türlü anlayamadım.": [
        "Bu, belki de kim olduğumuzu her gün yeniden keşfetmenin bir yansımasıdır.",
        "Kimi zaman tanıdık yüzler bile yabancı gelebilir, belki de bakış açın değişiyor.",
        "Belki de insan, her gün yeniden doğuyor ve geçmiş benliklerinden ayrılıyor."
    ],
    "Bir çiçeğin, rüzgarla savrulup kaybolan yapraklarını izlerken, kendi kaybolmuş hislerimi hatırladım.": [
        "Bazen kaybolmak, yeniden bulunmanın başlangıcı olabilir.",
        "Bir şeyin kaybolması, ona başka bir şekilde var olma şansı tanır.",
        "Doğa, hislerimizi yansıtan bir aynadır; belki de o çiçek, senin bir parçanı anlatıyordur."
    ],
    "Bir tabloya bakarken, ressamın ruhunu hissettim ve bir anda onun duygularını yaşadığımı düşündüm.": [
        "Sanat, başkalarının içsel dünyalarını hissetme yoludur.",
        "Bir sanat eseri, duyguların bir dili gibi; belki de aslında hepimiz, aynı dili konuşuyoruz.",
        "Sanat bazen bir köprü gibidir; ruhları ve zamanları birbirine bağlar."
    ],
    "Bir çayın buharı, sabahın serinliğini hissettirirken, buharın içine karışan zamanın kokusunu nasıl tarif edebilirim ki?": [
        "Zamanın kokusu, belki de her anı içimizde barındıran bir izdir.",
        "O kokuyu, sadece o an yaşadığımızda duyabiliriz.",
        "Belki de çayın buharı, geçmiş ve gelecek arasındaki ince çizgiyi gösteriyordur."
    ],
    "Bir çocuğun gülen yüzünü görünce, kaybolan umutlarım bir an için geri geldi, ama hemen kayboldu yine.": [
        "Çocuklar, umutlarımızın en saf hali gibi.",
        "Onların gülen yüzü, aslında kaybolan tüm umutların bir yansımasıdır.",
        "Belki de kaybolan şeyler, sadece başka bir yerde bulmamız için kayboluyor."
    ],
    "Bir yolda yürürken, geçmişimle geleceğim arasında sıkışmış hissediyorum ve o an, her şeyin ne kadar küçük olduğunu fark ediyorum.": [
        "Belki de hayat, bu iki zaman dilimi arasında sıkışıp kalmamızla anlam kazanıyor.",
        "Geçmiş, geleceği şekillendiriyor, ama asıl büyük şey, bu anı gerçekten hissedebilmekte.",
        "Hayatta bazen sıkışmış hissetmek, aslında yeni yollar keşfetmek için bir fırsattır."
    ],
    "Bir gözlüğün camından dışarı bakarken, her şey biraz daha bulanık hale geliyor ve birden daha derin bir görüş elde ediyorum.": [
        "Bazen netlik, bir şeyin bulanıklaşmasında saklıdır.",
        "Belki de hayatta her şeyin anlamı, net olmayanlarda gizlidir.",
        "Gözlük bir araç olabilir, ama gerçek görüş, bazen gözlerimizden değil, ruhumuzdan gelir."
    ],
     "Bugün hava gerçekten çok güzel.": [
    "Evet, böyle günlerde dışarıda vakit geçirmek çok keyifli oluyor.",
    "Doğru, bu güzel havayı değerlendirmek gerek.",
    "Hava ne kadar güzel olsa da, içeriğe de bir şeyler yapmamız lazım."
  ],
  "Yeni bir diziye başladım, çok sarıyor.": [
    "Hangi dizi? Konusu nedir?",
    "Dizi önerilerine bayılırım, hangisini izliyorsun?",
    "Beni de dahil et, hangi platformda yayınlanıyor?"
  ],
  "Bu hafta sonu için planların var mı?": [
    "Henüz bir plan yapmadım, belki arkadaşlarımla buluşurum.",
    "Evet, ailemle birlikte küçük bir kaçamak yapmayı düşünüyoruz.",
    "Plan yapmadım ama açık hava konserine gitmeyi düşünüyordum."
  ],
  "Son zamanlarda hangi kitabı okudun?": [
    "Şu an bir psikoloji kitabı okuyorum, çok ilginç.",
    "Geçen hafta bir bilim kurgu romanı bitirdim, harikaydı.",
    "En son bir biyografi okudum, gerçek hayat hikâyeleri hep ilgimi çekmiştir."
  ],
  "Sence insanlar neden geç olana kadar öğrenmemekte ısrar ederler?": [
    "Belki de konfor alanlarından çıkmak istemediklerinden.",
    "Korkuları ve belirsizlikleri yüzünden değişime direniyor olabilirler.",
    "Alışkanlıklar, değişimi zorlaştırıyor; bu yüzden öğrenmekte geç kalıyorlar."
  ],
    "Uğur Böceği: Nasılsın?": [
        "Güçlerim yerinde, suçla mücadeleye hazırım! Sen nasılsın?",
        "Ladybug’un enerjisiyle doluyum, şehirdeki kötülüklere meydan okumaya hazırım!",
        "Biraz yorgunum ama Miraculous ruhum her zaman parlak, senin günün nasıl geçiyor?"
    ],
    "Şehrimizde barış hakim!": [
        "Evet, ama kötü güçler her an pusuya yatabilir. Hazırlıklı olmak gerek!",
        "Barış dolu günler, kahramanlarımızın emeklerinin sonucudur!",
        "Güzel hava ve huzur, Ladybug ve Kara Kedi’nin motive edici etkisiyle birleşince harika oluyor!"
    ],
    "Biraz Miraculous efsaneleri okumak istiyorum.": [
        "Hangi kahramanın maceraları ilgini çekiyor, Ladybug mu yoksa Kara Kedi mi?",
        "Harika fikir! Eski efsanelerde gizli güçleri keşfetmek her zaman ilham verici.",
        "Kahramanlık öyküleri, yeni stratejiler bulmana yardımcı olabilir. Hangi serüveni okuyacaksın?"
    ],
    "Göreve geç kaldım!": [
        "Her kahramanın zaman zaman aksilikleri olur, önemli olan yeniden ayağa kalkmak!",
        "Acele etme, Miraculous’ın gerçek gücü sabırda gizlidir.",
        "Bu sefer geç kaldın ama gelecek görevde Ladybug ve Kara Kedi’nin izinden daha hızlı koşarsın!"
    ],
    "Görev sonrası çok açım.": [
        "Kahramanların da enerjiye ihtiyacı var! Ne yemeyi planlıyorsun?",
        "Bir güzel croissant ya da sıcak bir kahve, belki de şehrin en iyi lezzeti sana iyi gelecektir.",
        "Görev sonrası kendini ödüllendirmek şart! Ne tarz bir atıştırmalık tercih edersin?"
    ],
    "Kara Kedi: Bugün nasılsın?": [
        "Bugün her şey mükemmel, sadece Ladybug’ı görmek için sabırsızlanıyorum!",
        "Hazırım! Şehirdeki kötülüklere karşı durmak için her zaman enerjik olmalıyım!",
        "Biraz yalnız hissediyorum ama Kara Kedi her zaman dostlarıyla güçlüdür!"
    ],
    "Ladybug: Harika bir gün!": [
        "Evet, tam da böyle günlerde kahramanlar görevde olmalı!",
        "Şehirde huzuru sağlamak için harika bir fırsat, değil mi?",
        "Havalar güzel, ama kötücüller yine pusuya yatabilir!"
    ],
    "Miraculous taşlarını keşfetmek istiyorum.": [
        "Harika fikir! Taşlar her zaman yeni güçlerin kaynağıdır, dikkatli ol!",
        "Ladybug ve Kara Kedi’nin taşları her zaman sırlarla doludur, hangi gücü keşfetmek istersin?",
        "Taşların sırrını çözmek, bir kahramanın görevi! Hazır mısın?"
    ],
    "Geceyi kaçırdım!": [
        "Geceyi kaçırmak sık olur ama kahramanlar için her an yeni bir mücadele başlar!",
        "Ladybug ve Kara Kedi her an hazırdır, geceyi kaybetmek önemli değil!",
        "Geceleri beklemek zor olabilir ama sabah yeni fırsatlar doğar!"
    ],
    "Bugün büyük bir savaş var!": [
        "Evet, ama her zaman olduğu gibi Ladybug ve Kara Kedi’nin yanında duracağım!",
        "Hazır ol, zafer bizim olacak! Miraculous güçleriyle her şey mümkün!",
        "Savaş büyük olabilir, ama dostluk ve cesaretle kazanacağız!"
    ],
    "Çok yorgunum, biraz dinlenmeliyim.": [
        "Evet, her kahramanın biraz dinlenmeye ihtiyacı vardır. Yarın yeni bir savaş bizi bekliyor!",
        "Kahramanlık zor bir iş! Dinlen, çünkü seni çok daha güçlü görmek istiyorum!",
        "Biraz rahatla, Ladybug ve Kara Kedi her zaman enerjik geri döner!"
    ],
    "Kahramanlık yapmak istiyorum!": [
        "Senin gibi birinin yardımına her zaman ihtiyacımız var! Hazırlıklı ol!",
        "Miraculous güçlerinle dünyayı değiştirebilirsin! Hangi kahramanı taklit etmek istersin?",
        "Hadi, şehri koruyalım! Ladybug ve Kara Kedi’nin izinden gidebilirsin!"
    ] 

}


# Tokenizer ile kelimeleri vektörleştirme
tokenizer = Tokenizer()
tokenizer.fit_on_texts(data.keys())
sequences = tokenizer.texts_to_sequences(data.keys())
padded_sequences = pad_sequences(sequences, padding='post')

# Yanıtları etiket olarak alalım
responses = list(data.values())

# Modeli oluştur
model = keras.Sequential([
    layers.Embedding(1000, 16, input_length=padded_sequences.shape[1]),
    layers.GlobalAveragePooling1D(),
    layers.Dense(320, activation='relu'),  # Daha fazla nöron ekledik
    layers.Dense(len(responses), activation='softmax')  # Çoklu sınıf çıktısı
])

# Modeli derle
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',  # Çoklu sınıf kaybı
              metrics=['accuracy'])

# Yanıt etiketlerini oluştur (cümle başına tek bir etiket)
labels = np.array([i for i in range(len(data))])

# Modeli eğit
model.fit(np.array(padded_sequences), labels, epochs=60, verbose=4)

# Gerçek zamanlı sohbet fonksiyonu
def chat():
    print("Merhaba! Benimle sohbet edebilirsin. Çıkmak için 'çık' yazabilirsin.")
    while True:
        user_input = input("Sen: ")
        if user_input.lower() == 'çık':
            print("Görüşmek üzere! 😊")
            break
        
        # Kullanıcıdan gelen inputu işleme
        sequence = tokenizer.texts_to_sequences([user_input])
        padded = pad_sequences(sequence, maxlen=padded_sequences.shape[1], padding='post')
        
        # Model ile tahmin yapma
        prediction = model.predict(padded)
        
        # En yüksek tahmin edilen yanıt indexini bulma
        response_index = np.argmax(prediction)  # En yüksek tahmin edilen yanıt
        response = responses[response_index]
        
        # Yanıtı yazdırma
        print(f"Asistan: {response[0]}")  # Yanıtların bir liste olduğunu unutma, ilk eleman alınıyor

# Sohbeti başlat
if __name__ == "__main__":
    chat()