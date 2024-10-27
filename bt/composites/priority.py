import bt_library as btl

class Priority(btl.Composite):
    """
    Specific implementation of the priority composite.
    Children are evaluated in order of priority; succeeds if ANY of the children succeed.
    """

    def __init__(self, children: btl.NodeListType):
        """
        Default constructor.

        :param children: List of children for this node
        """
        super().__init__(children)

    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        """
        Execute the behavior of the node.

        :param blackboard: Blackboard with the current state of the problem
        :return: The result of the execution
        """
        # Iterate through all children in order of priority (highest to lowest)
        for child_position, child in enumerate(self.children):
            # Execute the current child
            result = child.run(blackboard)

            # If child succeeds, priority node succeeds; return 0 to reset to the highest priority on the next tick
            if result == btl.ResultEnum.SUCCEEDED:
                return self.report_succeeded(blackboard, 0)

            # If child is running, priority node considered running; return the current child position (just to store)
            elif result == btl.ResultEnum.RUNNING:
                return self.report_running(blackboard, child_position)

            # If child fails, loop continues to the next child

        # If all children fail, the priority node fails; return 0 to reset to highest priority on the next tick
        return self.report_failed(blackboard, 0)