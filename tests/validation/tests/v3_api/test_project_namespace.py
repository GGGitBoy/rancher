from .common import *  # NOQA

def test_namespace_quota_edit(remove_resource):
    client, cluster = get_global_admin_client_and_cluster()

    pj1 = client.create_project(name=random_str(),
                                clusterId=cluster.id,
                                resourceQuota={"limit": {"limitsCpu": "20m"}},
                                namespaceDefaultResourceQuota={
                                    "limit": {"limitsCpu": "10m"}})

    pj2 = client.create_project(name=random_str(),
                                clusterId=cluster.id,
                                resourceQuota={"limit": {"limitsCpu": "15m"}},
                                namespaceDefaultResourceQuota={
                                    "limit": {"limitsCpu": "15m"}})

    
    p_client = get_cluster_client_for_token(cluster, ADMIN_TOKEN)

    ns1 = p_client.create_namespace(name=random_str(),
                                 clusterId=cluster.id,
                                 projectId=pj1.id)
    
    ns2 = p_client.create_namespace(name=random_str(),
                                  clusterId=cluster.id,
                                  projectId=pj2.id)

    ns1 = p_client.wait_success(ns1)
    ns2 = p_client.wait_success(ns2)

    p_client.action(obj=ns2,
                  action_name="move",
                  projectId=None)

    ns1 = p_client.update(ns1,
                resourceQuota={"limit": {"limitsCpu": "11m"}})

    ns1_limitsCpu = ns1.resourceQuota.limit.limitsCpu
    assert ns1_limitsCpu == "11m"

    remove_resource(pj1)
    remove_resource(pj2)
    remove_resource(ns2)
