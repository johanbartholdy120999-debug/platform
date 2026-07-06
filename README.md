# Platform Development Repository

## Formål

Dette repository anvendes til udvikling, test og vedligeholdelse af både **Platform** og **Mobile Platform** løsningen.

Repository'et indeholder den fælles udviklingsstruktur, hvor udviklere kan bidrage med ny funktionalitet, fejlrettelser og forbedringer til både frontend- og backend-komponenter.

---

# Projekter

## Platform

Platform-delen indeholder udviklingen af den primære platformsløsning.

Her arbejdes der med:
- Backend-udvikling
- Frontend-udvikling
- Integrationer
- API'er
- Forretningslogik
- Infrastrukturrelateret kode

Alle ændringer skal testes via det tilhørende GitHub Actions workflow, før kode accepteres.

---

## Mobile Platform

Mobile Platform-delen indeholder udviklingen af mobilplatformen.

Her arbejdes der med:
- Mobile frontend-komponenter
- Applikationslogik
- Kommunikation mellem mobilklient og backend
- Mobile integrationer

Ændringer skal ligeledes valideres gennem det tilhørende GitHub Actions workflow.

---

# CI/CD Workflows

Repository'et indeholder automatiske workflows til validering af kode.

Workflows udfører blandt andet:

- Kontrol af Python syntax
- Testkørsel
- Code quality checks
- Docker build og deployment (hvor relevant)

Når en udvikler pusher kode til repository'et, bliver workflowet automatisk startet og kontrollerer, at koden kan godkendes.

---

# Udviklingsproces

Udviklere skal følge denne proces:

1. Opret en ny branch fra `main`

Eksempel:

```bash
git checkout -b feature/navn-på-funktion
