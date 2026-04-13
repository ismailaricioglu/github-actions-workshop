# Gorev 5: Otomatik Issue Olusturma

## Amac
Yeni bir PR acildiginda otomatik olarak bir review **issue**'su olusturan workflow yazin.

## Gereksinimler

- Dosya: `.github/workflows/auto-issue.yml`
- Tetikleme: PR **ilk acildiginda** (sadece opened, synchronize degil)
- Issue icerigi:
  - Baslik: PR numarasi ve basligi icermeli
  - Body: PR'i acan kisi, branch adi ve PR linki olmali
- `gh` CLI kullanin (GitHub Actions'da hazir yuklu gelir)

## Arastirma Konulari

- `pull_request` event'inin `types` filtresi nasil calisir?
- `permissions` altinda `issues: write` neden gerekli?
- `github.event.pull_request` context'inden hangi bilgiler alinabilir?
- `gh issue create` komutunun parametreleri neler?

## Test Etme
- PR acin, Issues sekmesinde otomatik issue goruntuleyin
- Issue iceriginde PR bilgilerinin dogru oldugundan emin olun
