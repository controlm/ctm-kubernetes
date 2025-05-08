# Tutorial: Deploying a containerized Remote Spec Service for the Control-M Kubernetes Agent

This tutorial demonstrates how to build an OCI image for a simple template server, deploy it using Helm, and use it for Control-M Kubernetes Jobs.


## 📦 Overview

- **Docker**: Containerize your application  
- **Helm**: Deploy it to a Kubernetes cluster  
- **Control-M**: Automate the deployment as a scheduled job

---

## Steps

## 🔧 Prerequisites

Before you start, ensure you have the following tools installed and configured:

- [Docker](https://docs.docker.com/get-docker/)
- [Kubernetes](https://kubernetes.io/docs/tasks/tools/) (with a working `kubectl` setup)  
- [Helm](https://helm.sh/docs/intro/install/)  
- Access to a **Control-M** environment including an agent deployed in the Kubernetes cluster

---

## 🚀 1. Build the OCI Image

To begin, create the image by running the following command:

```bash
 docker build -t tpl-server:latest image
```

This builds your Docker image tagged as `tpl-server:latest`.

---

## 📦 2. Publish the image

Tag and push image to <my-repo> (public or private) accessible to the Kubernetes cluster

```bash
 docker tag localhost/tpl-server:latest <my-repo>/tpl-server:latest
 docker push <my-repo>/tpl-server:latest
```

---

## ⎈ 3. Deploy to Kubernetes with Helm


### Update `chart/values.yaml` file

```yaml
 image:
   repos: <my-repo>
   tag: latest
```

### Install the Helm chart in your Kubernetes cluster

```bash
helm install my-template-server ./chart
```


Verify the deployment:

```bash
kubectl get pods
kubectl get svc
```

---

## 📅 4. Run sample Control-M Kubernetes Job


### Create the Connection Profile

In Control-M Configuration → Centralized Connection Profiles: create a Kubernetes Connection Profile and set following values
 - Name: K8STPLSVC
 - Namespace: the namespace where you will run the sample job
 - Spec Endpoint URL: http://my-template-server-svc/jobspec 

💡 *my-template-server-svc is the Service exposing the template server deployed in step 3*


### Edit `RemoteSpec_demoJob.json`

File `RemoteSpec_demoJob.json` is a sample Control-M job definition. Edit it to set values corresponding to your environment:
 - ControlmServer: your Control-M server name
 - Host: the Hostgroup to which your Kubernetes Agent belongs to (e.g.: k8s_group)
 

### Run the Job

```bash
ctm run RemoteSpec_demoJob.json
```

In Control-M Monitoring, locate the job and inspect it.

---

## 🛠️ 5. Troubleshooting

Check pod logs:

```bash
kubectl logs <pod-name>
```

Recheck your Helm chart values and Kubernetes resources if something fails to deploy.

---

## ✅ Summary

You've successfully:

- Built a Docker image  
- Deployed it to Kubernetes with Helm  
- Run a Control-M job that executes the Kubernetes Job provided by the server

---

## 📁 Project Structure

# ```
# my-project/
# ├── image/
# │   ├── Dockerfile
# │   ├── demo.yaml
# │   └── tplserver.py
# ├── chart/
# │   ├── Chart.yaml
# │   ├── values.yaml
# │   └── templates/
# │       ├── deployment.yaml
# │       └── service.yaml
# ├── RemoteSpec_demoJob.json
# └── README.md
# ```

---

## 📚 Resources

- [Docker Documentation](https://docs.docker.com/)  
- [Helm Charts Guide](https://helm.sh/docs/topics/charts/)  
- [Control-M for Kubernetes Documentation](https://docs.bmc.com/docs/display/CTMK8S)
