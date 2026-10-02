# CodeAlpha CI CD Pipeline using Azure

[![Build](https://img.shields.io/badge/Build-Passing-brightgreen.svg)](https://github.com/kkhansameer94/CodeAlpha_CI-CD-pipeline-using-Azure)
[![Azure DevOps](https://img.shields.io/badge/Azure%20DevOps-0078D4?logo=azuredevops&logoColor=white)](https://dev.azure.com/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![Azure App Service](https://img.shields.io/badge/Azure%20App%20Service-0089D6?logo=microsoftazure&logoColor=white)](https://azure.microsoft.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An automated continuous integration and continuous deployment (CI/CD) pipeline built using Azure DevOps, Docker, Azure Container Registry (ACR), and Azure App Service.

## Screenshots

![Pipeline Workflow](https://raw.githubusercontent.com/kkhansameer94/CodeAlpha_CI-CD-pipeline-using-Azure/main/Screenshot.png)

## Overview

The CodeAlpha CI/CD Pipeline using Azure project automates the deployment lifecycle of a containerized Python web application. Every commit pushed to the main branch triggers Azure DevOps Pipelines to build the application container, package artifacts, push images to Azure Container Registry, and deploy directly to Azure App Service without manual intervention.

## Project Structure

```text
.
├── azure-pipelines.yml     # Multi-stage CI/CD workflow pipeline definition
├── Dockerfile              # Production Python 3.11 container definition
├── src/
│   └── app.py              # Lightweight HTTP web service application
├── .dockerignore           # Build context exclusion rules
├── .gitignore              # Repository file exclusion rules
└── README.md               # Technical project documentation
