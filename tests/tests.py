import os
import unittest
from workflows.basic import get_workflow_name, get_jobs_count

class Test(unittest.TestCase):

    def test_get_workflow_name(self):
        with open(os.path.join('tests', 'github-actions-demo.yml'), 'r') as f:
            workflow_file = f.read()
        result = get_workflow_name(workflow_file)
        self.assertEqual(result, 'GitHub Actions Demo')

        with open(os.path.join('tests', 'multiple-jobs.yml'), 'r') as f:
            workflow_file = f.read()
        result = get_workflow_name(workflow_file)
        self.assertEqual(result, 'This Workflow Has Multiple Jobs')

    def test_get_jobs_count(self):
        with open(os.path.join('tests', 'github-actions-demo.yml'), 'r') as f:
            workflow_file = f.read()
        result = get_jobs_count(workflow_file)
        self.assertEqual(result, 1)

        with open(os.path.join('tests', 'multiple-jobs.yml'), 'r') as f:
            workflow_file = f.read()
        result = get_jobs_count(workflow_file)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
