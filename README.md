# Prefect deployment experiments
Attempt to make Prefect Deployments that function outside of the repo that holds the Flows for the deployments.

Based on the [issue](https://github.com/anna-geller/prefect-docker-deployment/issues/1)

## Requirements and installation
- docker engine
- prefect installation
- (optional) `venv`

### Installation
Clone this repo.

### Example environment provision
Using `venv`:
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## How to run docker hello world example
For all new terminals run `source .venv/bin/activate` if using `venv`
- In a new terminal start the orion server `prefect orion start`
- In a new terminal start the agent: `prefect agent start -q "docker_experiments"`
- In a new terminal apply the deployment: `python docker_hello_world.py`
- Then run the deployment: `prefect deployment run "docker_experiment/hello"`

You will then see the logs of the hello world docker in the terminal with the agent running.

## How to run flow healthcheck from the repo [prefect-docker-deployment](https://github.com/anna-geller/prefect-docker-deployment)
Firstly you need to have the `dataflowops` image  from the [prefect-docker-deployment repo](https://github.com/anna-geller/prefect-docker-deployment) persisted locally.

To build `dataflowops` on your machine:
- Download the repo: `git clone https://github.com/anna-geller/prefect-docker-deployment ../prefect-docker-deployment`
- Run the command:
```
cd ../prefect-docker-deployment/
docker build -t dataflowops .
IMAGE=$(docker images --no-trunc --quiet dataflowops)
echo $IMAGE
cd ../prefect_deployment_experiment/
```

It is then possible to run the healthcheck flow from the prefect-docker-deployment repo with the commands:
- For all new terminals run `source .venv/bin/activate` if using `venv`
- In a new terminal start the orion server `prefect orion start`
- In a new terminal start the agent: `prefect agent start -q "docker_experiments"`
- In a new terminal apply the deployment: `python deploy_healthcheck_from_different_repo.py`
- Then run the deployment: `prefect deployment run "healthcheck/from_different_repo"`

You can see the logs for the healthcheck on the terminal that has the agent running.
