from dagster import check
from dagit.pipeline_run_storage import PipelineRunStorage


class DagsterGraphQLContext(object):
    def __init__(self, repository_container, pipeline_runs, synchronous_mode=False):
        from dagit.app import RepositoryContainer
        self.repository_container = check.inst_param(
            repository_container,
            'repository_container',
            RepositoryContainer,
        )
        self.pipeline_runs = check.inst_param(
            pipeline_runs,
            'pipeline_runs',
            PipelineRunStorage,
        )

        self.synchronous_mode = check.bool_param(synchronous_mode, 'synchronous_mode')