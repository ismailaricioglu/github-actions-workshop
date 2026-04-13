# Gorev 18: Gate Pattern ile Required Checks

## Amac
Birden fazla kontrolu (lint, test, build) paralel calistirip, hepsinin basarili olmasini zorunlu kilan bir **gate pattern** workflow'u olusturun.

## Gereksinimler

- Dosya: `.github/workflows/gate.yml`
- Tetikleme: `main` branch'e PR acildiginda
- Uc paralel job tanimlayin:
  - `lint`: Python 3.11 kurup `flake8 app/ tests/` calistirsin
  - `test`: Python 3.11 kurup `pytest tests/ -v` calistirsin
  - `build`: Repo'daki `Dockerfile` ile Docker image build etsin
- Son bir `gate` job'i ekleyin:
  - `needs: [lint, test, build]` ile uc job'a bagli olsun
  - Sadece hepsi basarili olursa gecsin
  - `echo "All checks passed!"` yazsin

## Ipuclari

- Job'lar arasinda `needs` tanimlanmazsa default olarak paralel calisirlar
- Gate pattern: son bir job tum diger job'lara `needs` ile baglanir
- Gate job'unda `runs-on: ubuntu-latest` ve tek step yeterlidir
- Bu pattern, GitHub branch protection'da tek bir check (gate) izlemeyi kolaylastirir
- **Not:** Branch protection rule eklemek repo ayarlarindan yapilir (Settings > Branches), bu gorevde sadece workflow dosyasini olusturmaniz yeterlidir

## Test Etme
- PR acin, `lint`, `test`, `build` job'larinin paralel basladigini goruntuleyin
- Hepsi gecince `gate` job'unun basarili oldugunu dogrulayin
- Bilerek bir job'u fail ettirin (ornegin `app/main.py`'a kullanilmayan import ekleyin), `gate` job'unun da fail oldugunu gorun
- Duzeltip tekrar push edin, tum job'larin ve gate'in yesile donmesini dogrulayin
