import yaml
import random
import string
from kubernetes import client, config


JOB_NAME = "pi"


def random_string(length):
    return "".join(
        random.choices(string.ascii_lowercase + string.digits, k=length)
    )


def set_job_name(job_object):
    job_object["metadata"]["name"] = "{}-{}".format(
        job_object["metadata"]["name"][:58], random_string(5)
    )
    return job_object


def set_args(job_object, args):
    spec = job_object["spec"]["template"]["spec"]
    containers = spec["containers"]
    container = containers[0]
    container["args"] = args
    return job_object


def get_jog_template():
    with open("/template/job-template.yaml") as f:
        return yaml.safe_load(f)


def clone_job_object(args):
    job_object = get_jog_template()
    job_object = set_job_name(job_object)
    job_object = set_args(job_object, args)
    return job_object


def get_current_namespace():
    return open(
        "/var/run/secrets/kubernetes.io/serviceaccount/namespace"
    ).read()


def create_clone_job(args):
    config.load_incluster_config()
    batch_v1 = client.BatchV1Api()
    job_object = clone_job_object(args)
    batch_v1.create_namespaced_job(
        body=job_object, namespace=get_current_namespace()
    )
