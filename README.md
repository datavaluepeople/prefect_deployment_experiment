# Prefect deployment experiments
Attempt to make Prefect Deployments that function outside of the repo that holds the Flows for the deployments.

Based on the [issue](https://github.com/anna-geller/prefect-docker-deployment/issues/1)

## Requirements and installation
- docker engine
- prefect installation

### Example installation
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## How to run docker hello world example
For all new terminals run `source .venv/bin/activate`
- In a new terminal start the orion server `prefect orion start`
- In a new terminal start the agent: `prefect agent start -q "docker_experiments"`
- In a new terminal apply the deployment: `python docker_hello_world.py`
- Then run the deployment: `prefect deployment run "docker_experiment/hello"`

You will then see the logs of the hello world docker in the terminal with the agent running.
