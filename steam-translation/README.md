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

Sayfa metinleri **`texts.md`** dosyasından, açılırken okuyor. Yani sunucudaki
`texts.md`'yi değiştirip push'lamak yeterli — `index.html`'e dokunmana gerek yok.
Dosya adı tam olarak `texts.md` olmalı ve `index.html` ile aynı klasörde durmalı.

`index.html` içinde metinlerin bir kopyası daha var; sadece `texts.md` çekilemezse
(dosyayı bilgisayarında `file://` ile açtığında, ya da dosya eksikse) devreye giriyor.

Güvenli yol, ikisini birden güncelleyen script:

    python3 update-texts.py yeni-dosya.md --label v2.8

Yaptıkları: dosyayı kontrol eder, `texts.md` olarak yazar, `index.html` içindeki
yedek kopyayı da tazeler, eskisini `index.html.bak` olarak saklar. Kontrolleri:

- her dilin kısa açıklaması 300 karakterin altında mı (300'e 15'ten yakınsa uyarır)
- diller arasında paragraf sayısı farkı var mı — **durdurmaz**, uyarır. Farklı olan
  dilin karşılaştırma görünümü paragraf paragraf değil, iki metin yan yana olur.
- metinde geçen `{STEAM_APP_IMAGE}/extras/...` klipleri `assets/` içinde var mı
- sayfanın render edemeyeceği bir BBCode etiketi var mı

`--label` sayfanın üstünde ve geri gelen notların başında görünür — kimin hangi
taslağa baktığı karışmasın diye. Script bunu `texts.md`'nin ilk satırına
`<!-- label: v2.8 -->` olarak yazar; elle düzenlersen o satırı güncelle.

Tarayıcı cache'i: sayfa `texts.md`'yi `no-store` ile çekiyor, ama GitHub Pages'in
CDN'i birkaç dakika eski dosyayı verebilir. Hemen görmek istersen hard refresh
(Ctrl+Shift+R).

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
