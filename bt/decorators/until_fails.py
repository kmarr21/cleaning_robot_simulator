from bt_library.blackboard import Blackboard
from bt_library.common import ResultEnum
from bt_library.decorator import Decorator
from bt_library.tree_node import TreeNode


class UntilFails(Decorator):
    """
    Specific implementation of the until-fails decorator.
    Executes attached node while it succeeds returning RUNNING.
    Returns SUCCEEDED at the first failure.
    """

    def __init__(self, child: TreeNode):
        """
        Default constructor.

        :param child: Child associated to the decorator
        """
        super().__init__(child)

    def run(self, blackboard: Blackboard) -> ResultEnum:
        """
        Execute the behavior of the node.

        :param blackboard: Blackboard with the current state of the problem
        :return: The result of the execution
        """
        result_child = self.child.run(blackboard)

        # If child fails, decorator succeeds and returns; otherwise, returns "RUNNING" until failure
        if result_child == ResultEnum.FAILED:
            return self.report_succeeded(blackboard)
        elif result_child == ResultEnum.SUCCEEDED:
            return self.report_running(blackboard)
        else:
            return self.report_running(blackboard)