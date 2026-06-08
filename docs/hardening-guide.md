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

## Employer-facing explanation

This repository shows how I approach Kubernetes hardening as an engineering system: define a secure baseline, codify it in manifests, and use automated tests to prevent insecure drift. The tests make the project verifiable instead of purely descriptive.
