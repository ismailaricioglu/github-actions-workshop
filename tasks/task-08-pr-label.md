# Gorev 8: Otomatik PR Label

## Amac
PR'da degisen dosyalarin konumuna gore otomatik **label** ekleyen bir workflow olusturun.

## Gereksinimler

- Iki dosya olusturmaniz gerekiyor:
  1. `.github/labeler.yml` — label kurallari
  2. `.github/workflows/labeler.yml` — workflow dosyasi
- Label kurallari:
  - `app/` altinda degisiklik → `app` labeli
  - `tests/` altinda degisiklik → `tests` labeli
  - `.github/` altinda degisiklik → `ci` labeli
  - `*.md` dosyalarinda degisiklik → `docs` labeli

## Arastirma Konulari

- `actions/labeler@v5` nasil kullanilir?
- `.github/labeler.yml` dosyasinin formati nasil olmali? (`changed-files` ve `any-glob-to-any-file` key'lerini arastirin)
- Workflow icin hangi `permissions` gerekli?

## Test Etme
- Sadece `app/` altinda degisiklik yapip PR acin → `app` labeli gelmeli
- Hem `app/` hem `tests/` degistirip PR acin → iki label birden gelmeli
