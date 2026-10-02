# ☁️ CodeAlpha: CI/CD Pipeline using Azure (Task 1)

[![Azure DevOps](https://img.shields.io/badge/Azure%20Pipelines-0078D7?logo=azuredevops&logoColor=white)](https://azure.microsoft.com/en-us/products/devops/)
[![Docker](https://img.shields.io/badge/Container-ACR-0089D6?logo=docker&logoColor=white)](https://azure.microsoft.com/en-us/products/container-registry/)
[![Azure App Service](https://img.shields.io/badge/Compute-Azure%20App%20Service-0078D4?logo=microsoftazure&logoColor=white)](https://azure.microsoft.com/en-us/products/app-service/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An enterprise-ready automated CI/CD pipeline built using **Azure DevOps Pipelines**, containerizing web workloads into **Azure Container Registry (ACR)**, and deploying automatically to **Azure App Service**.

---

## 📸 Screenshots

<p align="center">
  <img src="https://raw.githubusercontent.com/kkhansameer94/CodeAlpha_CI-CD-pipeline-using-Azure/main/src/app.py" alt="Azure Architecture Workflow" width="700"/>
</p>

---

## 📌 Architecture & Deliverables

* **Source Control**: GitHub repository integration triggering automated builds on `main`.
* **Container Registry**: Packaging web app artifacts into Azure Container Registry (ACR).
* **Automated CD**: Deploying container instances into Azure App Service without manual intervention.
* **Observability**: Execution logs and runtime monitoring via Azure Pipelines telemetry.

---

## 🛠 Project Layout

```text
├── azure-pipelines.yml     # Multi-stage CI/CD workflow
├── Dockerfile              # Container definition
├── src/
│   └── app.py              # Web application
├── .gitignore              # Ignored cache artifacts
└── README.md               # Technical overview
