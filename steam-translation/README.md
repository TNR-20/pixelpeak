# /steam-translation — çeviri kontrol sayfası

Steam mağaza sayfasının birebir kopyası, 16 dilde. Kontrol edenler paragraf
başına not bırakıp sana yolluyor.

## Kurulum

Bu klasörü (`steam-translation/`) siteyi barındıran reponun köküne, `index.html`
ile aynı seviyeye koy. Başka bir şey değişmiyor:

    /
    ├── index.html
    ├── assets/            ← Archivo fontları ve ikonlar buradan okunuyor
    └── steam-translation/
        ├── index.html
        └── assets/        ← sadece bu sayfanın videoları + kapsül görseli

Adres: **https://pixelpeak.games/steam-translation/**

## Dile özel linkler

    .../steam-translation/#schinese     简体中文
    .../steam-translation/#tchinese     繁體中文
    .../steam-translation/#japanese     日本語
    .../steam-translation/#koreana      한국어
    .../steam-translation/#thai         ไทย
    .../steam-translation/#russian      Русский
    .../steam-translation/#ukrainian    Українська
    .../steam-translation/#polish       Polski
    .../steam-translation/#german       Deutsch
    .../steam-translation/#french       Français
    .../steam-translation/#italian      Italiano
    .../steam-translation/#spanish      Español
    .../steam-translation/#dutch        Nederlands
    .../steam-translation/#brazilian    Português (BR)
    .../steam-translation/#turkish      Türkçe
    .../steam-translation/#english      English (kaynak)

Sayfadaki "Copy link for this language" butonu da aynı linki panoya kopyalar.

## Arama motorları

Sayfada `noindex, nofollow` var, `sitemap.xml`'e de eklenmedi — Google'a düşmez.
`robots.txt`'e bilerek `Disallow` yazmadım: crawl engellenirse `noindex`
etiketi de okunamıyor, o yüzden mevcut hâli daha güvenli.

Discord/WhatsApp'a link atınca düzgün önizleme çıksın diye OG etiketleri var
(kapsül görseli + "Read the Steam store page in your language").

## Metin güncellemek

Yeni bir çeviri dosyası çıktığında bu klasörde:

    python3 update-texts.py kayak-photography-sim-store-localization-v2_7.md --label v2.7

`index.html` içindeki metinleri değiştirir, başka hiçbir şeye dokunmaz.
Eskisini `index.html.bak` olarak saklar. Yazmadan önce kontrol ettikleri:

- her dilin kısa açıklaması 300 karakterin altında mı
- bütün diller aynı paragraf sayısına sahip mi (yoksa karşılaştırma modu ve
  geri gelen notlardaki paragraf numaraları kayar)
- metinde geçen `{STEAM_APP_IMAGE}/extras/...` klipleri `assets/` içinde var mı
- sayfanın render edemeyeceği bir BBCode etiketi var mı

Bir tanesi tutmazsa dosyayı hiç yazmaz, nedenini söyler.

`--label` sayfanın üstünde ve geri gelen notların başında görünür — kimin hangi
taslağa baktığı karışmasın diye. Şu an: **v2.6**

Markdown formatı şu olduğu sürece çalışır (mevcut dosyaların formatı):

    # Dil Adı — `steamkodu`
    ...
    ```
    kısa açıklama
    ```
    ...
    ```
    [p]uzun açıklama BBCode ile[/p]
    ```

## Notlar

Sunucu yok. Notlar kontrol edenin tarayıcısında (localStorage) duruyor,
"Send my notes" ile metin olarak kopyalanıp sana gönderiliyor.
