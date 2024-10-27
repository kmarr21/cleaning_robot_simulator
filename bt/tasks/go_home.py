import bt_library as btl
from ..globals import HOME_PATH

class GoHome(btl.Task):
    """
    Implementation of the Go Home task: robot goes to "home" station
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message('Going home')
        # Finds home path (currently just a print statement)
        home_path = blackboard.get_in_environment(HOME_PATH, None)
        # If home path exists, prints the home path and succeeds
        if home_path:
            self.print_message(f'Following path: {home_path}')
            return self.report_succeeded(blackboard)
        else:
            # Otherwise fails: could not find home path 
            #   (given that in this simple implementation the home path is a print statement, this should always succeed barring external error)
            self.print_message('No path home found')
            return self.report_failed(blackboard)