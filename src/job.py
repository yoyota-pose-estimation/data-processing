import yaml
from kubernetes import client, config


JOB_NAME = "pi"


def create_job_object():
    container = client.V1Container(
        name="pi",
        image="perl",
        command=["perl", "-Mbignum=bpi", "-wle", "print bpi(2000)"],
    )
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": "pi"}),
        spec=client.V1PodSpec(restart_policy="Never", containers=[container]),
    )
    # Create the specification of deployment
    spec = client.V1JobSpec(template=template, backoff_limit=4)
    job = client.V1Job(
        api_version="batch/v1",
        kind="Job",
        metadata=client.V1ObjectMeta(name=JOB_NAME),
        spec=spec,
    )

    return job


def create_job():
    with open("/template/job-template.yaml") as f:
        job_template = yaml.safe_load(f)
        print(job_template)
    config.load_incluster_config()
    batch_v1 = client.BatchV1Api()
    job = create_job_object()
    current_namespace = open(
        "/var/run/secrets/kubernetes.io/serviceaccount/namespace"
    ).read()
    api_response = batch_v1.create_namespaced_job(
        body=job, namespace=current_namespace
    )
    print("Job created. status='%s'" % str(api_response.status))
