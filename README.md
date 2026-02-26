# Control-M for Kubernetes Overview

The Control-M for Kubernetes plug-in enables you to do the following:

- **Run one or more pods to completion in a Kubernetes cluster**  
  This enables you to integrate Control-M capabilities, such as advanced scheduling criteria, status monitoring, and SLA management.  
  Kubernetes job specs for this purpose can be retrieved from a remote location during job execution using a REST request or can be uploaded during job definition as local YAML files. In addition, you can provide job specs as templates with placeholders for job spec parameters.

- **Run OS jobs on remote UNIX-based hosts outside the Kubernetes cluster in an agentless manner**  
  To run these OS jobs, the Agents in Kubernetes connect to multiple hosts outside the cluster using the SSH protocol.

- **Use Control-M Managed File Transfer (MFT) to:**
  - Pull files from central storage (such as S3) into a persistent volume in the Kubernetes cluster and process them by running application pods.
  - Transfer files generated in the persistent volume during application processing to central storage outside the cluster.

- **Use containerized Agents running in Kubernetes to consume remote services**  
  This enables you to run the Agents on an optimized and highly scalable platform while executing a variety of workloads in a secure and fully automated manner.

---

## Repository Structure

The **main branch** contains general information, overview material, and shared resources related to the Control-M for Kubernetes plug-in.

Each example is provided as a dedicated folder in the repository root.  
Every example focuses on a specific capability or integration pattern and includes step-by-step guidance and sample configurations.

---

## Available Examples

- [01-Remote_Job_Specification_sample](./01-Remote_Job_Specification_sample)  
  Demonstrates how to deploy a containerized Remote Specification service that dynamically generates Kubernetes Job specifications for Control-M jobs at runtime.

Additional examples may be added over time to showcase more advanced use cases and best practices.

---

## Support

Found a bug? Looking for a new feature? Check if we already have an open issue in the [GitHub Issues page](https://github.com/controlm/ctm-kubernetes/issues).  
If not, feel free to create a new one. Together with the community, we will review, prioritize, and address relevant feedback and enhancement requests.