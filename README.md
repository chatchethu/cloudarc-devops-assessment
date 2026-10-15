# CloudArc DevOps Assessment

A small Flask web application demonstrating Docker containerization, automated testing, Git-based version control, and continuous integration using GitHub Actions.

## 1. Project Overview

| Endpoint | Description |
|---|---|
| `/` | Returns the application name, runtime status, and environment. |
| `/health` | Returns `{"status": "healthy"}` with HTTP 200. |

## 2. Architecture

```
Developer → Git (GitHub) → GitHub Actions
                                 │
                    ┌────────────┴────────────┐
                    ▼                         ▼
             Run pytest              Build Docker image
                                   (only if tests pass)
```

## 3. Technologies

- Python 3.12 · Flask · pytest
- Docker · Git · GitHub Actions
- Ubuntu CI runners · Windows PowerShell (local dev)

## 4. Project Structure

```
cloudarc-devops-assessment/
├── .github/workflows/ci.yml
├── tests/test_app.py
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```

## 5. Prerequisites

Python 3.12+, Git, Docker Desktop (running).

```powershell
python --version
git --version
docker --version
docker info
```

## 6. Run Locally (Windows)

```powershell
git clone https://github.com/chatchethu/cloudarc-devops-assessment.git
cd cloudarc-devops-assessment

py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1

python -m pip install -r requirements.txt
python -m pytest -v

python app.py
```

In a second terminal:

```powershell
Invoke-RestMethod http://127.0.0.1:5000/
Invoke-RestMethod http://127.0.0.1:5000/health
```

Stop with `Ctrl+C`.

## 7. Build and Run with Docker

```powershell
docker build -t cloudarc-app:1.0 .

docker run -d `
  --name cloudarc-app `
  -p 127.0.0.1:5000:5000 `
  -e APP_ENV=production `
  cloudarc-app:1.0

Invoke-RestMethod http://127.0.0.1:5000/
Invoke-RestMethod http://127.0.0.1:5000/health

docker stop cloudarc-app
docker rm cloudarc-app
```

## 8. Environment Configuration

`APP_ENV` defaults to `development`. Override at runtime:

```powershell
docker run --rm -p 127.0.0.1:5000:5000 -e APP_ENV=production cloudarc-app:1.0
```

Never commit secrets or credentials to Git or bake them into images.

## 9. CI/CD Workflow

File: `.github/workflows/ci.yml`

Triggers: push to `main`, pull requests targeting `main`.

Steps:
1. Checkout source code
2. Set up Python 3.12
3. Install dependencies
4. Run pytest
5. Build Docker image *(only if tests pass)*

## 10. Troubleshooting

**Container exits unexpectedly**
```powershell
docker ps -a
docker logs cloudarc-app
```

**Port conflict** — stop the conflicting process or map a different host port (`5001:5000`).

**Tests fail** — run `python -m pytest -v` locally, check the first error, fix, and push.

**CI fails** — open the failed GitHub Actions step, read the error, fix the issue, commit, and push.

## 11. Known Limitations

- No database or persistent storage
- No container registry publishing
- No production WSGI server (Gunicorn/uWSGI)
- No cloud deployment
- No vulnerability scanning

## 12. Future Improvements

- Pin Actions to full commit SHAs
- Add linting (flake8/ruff) and type checking (mypy)
- Publish versioned images to Docker Hub or GHCR
- Add Docker health check (`HEALTHCHECK` instruction)
- Deploy to a cloud VM or managed container service
- Add secrets management and monitoring

## 13. Technical Challenges and Resolutions

- **Container connectivity:** Flask binds to `0.0.0.0` so Docker port mapping works correctly.
- **Configuration:** `APP_ENV` env var with `development` default keeps config out of code.
- **Automated validation:** pytest + GitHub Actions runs tests before every Docker build.
- **Reproducibility:** Bounded dependency version ranges (`>=min,<max`) in `requirements.txt` and documented commands ensure consistent results across environments.

## 14. Author and Repository

Author: Chethan T  
Repository: https://github.com/chatchethu/cloudarc-devops-assessment
