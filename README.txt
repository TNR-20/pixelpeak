PIXELPEAK — SITE (Contact butonu eklendi)

CONTACT BUTONU
  Açıklamanın altına sade, çerçeveli bir "Contact" butonu eklendi.
  LinkedIn'e yönlendiriyor, yeni sekmede açılıyor.

  !!! YAPMAN GEREKEN TEK ŞEY !!!
  index.html içinde şunu bul:
      href="PASTE_YOUR_LINKEDIN_URL_HERE"
  ve tırnakların arasına kendi LinkedIn linkini yapıştır. Örnek:
      href="https://www.linkedin.com/in/kullanici-adin/"

  Bulmak için: index.html'i metin editöründe aç, Ctrl+F ile
  "PASTE_YOUR_LINKEDIN" ara. Ya da GitHub'da dosyayı düzenlerken
  (pencil ikonu) aynı şekilde bul-değiştir yap.

  Linki yapıştırmadan yüklersen buton çalışmaz (o yazıya gider).

YÜKLEME
  Sadece index.html değişti.
    Add file > Upload files > index.html > Commit
  Hard refresh: Ctrl+Shift+R

STİL NOTU
  Buton bilinçli olarak sade: ince beyaz çerçeve, hover'da
  hafif parlıyor. Sayfanın minimal havasını bozmuyor. Rengini
  ya da dolgusunu değiştirmek istersen .contact { } bloğu
  index.html <style> içinde.
