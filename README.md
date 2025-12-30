
# Deploying a Containerized Remote Spec Service for a Control‑M Kubernetes Agent

## 📘 Introduction

This tutorial demonstrates how to build an OCI image for a simple template server, deploy it using Helm, and use it for **Control‑M Kubernetes jobs of type Remote Web Service**.

**OCI (Open Container Initiative)** defines standards for container images and runtimes to ensure interoperability across tools.
This tutorial uses Docker to build the image, but any OCI‑compliant tool may be used.

When a Control‑M Kubernetes job runs, the Control‑M/Agent requests a Job specification from the Template Server by providing a template name and parameters. The server renders the template and returns a complete Kubernetes Job spec (YAML).

---

## 📊 Deployment Flow Diagram

![deployment diagram](image.png)

---

## 🔧 Prerequisites

Make sure the following tools are installed:

- Docker: https://docs.docker.com/get-docker/
- Kubernetes + kubectl: https://kubernetes.io/docs/tasks/tools/
- Helm: https://helm.sh/docs/intro/install/
- Control‑M environment with an agent running in your Kubernetes cluster

---

## 🚀 Begin

### 1. Build the OCI image
```bash
docker build -t tpl-server:latest image
```

### 2. Verify the image exists
```bash
docker images | grep tpl-server
```

### 3. Tag & push the image to your registry
```bash
docker tag tpl-server:latest <my-repo>/tpl-server:latest
docker push <my-repo>/tpl-server:latest
```

### 4. Confirm the image is published
```bash
docker pull <my-repo>/tpl-server:latest
```

### 5. Download the Remote Job Spec sample files
https://github.com/controlm/ctm-kubernetes/tree/remote-tpl/01-Remote_Job_Specification_sample

### 6. Update the Helm chart values
Edit `chart/values.yaml`:
```yaml
image:
  repos: <my-repo>
```

### 7. Deploy the Template Server via Helm
```bash
helm install my-template-server ./chart
```

### 8. Check the pod status
```bash
kubectl get pods
kubectl describe pod <pod-name>
```

### 9. Create a Control‑M centralized connection profile
```
Name: K8STPLSVC
Namespace: your-namespace
Spec Endpoint URL: http://my-template-server-svc/jobspec
```

### 10. Customize `RemoteSpec_demoJob.json`
Update:
- ControlmServer
- Other environment‑specific fields

### 11. Run the job using Control‑M Automation API
```bash
ctm run RemoteSpec_demoJob.json
```

---

## 🧩 What Happens When the Control‑M Job Runs

1. Control‑M executes a RemoteSpec Kubernetes‑type job.
2. The agent sends a request to the Template Server (`tplserver.py`).
3. The server loads the requested template (e.g., `demo.yaml`) and injects job parameters.
4. Flask `render_template()` generates a fully rendered Kubernetes Job YAML.
5. Control‑M submits the generated spec as the actual job.

---

## 🛠️ Troubleshooting

### ImagePullBackOff
- Verify image name & tag
- Ensure registry access/authentication is correct

### Helm install issues
- Check `values.yaml` contains correct repo & tag

### View pod logs
```bash
kubectl logs <pod-name>
```

---
