service = client.V1Service(
    metadata=client.V1ObjectMeta(
        name=name,
        labels={"name": name}
    ),
    spec={
        "ports": [{"port": port}],
        "selector": {"app": app},
        "type": svc_type,
        "externalTrafficPolicy": traffic_policy,
    }
)
if cluster_ip:
    service.spec["clusterIP"] = cluster_ip
if ipv6:
    service.spec["ipFamily"] = "IPv6"
api_response = self.cluster.create_namespaced_service(
    body=service,
    namespace=ns
)
