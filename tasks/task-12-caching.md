# Gorev 12: Dependency Caching

## Amac
Test workflow'unda Python bagimliklarini **cache'leyerek** workflow calisma suresini kisaltan bir workflow olusturun.

## Gereksinimler

- Dosya: `.github/workflows/cached-test.yml`
- Tetikleme: `main` branch'e PR acildiginda
- Python 3.11 kullanin
- `actions/cache` ile `pip` bagimliklarini cache'leyin
- Cache key olarak `requirements.txt` dosyasinin hash'ini kullanin
- Cache hit oldugunda `pip install` adimini atlayin
- Testleri `pytest` ile calistirin

## Ipuclari

- `actions/cache@v4` action'ini kullanin
- Cache path: `~/.cache/pip` (Linux runner'larda)
- Cache key formati: `${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}`
- `restore-keys` ile kısmi esleme yapin: `${{ runner.os }}-pip-`
- Cache hit kontrolu: `steps.cache.outputs.cache-hit`
- Ilk calistirmada cache olmayacak, ikincide hiz farkini gozlemleyin

## Test Etme
- PR acin, ilk calisma suresini not edin
- Ayni PR'a kucuk bir commit daha atin, ikinci calismanin daha hizli oldugunu dogrulayin
- `requirements.txt`'e yeni bir paket ekleyin, cache'in yeniden olusturuldugunu goruntuleyin
