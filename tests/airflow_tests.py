import unittest
from airflow.models import DagBag
from airflow.utils.dates import days_ago

class TestDagIntegrity(unittest.TestCase):

    def setUp(self):
        self.dagbag = DagBag()

    def test_import_dags(self):
        self.assertFalse(
            len(self.dagbag.import_errors),
            'DAG import failures. Errors: {}'.format(
                self.dagbag.import_errors
            )
        )

class TestModellingDag(unittest.TestCase):

    def setUp(self):
        self.dagbag = DagBag()

    def test_task_count(self):
        dag_id = "modelling_dag"
        dag = self.dagbag.get_dag(dag_id)
        self.assertEqual(len(dag.tasks), 6)

    def test_contain_tasks(self):
        """Check task contains in hello_world dag"""
        dag_id = 'modelling dag'
        dag = self.dagbag.get_dag(dag_id)
        tasks = dag.tasks
        task_ids = list(map(lambda task: task.task_id, tasks))
        self.assertListEqual(task_ids, ['pull_top_subreddits', 'scrape_reddit', 'process_reddit', 'build_features', 'model', 'upload_to_s3'])

    def test_runs_daily(self):
        """Check dag runs daily"""
        dag_id = "modelling_dag"
        dag = self.dagbag.get_dag(dag_id)
        default_args = dag.default_args
        self.assertEqual(default_args["start_date"],days_ago(2))