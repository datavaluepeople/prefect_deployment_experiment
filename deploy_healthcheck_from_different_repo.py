"""Deployment that will run the health check flow from prefect-docker-deployment.

See README.md for more information.
"""
from prefect import flows
from prefect.deployments import Deployment
from prefect.infrastructure import docker


def mock_fn():
    pass


# Need to have flow to set the flow name of the deployment
# Needs to have a callable fn property
flow = flows.Flow(name="healthcheck", fn=mock_fn)
infra = docker.DockerContainer(
    image="dataflowops",
    # This is needed since the image is persisted locally and should not be pulled
    image_pull_policy="NEVER",
    # Need to have the network to be the host because orion is run
    # on the host using `prefect orion start`
    network_mode="host",
    # This sets the correct url for the API
    # so that the flow can be requested from the orion server
    env={"PREFECT_API_URL":"http://127.0.0.1:4200/api"}
)

deployment = Deployment.build_from_flow(
    flow=flow,
    name="from_different_repo", 
    version=1,
    # This matches: https://github.com/anna-geller/prefect-docker-deployment/blob/b901514de7525248cc8818d3793054d0b6267e15/deploy.bash#L6
    entrypoint="flows/healthcheck.py:healthcheck",
    infrastructure=infra,
    work_queue_name="docker_experiments",
)

deployment.apply()
