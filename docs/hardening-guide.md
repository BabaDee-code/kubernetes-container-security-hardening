# Kubernetes Hardening Guide

## Security objective

Create a workload baseline that reduces Kubernetes attack surface before production deployment.

## Implemented controls

| Area | Control |
|---|---|
| Namespace security | Restricted Pod Security Admission labels |
| Workload identity | Dedicated service account |
| Token exposure | Service account token automount disabled |
| RBAC | Read-only access to ConfigMaps only |
| Runtime security | Non-root user, no privilege escalation, dropped capabilities |
| Filesystem | Read-only root filesystem |
| Seccomp | RuntimeDefault profile |
| Network | NetworkPolicy restricts ingress and egress |
| Reliability | Resource requests, limits, and readiness probe |

## DNS egress boundary

The workload needs DNS resolution, but allowing port 53 to every namespace is broader than a DNS-only policy: any pod in the cluster could listen on that port and become an allowed destination. The egress rule therefore constrains DNS traffic by both namespace identity (`kube-system`) and DNS pod identity (`k8s-app: kube-dns`) and permits UDP and TCP 53. TCP is retained because DNS can legitimately fall back to TCP for large or truncated responses.

The `k8s-app: kube-dns` label is common for CoreDNS deployments but is not universal. Before applying this baseline to another Kubernetes distribution, verify the labels used by its cluster DNS pods and adapt the selector without broadening the namespace boundary.

The manifest tests encode this destination constraint so a future change cannot silently regress to cluster-wide port-53 egress.

## Employer-facing explanation

This repository shows how I approach Kubernetes hardening as an engineering system: define a secure baseline, codify it in manifests, and use automated tests to prevent insecure drift. The tests make the project verifiable instead of purely descriptive.
