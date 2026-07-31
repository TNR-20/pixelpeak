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

Çeviriler `index.html` içinde `const LANGS = [...]` satırında JSON olarak duruyor.
BBCode olduğu gibi saklanıyor, sayfa render ederken çeviriyor — yani Steam'e
yapıştıracağın metnin aynısı burada.

## Notlar

Sunucu yok. Notlar kontrol edenin tarayıcısında (localStorage) duruyor,
"Send my notes" ile metin olarak kopyalanıp sana gönderiliyor.
