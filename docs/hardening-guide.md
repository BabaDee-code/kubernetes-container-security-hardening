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
| Supply chain | Workload image pinned to an immutable SHA-256 digest |
| Reliability | Resource requests, limits, and readiness probe |

## Immutable image references

Mutable tags such as `latest` are convenient for development but are a weak production deployment boundary: the same manifest can resolve to different image bytes at different times. This makes rollback, provenance review, and incident reconstruction less reliable.

The example Deployment therefore uses the OCI digest form `repository@sha256:<digest>`. The checked-in digest is illustrative rather than a claim that the image exists in a registry. In a real delivery pipeline, the trusted build stage should publish the image, capture the registry-reported digest, complete required vulnerability/signature or provenance checks, and update the deployment artifact with that exact digest before promotion.

The manifest test enforces the invariant that the workload cannot silently drift back to `:latest` or another tag-only reference.

## Employer-facing explanation

This repository shows how I approach Kubernetes hardening as an engineering system: define a secure baseline, codify it in manifests, and use automated tests to prevent insecure drift. The tests make the project verifiable instead of purely descriptive.
