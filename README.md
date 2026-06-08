# Kubernetes & Container Security Hardening

![CI](https://github.com/BabaDee-code/kubernetes-container-security-hardening/actions/workflows/ci.yml/badge.svg)

A practical Kubernetes and container hardening lab that demonstrates secure image design, namespace isolation, least-privilege RBAC, network segmentation, pod security settings, and automated manifest validation.

## What this project shows

- Secure-by-default Kubernetes workload design
- Least-privilege service account and RBAC permissions
- NetworkPolicy-based traffic restriction
- Non-root containers, read-only root filesystems, dropped Linux capabilities, and seccomp profiles
- Automated tests that validate hardening controls before deployment

## Repository structure

```text
k8s/                        Hardened Kubernetes manifests
app/                        Minimal containerized demo application
tests/                      Manifest security validation tests
.github/workflows/ci.yml    Automated CI validation
docs/hardening-guide.md     Security design and control mapping
```

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements-dev.txt
pytest -q
```

Optional deployment to a local cluster:

```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/service-account.yaml
kubectl apply -f k8s/rbac.yaml
kubectl apply -f k8s/network-policy.yaml
kubectl apply -f k8s/deployment.yaml
```

## Security controls represented

- Namespace isolation
- Least-privilege RBAC
- Non-root container execution
- Read-only root filesystem
- Dropped Linux capabilities
- Seccomp runtime default profile
- Network ingress restriction
- CI-based manifest testing

## Portfolio talking points

This project demonstrates how I would secure Kubernetes workloads before production deployment by combining architecture, secure configuration, and automated validation. It shows cloud-native security engineering depth across container hardening, workload identity, RBAC, and Kubernetes governance.
