
Deploying a Containerized Remote Spec Service for a Control-M Kubernetes Agent
# Introduction
This tutorial demonstrates how to build an OCI image for a simple template server, deploy it using Helm, and use it for Control-M Kubernetes jobs of type Remote web service.
OCI (Open Container Initiative) is the standard for container image formats and runtimes to ensure interoperability and consistency across container tools. This tutorial uses Docker for building the image, but any OCI-compliant tool can be used instead.
In this tutorial, you run a Control-M Kubernetes-type job. When the job is executed, the Control-M/Agent requests a Job specification from the server by specifying a template and parameters. The server generates the template using those parameters and returns a complete and usable Kubernetes Job specification.
The following diagram illustrates the deployment flow:

In this diagram, you can see the following main deployment flow components:
Build Machine: Builds and pushes the Docker image
Container Registry: Stores the tpl-server image
Kubernetes Cluster: Runs a Helm Chart, which deploys a Template Server Pod and generates the /jobspec service
Control-M Agent: Runs the RemoteSpec job
# 🔧 Prerequisites
Before you begin, ensure you have the following tools installed and configured:
Docker: https://docs.docker.com/get-docker/
Kubernetes (with kubectl): https://kubernetes.io/docs/tasks/tools/
Helm: https://helm.sh/docs/intro/install/
Access to a Control-M environment, including an agent deployed in the Kubernetes cluster
# 🚀 Begin
Build the OCI image by running the following command:
docker build -t tpl-server:latest image
This packages your template server into a portable container image that can run anywhere.
Ensure that you now have the image by running the following command:
docker images | grep tpl-server
Publish the image by running the following commands:
docker tag tpl-server:latest <my-repo>/tpl-server:latest
docker push <my-repo>/tpl-server:latest
This enables Kubernetes to pull the image from a registry accessible to the cluster.
Ensure that the image is published by running the following command:
docker pull <my-repo>/tpl-server:latest
Download the sample files of the remote job specification from the following location:
https://github.com/controlm/ctm-kubernetes/tree/remote-tpl/01-Remote_Job_Specification_sample
Customize the chart/values.yaml file (in the sample files).
Under the image: element, provide the name of your repository on the following line:
repos: <my-repo>
In Kubernetes, create a pod by running the following Helm command:
helm install my-template-server ./chart
Check the status and details of the my-template-server pod by running the following commands:
kubectl get pods
kubectl describe pod <pod-name>
In Control-M, create a Kubernetes-type centralized connection profile with the following settings:
Name: K8STPLSVC
Namespace: your namespace
Spec Endpoint URL: http://my-template-server-svc/jobspec
Customize the RemoteSpec_demoJob.json file (in the sample files) with your environment details.
In particular, you must adjust the value of the ControlmServer property.
Run the Kubernetes-type job in Control-M with the following Automation API command:
ctm run RemoteSpec_demoJob.json
# What Happens when the Control-M Job Runs
During execution of the Control‑M RemoteSpec job, Control‑M sends a request to the Template Server (the provided Flask app that runs tplserver.py). The Template Server loads the requested template file (for example, demo.yaml) and injects into it the values provided in the job’s Spec Request Parameters field.
Using Flask’s render_template(), the server produces a fully rendered Kubernetes Job spec (YAML), with all placeholders replaced by the parameter values sent from Control‑M.
# 🛠️ Troubleshooting
Common issues and fixes:
ImagePullBackOff pod status: Verify that the image name and tag are correct, and that the image registry is reachable and properly authenticated
Helm install fails: Ensure that values.yaml is updated with the correct repo and tag.

To check pod logs in any case of an issue, run the following command:
kubectl logs <pod-name>
