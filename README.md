# Book API – Projekt DevOps

## Opis projektu

Book API to prosta aplikacja REST API napisana w **FastAPI**, wdrożona do **Amazon ECS Fargate** z wykorzystaniem kompletnego procesu CI/CD.

Celem projektu było przygotowanie nowoczesnego środowiska DevOps obejmującego konteneryzację aplikacji, automatyczne testy, wdrożenie infrastruktury jako kodu oraz automatyczne publikowanie nowych wersji aplikacji w chmurze AWS.

---
## Publiczny adres aplikacji

Aplikacja jest dostępna pod adresem:

http://18.196.29.196:8000

Przykładowe endpointy:

- http://18.196.29.196:8000:8000/health
- http://18.196.29.196:8000/version
- http://18.196.29.196:8000/books

> Uwaga: aplikacja została wdrożona w Amazon ECS Fargate z wykorzystaniem publicznego adresu IP. W przypadku ponownego wdrożenia adres IP może ulec zmianie.

# Architektura rozwiązania

```text
Programista
      │
      ▼
Repozytorium GitHub
      │
      ▼
GitHub Actions
 ├── Uruchomienie testów
 ├── Budowa obrazu Docker
 ├── Publikacja obrazu do Amazon ECR
 └── Automatyczne wdrożenie do Amazon ECS
                      │
                      ▼
               Amazon ECS Fargate
                      │
                      ▼
                 Aplikacja FastAPI
                      │
                      ▼
             Amazon CloudWatch Logs
```

---

# Wykorzystane technologie

* Python 3.9
* FastAPI
* SQLAlchemy
* SQLite
* Pytest
* Docker
* GitHub Actions
* Terraform
* Amazon ECS Fargate
* Amazon ECR
* Amazon CloudWatch
* AWS IAM

---

# Struktura projektu

```text
book-api/
├── app/
├── tests/
├── terraform/
├── .github/
│   └── workflows/
│       └── ci.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# Funkcjonalność aplikacji

Aplikacja udostępnia następujące endpointy REST:

| Metoda | Endpoint   | Opis                          |
| ------ | ---------- | ----------------------------- |
| GET    | `/health`  | Sprawdzenie stanu aplikacji   |
| GET    | `/version` | Wyświetlenie wersji aplikacji |
| GET    | `/books`   | Pobranie listy książek        |

---

# Proces CI/CD

Po każdym wysłaniu zmian (`git push`) do gałęzi **main** wykonywane są automatycznie następujące kroki:

1. Pobranie kodu z repozytorium GitHub.
2. Instalacja zależności projektu.
3. Uruchomienie testów jednostkowych (`pytest`).
4. Budowa obrazu Docker.
5. Publikacja obrazu do repozytorium Amazon ECR.
6. Automatyczne wdrożenie nowej wersji aplikacji do Amazon ECS Fargate.

Dzięki temu każda nowa wersja aplikacji jest publikowana bez konieczności ręcznego wdrażania.

---

# Infrastruktura jako kod (Terraform)

Cała infrastruktura została utworzona z wykorzystaniem narzędzia Terraform.

Tworzone są następujące zasoby:

* Repozytorium Amazon ECR
* Klaster Amazon ECS
* Definicja zadania (Task Definition)
* Usługa Amazon ECS
* Role IAM
* Security Group
* Grupa logów Amazon CloudWatch

---

# Uruchomienie aplikacji lokalnie

Instalacja zależności:

```bash
pip install -r requirements.txt
```

Uruchomienie aplikacji:

```bash
uvicorn app.main:app --reload
```

Dokumentacja Swagger będzie dostępna pod adresem:

```text
http://localhost:8000/docs
```

---

# Uruchomienie testów

```bash
pytest
```

---

# Docker

Budowa obrazu:

```bash
docker build -t book-api .
```

Uruchomienie kontenera:

```bash
docker run -p 8000:8000 book-api
```

---

# Efekt końcowy

Po zakończeniu projektu aplikacja:

* działa w środowisku Amazon ECS Fargate,
* jest dostępna z poziomu Internetu,
* automatycznie przechodzi testy przy każdej zmianie kodu,
* automatycznie buduje nowy obraz Docker,
* automatycznie publikuje obraz do Amazon ECR,
* automatycznie wdraża nową wersję aplikacji po wykonaniu `git push`.

---

# Możliwe kierunki rozwoju

Projekt można w przyszłości rozszerzyć o:

* Application Load Balancer (ALB),
* własną domenę i certyfikat HTTPS,
* bazę PostgreSQL zamiast SQLite,
* monitoring i metryki aplikacji,
* automatyczny rollback po nieudanym wdrożeniu,
* wdrożenia Blue/Green.

---

# Autor

Projekt został wykonany w ramach nauki technologii DevOps z wykorzystaniem:

* FastAPI,
* Docker,
* Terraform,
* GitHub Actions,
* Amazon Web Services (AWS).

