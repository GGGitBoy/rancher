import pytest

from .common import *  # NOQA

def test_add_node_label():
    client, cluster = get_admin_client_and_cluster()
    testLabel = "foo"
    nodes = client.list_node(clusterId=cluster.id)
    assert len(nodes.data) > 0
    nodeId = nodes.data[0].id
    node = client.by_id_node(nodeId)

    # Make sure there is no test label and add test label
    node_labels = node.labels.data_dict()
    assert testLabel not in node_labels

    print("Add test label")
    node_labels[testLabel] = "bar"
    client.update(node, labels=node_labels)

    # Label should be added
    time.sleep(2)
    node = client.by_id_node(nodeId)
    node_labels = node.labels.data_dict()

    assert node_labels[testLabel] == "bar"
    print("Test label has been added")

     # Label should be delete
    del node_labels[testLabel]
    client.update(node, labels=node_labels)
    time.sleep(2)
    node = client.by_id_node(nodeId)
    node_labels = node.labels.data_dict()
    assert testLabel not in node_labels
    print("Test label has been delete")