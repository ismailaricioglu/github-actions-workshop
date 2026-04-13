# Gorev 6: Welcome Bot

## Amac
PR acildiginda PR'a otomatik **hosgeldin yorumu** yazan bir workflow olusturun.

## Gereksinimler

- Dosya: `.github/workflows/welcome.yml`
- Tetikleme: PR acildiginda
- PR'a yorum olarak su bilgileri iceren bir mesaj yazin:
  - PR acan kisiye hosgeldin mesaji (@mention ile)
  - Bir kontrol listesi (testler, format, lint)
- `gh` CLI kullanin

## Arastirma Konulari

- `gh pr comment` komutu nasil kullanilir?
- PR'a yorum yazmak icin hangi `permissions` gerekli?
- `pull_request` vs `pull_request_target` farki nedir? Hangisini secmelisiniz?

## Test Etme
- PR acin ve yorumun otomatik geldigini goruntuleyin
- Yorumda mention'in dogru oldugundan emin olun
