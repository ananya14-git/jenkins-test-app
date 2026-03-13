# Jenkins Test Application

[![Build Status](http://localhost:8080/buildStatus/icon?job=python-test-app-pipeline)](http://localhost:8080/job/python-test-app-pipeline/)

A simple Python application to demonstrate Jenkins CI/CD pipeline.

## 📋 Pipeline Stages
1. Checkout Code
2. Build
3. Test
4. Build Docker Image
5. Push to Docker Hub
6. Run Container

## 🚀 How to Trigger
- Push to GitHub main branch
- Manual build in Jenkins

## 📊 Pipeline Status
![Pipeline](https://via.placeholder.com/800x400?text=Jenkins+Pipeline+View)
=======
# jenkins-test-app
A Jenkins job that pulls a simple "Hello World" code from your GitHub, builds it (e.g., a simple C program or Java jar), and emails the build status.
