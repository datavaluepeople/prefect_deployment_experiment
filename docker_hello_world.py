"""Deployment that will run the hello world docker image.

https://hub.docker.com/_/hello-world/
https://github.com/docker-library/hello-world
"""
from prefect import flows
from prefect.deployments import Deployment
from prefect.infrastructure import docker


def mock_fn():
    pass


# Need to have flow to set the flow name of the deployment
# Needs to have a callable fn property
flow = flows.Flow(name="docker_experiment", fn=mock_fn)
infra = docker.DockerContainer(image="hello-world:latest", command=["/hello"])

deployment = Deployment.build_from_flow(
    flow=flow,
    name="hello", 
    version=1,
    infrastructure=infra,
    work_queue_name="docker_experiments",
)

deployment.apply()
