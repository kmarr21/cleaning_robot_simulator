import bt_library as btl

class AlwaysFail(btl.Task):
    """
    Implementation of the Always Fail task: always fails
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message('Always failing')
        return self.report_failed(blackboard)