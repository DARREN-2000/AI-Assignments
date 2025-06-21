from client import Agent

class ExitAgent(Agent):
    def __init__(self, run_id, agent_config):
        super().__init__(run_id, agent_config)

        # A new instance is created for each run (i.e. each game).
        # So you can keep a run-specific state.
        # WARNING: If a run was not finished, it will be resumed.
        #          get_action will then be called for the next required action.


    def get_action(self, percept, request_info):
        # The percept contains all the relevant information (history of guesses and feedback)
        # You can ignore request_info.

        return 'PORTAL 0,0'


if __name__ == '__main__':
    import sys, logging
    from client import run

    # You can set the logging level to logging.WARNING or logging.ERROR for less output.
    logging.basicConfig(level=logging.INFO)

    ExitAgent.run(
        agent_config_file=sys.argv[1],
        parallel_runs=False,    # If set to True, the server creates multiple parallel runs and bundles the requests.
        multiprocessing=False,  # Use multiple processes to run multiple agents in parallel.
        run_limit=1000,         # Stop after 1000 runs. Set to 1 for debugging.
    )

    # TIP: If your agent works, consider setting parallel_runs=True and multiprocessing=True.

