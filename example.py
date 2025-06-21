"""
    To use this implementation, you simply have to implement `agent_function` such that it returns a legal action.
    You can then let your agent compete on the server by calling
        python3 example_agent.py path/to/your/config.json

    You can interrupt the script at any time and continue at a later time.
    The server will remember the actions you have sent.

    Note:
        Once your agent "works", you can set `parallel_runs` to True.
        Then the server simulates multiple games in parallel and bundles requests.
        This reduces the overhead from waiting for the server.
        Furthermore, if you set `processes=5`, the client will use multiple processes
        for the calls to your agent_function.
"""


def agent_function(request_dict, _info):
    # TOOD: Implement this function in a better way
    print('I got the following request:')
    print(request_dict)
    return 'PORTAL 0,0'


if __name__ == '__main__':
    try:
        from client import run
    except ImportError:
        raise ImportError('You need to have the client.py file in the same directory as this file')

    import logging
    logging.basicConfig(level=logging.INFO)

    import sys
    config_file = sys.argv[1]

    run(
        # path to config file for the environment (in your personal repository)
        config_file,
        agent_function,
        # higher values will call the agent function on multiple requests in parallel (requires parallel_runs=True)
        processes=1,
        # stop after 1000 runs (then the rating is "complete")
        run_limit=1000,
        # set to True to let the server simulate multiple games in parallel
        parallel_runs=False,
        # set to True to "give up" all current games when you start the script.
        abandon_old_runs=False
    )
