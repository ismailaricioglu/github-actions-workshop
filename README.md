# GitHub Actions Workshop

Basit bir Python Flask Todo API uzerinde GitHub Actions pratiqi yapacagiz.

## Repo Yapisi

```
├── app/
│   └── main.py          # Flask API (Todo CRUD, Math, Utils)
├── Dockerfile           # Docker build icin
├── tests/
│   └── test_app.py      # Pytest testleri
├── tasks/               # Her katilimcinin gorevi
├── .github/workflows/   # Workflow dosyalari buraya eklenir
├── requirements.txt
└── pyproject.toml
```

## Baslangic

```bash
# Repo'yu fork edin ve clone'layin
git clone https://github.com/<KULLANICI>/<REPO>.git
cd github-actions-workshop

# Sanal ortam olusturun
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Bagimliliklari yukleyin
pip install -r requirements.txt

# Testleri calistirin
pytest tests/ -v

# Uygulamayi calistirin
python -m app.main
```

## Nasil Calisacak?

1. Bu repo'yu **fork** edin
2. Asagidaki tablodan size atanan gorevi bulun
3. `tasks/` klasorundeki gorev dosyanizi okuyun
4. Yeni bir branch olusturun: `git checkout -b gorev-XX-isim`
5. `.github/workflows/` altina workflow dosyanizi yazin
6. Push edin ve **Pull Request** acin
7. Actions sekmesinden workflow'unuzun calistigini dogrulayin

## Gorev Atama Tablosu

| Participant | Gorev | Dosya | Zorluk |
|-------------|-------|-------|--------|
| Participant 1 | Linting (flake8) | [task-01](tasks/task-01-linting.md) | ⭐ |
| Participant 2 | Format Check (black + isort) | [task-02](tasks/task-02-format-check.md) | ⭐ |
| Participant 3 | Test Runner (pytest) | [task-03](tasks/task-03-tests.md) | ⭐ |
| Participant 4 | Matrix Strategy (coklu Python) | [task-04](tasks/task-04-multi-python.md) | ⭐⭐ |
| Participant 5 | Otomatik Issue Olusturma | [task-05](tasks/task-05-auto-issue.md) | ⭐⭐ |
| Participant 6 | Welcome Bot | [task-06](tasks/task-06-welcome-bot.md) | ⭐⭐ |
| Participant 7 | Security Scan (bandit) | [task-07](tasks/task-07-security-scan.md) | ⭐⭐ |
| Participant 8 | Otomatik PR Label | [task-08](tasks/task-08-pr-label.md) | ⭐⭐ |
| Participant 9 | Scheduled Health Check | [task-09](tasks/task-09-scheduled-health.md) | ⭐⭐ |
| Participant 10 | PR Diff Ozeti + Review | [task-10](tasks/task-10-ai-review.md) | ⭐⭐⭐ |
| Participant 11 | Docker Build | [task-11](tasks/task-11-build.md) | ⭐ |
| Participant 12 | Dependency Caching | [task-12](tasks/task-12-caching.md) | ⭐⭐ |
| Participant 13 | Artifact Upload/Download | [task-13](tasks/task-13-artifacts.md) | ⭐⭐ |
| Participant 14 | Reusable Workflow | [task-14](tasks/task-14-reusable-workflow.md) | ⭐⭐⭐ |
| Participant 15 | Environment & Secrets | [task-15](tasks/task-15-environments.md) | ⭐⭐⭐ |
| Participant 16 | Custom Composite Action | [task-16](tasks/task-16-composite-action.md) | ⭐⭐⭐ |
| Participant 17 | Concurrency Control | [task-17](tasks/task-17-concurrency.md) | ⭐⭐ |
| Participant 18 | Branch Protection + Required Checks | [task-18](tasks/task-18-branch-protection.md) | ⭐⭐⭐ |

## Onemli Notlar

- Her gorev birbirinden **bagimsizdir**, baska birinin gorevini beklemenize gerek yok
- Workflow dosyanizi `.github/workflows/` altina `.yml` uzantisiyla kaydedin
- PR actiginizda Actions sekmesinden workflow'unuzu takip edin
- Yesil tik = basarili, kirmizi X = basarisiz
- Basarisiz olursa Actions sekmesinden log'lari inceleyin ve duzeltip tekrar push edin

## API Endpoints

| Method | Endpoint | Aciklama |
|--------|----------|----------|
| GET | `/` | Hosgeldin mesaji |
| GET | `/health` | Saglik kontrolu |
| GET | `/todos` | Tum todo'lari listele |
| POST | `/todos` | Yeni todo olustur |
| GET | `/todos/<id>` | Tek todo getir |
| PUT | `/todos/<id>` | Todo guncelle |
| DELETE | `/todos/<id>` | Todo sil |
| GET | `/math/add?a=1&b=2` | Toplama |
| GET | `/math/multiply?a=3&b=4` | Carpma |
| GET | `/utils/factorial/5` | Faktoriyel |
| GET | `/utils/palindrome?text=racecar` | Palindrom kontrolu |
