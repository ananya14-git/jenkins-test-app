# Jenkins CI/CD Project Summary

## 🎯 What I Built
A complete CI/CD pipeline that automatically:
- Detects code changes in GitHub
- Runs tests automatically
- Builds Docker images
- Pushes to Docker Hub
- Deploys containers

## 🛠️ Technologies Used
- Jenkins (CI/CD server)
- GitHub (source control)
- Docker (containerization)
- Python (sample application)
- Groovy (pipeline scripting)

## 📁 Project Structure
jenkins-test-app/
├── app.py # Main application
├── test_app.py # Unit tests
├── Dockerfile # Container config
├── Jenkinsfile # Pipeline definition
├── README.md # Documentation
└── .gitignore # Git ignore file

text

## 📊 Pipeline Stages Explained

| Stage | Purpose |
|-------|---------|
| Checkout | Pull latest code from GitHub |
| Build | Verify build environment |
| Test | Run unit tests |
| Build Docker | Create container image |
| Push to Hub | Upload to Docker registry |
| Run Container | Verify deployment |

## ✅ Skills Demonstrated
- CI/CD pipeline configuration
- Infrastructure as Code (Jenkinsfile)
- Containerization with Docker
- Version control with Git
- Automated testing
- Artifact management
