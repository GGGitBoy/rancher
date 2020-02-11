import pytest

from .common import *  # NOQA

dingtalk_config = {
    "type"  : "/v3/schemas/dingtalkConfig",
    "url"   : "https://oapi.dingtalk.com/robot/send",
    "secret": "testSecret"
}

microsoft_config = {
    "type" : "/v3/schemas/microsoftConfig",
    "url"  : "https://outlook.office.com/webhook",
   
}

CLUSTER_ALERTING_APP = "cluster-alerting"
ALERTMANAGER_CLUSTER_ALERTING_WORKLOAD  = "alertmanager-cluster-alerting"  	
WEBHOOK_RECEIVER_WORKLOAD = "webhook-receiver"

def test_add_notifier(remove_resource):
    client, cluster = get_global_admin_client_and_cluster()
    nodes = client.list_node(clusterId=cluster.id)
    assert len(nodes.data) > 0
    node_id = nodes.data[0].id

    # Add the notifier dingtalk and microsoft 
    notifier_dingtalk = client.create_notifier(name="dingtalk",
                                                clusterId=cluster.id,
                                                dingtalkConfig=dingtalk_config
                                              )

    notifier_microsoft = client.create_notifier(name="microsoft",
                                                 clusterId=cluster.id,
                                                 microsoftConfig=microsoft_config
                                                )  

    # Add the alertGroup
    all_recipients = []

    recipient1 = {
        "notifierId"   :  notifier_dingtalk.id,
        "notifierType" :  "dingtalk",
        "type"         :  "/v3/schemas/recipient"
    }

    recipient2 = {
        "notifierId"   :  notifier_microsoft.id,
        "notifierType" :  "microsoft",
        "type"         :  "/v3/schemas/recipient"
    }

    all_recipients.append(recipient1)
    all_recipients.append(recipient2)
    
    cluster_alertGroup = client.create_cluster_alert_group(name="testGroup",
                                                           clusterId=cluster.id,
                                                           recipients=all_recipients
                                                           ) 

    # Add the alertRule  
    node_rule = {
        "condition"    :  "mem",
        "cpuThreshold" :  70,
        "memThreshold" :  1,
        "nodeId"       :  node_id,
        "type"         :  "/v3/schemas/nodeRule"
    }
                     
    cluster_alertRule = client.create_cluster_alert_rule(name="testRule",
                                                         clusterId=cluster.id,
                                                         groupId=cluster_alertGroup.id,
                                                         nodeRule=node_rule
                                                        ) 

    # Make sure the webhook-receive is work 
    system_project = client.list_project(name="System",
                                         clusterId=cluster.id).data[0]

    project_client = get_project_client_for_token(system_project, ADMIN_TOKEN)
    wait_for_app_to_active(project_client, CLUSTER_ALERTING_APP)
    alerting_app = project_client.list_app(name=CLUSTER_ALERTING_APP).data[0]

    assert alerting_app.answers["webhook-receiver.enabled"] == "true"

    # Make sure the workload is active
    webhook_receiver = project_client.list_workload(name=WEBHOOK_RECEIVER_WORKLOAD).data[0]
    assert webhook_receiver.state == "active"

    alertmanager_cluster_alerting = project_client.list_workload(name=ALERTMANAGER_CLUSTER_ALERTING_WORKLOAD).data[0]
    assert alertmanager_cluster_alerting.state == "active"

    # Remove the alertGroup
    remove_resource(cluster_alertGroup)
    
    # Remove the notifiers
    remove_resource(notifier_dingtalk)
    remove_resource(notifier_microsoft)