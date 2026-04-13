# Gorev 7: Security Scan Workflow

## Amac
PR acildiginda Python kodunda **bandit** ile guvenlik taramasi yapan bir workflow olusturun.

## Gereksinimler

- Dosya: `.github/workflows/security.yml`
- Tetikleme: `main` branch'e PR acildiginda
- `bandit` araci ile `app/` klasorunu tarayin
- Sadece medium ve high severity sorunlari raporlayin

## Arastirma Konulari

- `bandit` nedir ve ne tur guvenlik sorunlarini bulur?
- Severity filtreleme nasil yapilir? (`-ll` gibi flag'ler)
- Bandit cikti formatlari nelerdir? (json, txt vs.)

## Test Etme
- Mevcut kodun temiz gectigini dogrulayin
- Bilerek guvenliksiz kod ekleyin, ornekler:
  - `eval(user_input)`
  - `exec()` kullanimi
  - Hardcoded password: `password = "123456"`
- PR acin ve bandit'in bunlari yakalayip yakalamayacagini goruntuleyin
