# Gorev 9: Scheduled Health Check (Cron)

## Amac
Belirli araliklarla testleri calistiran ve basarisiz olursa otomatik **issue acan** bir workflow olusturun.

## Gereksinimler

- Dosya: `.github/workflows/scheduled-health.yml`
- Tetikleme iki sekilde olsun:
  1. Her gun saat 09:00 UTC'de otomatik (cron)
  2. Manuel tetikleme butonu (Actions sekmesinden)
- Isleyis:
  1. Testleri calistir
  2. Testler **basarili** olursa: hicbir sey yapma
  3. Testler **basarisiz** olursa: otomatik issue ac (tarih ve workflow linkiyle)
- Onemli: testler fail etse bile workflow devam etmeli (issue acan adim calisabilsin)

## Arastirma Konulari

- `schedule` event'i ve cron syntax nasil yazilir?
- `workflow_dispatch` ne ise yarar?
- Bir adim fail ettiginde workflow'un devam etmesi icin ne yapilir? (`continue-on-error`)
- Onceki adimin sonucuna gore kosullu calistirma nasil yapilir? (`steps.<id>.outcome`, `if:`)

## Test Etme
- Actions sekmesinden "Run workflow" butonu ile manuel calistirin
- Testler geciyorsa issue olusturulmamali
- Bir testi bozun, commit edin, tekrar manuel calistirin → issue olusturulmali
