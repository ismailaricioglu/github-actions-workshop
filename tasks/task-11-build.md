# Gorev 11: Docker Build Workflow

## Amac
PR acildiginda uygulamayi **Docker image** olarak build eden bir workflow olusturun.

## Gereksinimler

- Dosya: `.github/workflows/build.yml`
- Tetikleme: `main` branch'e PR acildiginda
- Repo'daki `Dockerfile` kullanilarak image build edilsin
- Image'a anlamli bir tag verilsin (ornegin PR numarasi veya commit SHA)

## Ipuclari

- `docker build` komutu ile image olusturulur
- `docker build -t <isim>:<tag> .` seklinde tag verilir
- Commit SHA icin `${{ github.sha }}` kullanilabilir
- GitHub Actions runner'larinda Docker hazir yuklu gelir

## Test Etme
- PR acin ve build'in basarili tamamlandigini goruntuleyin
- Dockerfile'da bilerek hata yapin (ornegin yanlis COPY yolu), workflow fail etmeli
- Duzeltip tekrar push edin
