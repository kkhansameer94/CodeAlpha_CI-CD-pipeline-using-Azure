# CodeAlpha CI/CD Pipeline using Azure

[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen)](https://github.com/kkhansameer94/CodeAlpha_CI-CD-pipeline-using-Azure)
[![Azure DevOps](https://img.shields.io/badge/Azure%20DevOps-CI%2FCD-0078D4)](https://azure.microsoft.com/products/devops/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED)](https://www.docker.com/)
[![Azure Container Registry](https://img.shields.io/badge/Azure%20Container%20Registry-ACR-0078D4)](https://azure.microsoft.com/products/container-registry/)
[![Azure App Service](https://img.shields.io/badge/Azure%20App%20Service-Deployed-0078D4)](https://azure.microsoft.com/products/app-service/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Project Overview

An end-to-end CI/CD pipeline for deploying a containerized application to Microsoft Azure.

This project demonstrates automated Continuous Integration and Continuous Deployment using Azure DevOps, Docker, Azure Container Registry (ACR), and Azure App Service.

The pipeline automates the application lifecycle from source-code commit to container build, testing, image publishing, and cloud deployment.

## Technologies

- Azure DevOps
- Azure Pipelines
- Docker
- Azure Container Registry (ACR)
- Azure App Service
- Python
- Git
- GitHub
- Azure CLI

## Architecture

```text
Developer
    |
    | Git Push
    v
GitHub Repository
    |
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
    | Pull Docker Image
    v
Azure App Service
    |
    v
Running Application
