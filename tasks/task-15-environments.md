# Gorev 15: Environment ve Secrets

## Amac
**Staging** ve **production** ortamlarini kullanan bir deploy simülasyonu workflow'u olusturun.

## Gereksinimler

- Dosya: `.github/workflows/deploy.yml`
- Tetikleme: `main` branch'e push yapildiginda
- Iki asamali deploy:
  1. **staging** environment'ina deploy (otomatik)
  2. **production** environment'ina deploy (manual approval gerekli)
- Her iki adimda da environment adini ve deploy zamanini loglara yazin
- Secret olarak `DEPLOY_TOKEN` kullanin (deger onemli degil, mekanizmayi ogrenin)

## Ipuclari

- Environment tanimlama: job seviyesinde `environment: staging`
- Production icin GitHub'da environment protection rule ekleyin (Settings > Environments)
- Required reviewers ekleyerek manual approval zorunlu kilin
- Secret'a erisim: `${{ secrets.DEPLOY_TOKEN }}`
- GitHub repo Settings > Environments'tan `staging` ve `production` ortamlarini olusturun
- Her environment icin ayri secret tanimlayabilirsiniz
- Deploy simülasyonu icin `echo "Deploying to $ENV..."` yeterlidir

## Test Etme
- `main` branch'e push yapin
- Staging deploy'un otomatik basladigini goruntuleyin
- Production deploy'un approval bekledigini goruntuleyin
- Approve edin ve production deploy'un tamamlandigini dogrulayin
- Settings > Environments'tan secret degerlerini kontrol edin
