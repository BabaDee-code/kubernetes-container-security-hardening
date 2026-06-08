from pathlib import Path

import yaml


def load_yaml_documents(path: str):
    return [doc for doc in yaml.safe_load_all(Path(path).read_text()) if doc]


def test_deployment_runs_as_non_root_and_drops_capabilities():
    deployment = load_yaml_documents("k8s/deployment.yaml")[0]
    container = deployment["spec"]["template"]["spec"]["containers"][0]
    security_context = container["securityContext"]

    assert security_context["runAsNonRoot"] is True
    assert security_context["allowPrivilegeEscalation"] is False
    assert security_context["readOnlyRootFilesystem"] is True
    assert security_context["capabilities"]["drop"] == ["ALL"]


def test_service_account_token_is_not_automounted():
    deployment = load_yaml_documents("k8s/deployment.yaml")[0]
    assert deployment["spec"]["template"]["spec"]["automountServiceAccountToken"] is False

    service_account = load_yaml_documents("k8s/service-account.yaml")[0]
    assert service_account["automountServiceAccountToken"] is False


def test_namespace_enforces_restricted_pod_security():
    namespace = load_yaml_documents("k8s/namespace.yaml")[0]
    labels = namespace["metadata"]["labels"]
    assert labels["pod-security.kubernetes.io/enforce"] == "restricted"


def test_network_policy_defines_ingress_and_egress():
    policy = load_yaml_documents("k8s/network-policy.yaml")[0]
    assert set(policy["spec"]["policyTypes"]) == {"Ingress", "Egress"}
