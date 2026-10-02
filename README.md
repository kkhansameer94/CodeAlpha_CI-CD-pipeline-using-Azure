# CodeAlpha CI/CD Pipeline using Azure

[![Build](https://img.shields.io/badge/Build-Passing-brightgreen.svg)](https://github.com/kkhansameer94/CodeAlpha_CI-CD-pipeline-using-Azure)
[![Azure DevOps](https://img.shields.io/badge/Azure%20DevOps-CI%2FCD-0078D4?logo=azuredevops&logoColor=white)](https://azure.microsoft.com/products/devops/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![Azure Container Registry](https://img.shields.io/badge/Azure%20Container%20Registry-ACR-0078D4?logo=microsoftazure&logoColor=white)](https://azure.microsoft.com/products/container-registry/)
[![Azure App Service](https://img.shields.io/badge/Azure%20App%20Service-Deployed-0078D4?logo=microsoftazure&logoColor=white)](https://azure.microsoft.com/products/app-service/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> An end-to-end CI/CD pipeline for deploying a containerized Python web application using Azure DevOps, Docker, Azure Container Registry (ACR), and Azure App Service.

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Docker](#docker)
- [Azure Deployment](#azure-deployment)
- [CI/CD Pipeline](#cicd-pipeline)
- [Configuration](#configuration)
- [Monitoring](#monitoring)
- [Security](#security)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## Overview

The CodeAlpha CI/CD Pipeline using Azure automates the deployment lifecycle of a containerized Python web application.

A code push to the main branch can trigger the Azure DevOps pipeline to build the application, run tests, create a Docker image, push the image to Azure Container Registry, and deploy the container to Azure App Service.

### Workflow

```text
Developer
   |
   v
GitHub Repository
   |
   | Push
   v
Azure DevOps Pipeline
   |
   +---- Build
   |
   +---- Test
   |
   +---- Docker Build
   |
   v
Azure Container Registry
   |
   | Pull Image
   v
Azure App Service
   |
   v
Running Application
```

## Architecture

The project uses a container-based cloud deployment architecture:

```text
+------------------+
|     Developer    |
+--------+---------+
         |
         | Git Push
         v
+------------------+
| GitHub Repository|
+--------+---------+
         |
         v
+------------------+
|  Azure DevOps    |
|    Pipelines     |
+--------+---------+
         |
         +----------------+
         |                |
         v                v
   +-----------+    +-----------+
   |   Build   |    |   Tests   |
   +-----------+    +-----------+
         \                /
          \              /
           v            v
        +------------------+
        | Docker Image     |
        +--------+---------+
                 |
                 v
        +------------------+
        | Azure Container  |
        | Registry (ACR)   |
        +--------+---------+
                 |
                 v
        +------------------+
        | Azure App Service|
        +--------+---------+
                 |
                 v
        +------------------+
        | Production App   |
        +------------------+
```

## Features

- Automated CI/CD pipeline
- Azure DevOps integration
- Automated build and testing
- Docker containerization
- Azure Container Registry integration
- Automated Docker image tagging
- Azure App Service deployment
- Containerized cloud hosting
- Build and deployment logging
- Runtime monitoring
- Repeatable deployment workflow
- Git-based source control
- Cloud-ready application delivery

## Technology Stack

| Technology | Purpose |
|---|---|
| Azure DevOps | CI/CD automation |
| Azure Pipelines | Build and deployment workflow |
| Docker | Application containerization |
| Azure Container Registry | Private container image registry |
| Azure App Service | Cloud application hosting |
| Python 3.11 | Application runtime |
| Git | Version control |
| GitHub | Source-code hosting |
| Azure CLI | Azure resource management |

## Project Structure

```text
CodeAlpha_CI-CD-pipeline-using-Azure/
│
├── azure-pipelines.yml
├── Dockerfile
├── .dockerignore
├── .gitignore
├── requirements.txt
├── LICENSE
├── CONTRIBUTING.md
├── README.md
│
├── src/
│   └── app.py
│
├── tests/
│   └── test_app.py
│
└── docs/
    └── screenshots/
        ├── azure-devops-pipeline.png
        ├── azure-app-service.png
        └── architecture.png
```

## Screenshots

### CI/CD Pipeline

![Azure DevOps Pipeline](Screenshot.png)

### CI/CD Architecture

![CI/CD Architecture](docs/screenshots/architecture.png)

### Azure App Service

![Azure App Service](docs/screenshots/azure-app-service.png)

> If a screenshot file is not present in the repository, upload the corresponding image to the path used above.

## Prerequisites

Before running this project, install:

- Git
- Python 3.11 or later
- Docker
- Azure CLI
- An Azure account
- An Azure DevOps organization/project

Verify the installations:

```bash
git --version
python --version
docker --version
az --version
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/kkhansameer94/CodeAlpha_CI-CD-pipeline-using-Azure.git
```

### 2. Enter the Project Directory

```bash
cd CodeAlpha_CI-CD-pipeline-using-Azure
```

### 3. Create a Python Virtual Environment

```bash
python -m venv venv
```

Activate on Linux/macOS:

```bash
source venv/bin/activate
```

Activate on Windows:

```powershell
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Run the Application Locally

```bash
python src/app.py
```

### Build the Docker Image

```bash
docker build -t codealpha-app:latest .
```

### Run the Docker Container

```bash
docker run -d -p 8080:8080 --name codealpha-app codealpha-app:latest
```

### Verify the Application

```bash
curl http://localhost:8080
```

### Check Running Containers

```bash
docker ps
```

### View Container Logs

```bash
docker logs codealpha-app
```

### Stop the Container

```bash
docker stop codealpha-app
```

### Remove the Container

```bash
docker rm codealpha-app
```

## Testing

Run the automated test suite:

```bash
pytest
```

Run tests with verbose output:

```bash
pytest -v
```

The CI/CD pipeline should execute tests before the Docker image is deployed.

## Docker

Build the image:

```bash
docker build -t codealpha-app:latest .
```

Run the image:

```bash
docker run -d -p 8080:8080 codealpha-app:latest
```

Inspect Docker images:

```bash
docker images
```

Inspect running containers:

```bash
docker ps
```

## Azure Deployment

### Login to Azure

```bash
az login
```

### Check the Active Subscription

```bash
az account show
```

### Login to Azure Container Registry

```bash
az acr login --name <ACR_NAME>
```

### Build and Tag the Image

```bash
docker build -t <ACR_NAME>.azurecr.io/codealpha-app:latest .
```

### Push the Image to ACR

```bash
docker push <ACR_NAME>.azurecr.io/codealpha-app:latest
```

Configure Azure App Service to use the container image stored in Azure Container Registry.

## CI/CD Pipeline

The Azure DevOps pipeline follows these stages:

1. Source code checkout
2. Dependency installation
3. Application build
4. Automated testing
5. Docker image build
6. Docker image tagging
7. Push image to Azure Container Registry
8. Deploy container to Azure App Service
9. Monitor application and deployment logs

### Pipeline Flow

```text
Git Push
   |
   v
Checkout
   |
   v
Build
   |
   v
Test
   |
   v
Docker Build
   |
   v
Tag Image
   |
   v
Push to ACR
   |
   v
Deploy to App Service
   |
   v
Monitor
```

## Configuration

Typical deployment configuration values include:

```text
AZURE_SUBSCRIPTION_ID
AZURE_RESOURCE_GROUP
AZURE_REGION
AZURE_CONTAINER_REGISTRY
AZURE_APP_SERVICE
```

Store sensitive values in secure Azure DevOps pipeline variables or service connections.

Never commit passwords, access tokens, service-principal credentials, or other secrets to the repository.

## Monitoring

Application and deployment monitoring can use:

- Azure Monitor
- Application Insights
- Azure App Service logs
- Container logs
- Azure DevOps pipeline logs

Example App Service log command:

```bash
az webapp log tail \
  --name <APP_NAME> \
  --resource-group <RESOURCE_GROUP>
```

## Security

Security practices for this project include:

- Never commit credentials or secrets
- Use Azure DevOps secret variables
- Use secure Azure service connections
- Apply least-privilege permissions
- Keep Docker images updated
- Use `.dockerignore`
- Scan container images for vulnerabilities
- Restrict access to Azure resources

## Troubleshooting

### Docker Container Does Not Start

Check the logs:

```bash
docker logs codealpha-app
```

Check all containers:

```bash
docker ps -a
```

### Azure Container Registry Authentication Fails

```bash
az login
az acr login --name <ACR_NAME>
```

### Azure Deployment Fails

Check:

- Azure DevOps service connection
- Azure subscription
- Resource group
- Azure Container Registry
- Docker image name
- Docker image tag
- Azure App Service configuration
- Application logs
- Container startup configuration

## Contributing

Contributions, bug reports, documentation improvements, and feature suggestions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Run the tests.
5. Commit your changes.
6. Push your branch.
7. Open a Pull Request.

See [CONTRIBUTING.md](CONTRIBUTING.md) for additional contribution guidelines.

## License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE) file for the complete license text.

## Author

**Sameer Khan**

GitHub: https://github.com/kkhansameer94

## Support

If you find this project useful, consider giving the repository a star.

---

## DevOps Workflow Summary

**GitHub → Azure DevOps → Build → Test → Docker → Azure Container Registry → Azure App Service → Monitoring**
