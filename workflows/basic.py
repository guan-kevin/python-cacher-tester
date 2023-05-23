import yaml


def get_workflow_name(workflow_file):
    return yaml.safe_load(workflow_file)['name']

def get_jobs_count(workflow_file):
    return len(yaml.safe_load(workflow_file)['jobs'])
