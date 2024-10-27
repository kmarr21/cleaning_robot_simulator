import bt_library as btl

class Sequence(btl.Composite):
    """
    Specific implementation of the sequence composite.
    Children are evaluated left to right; fails as soon as one of the children fails.
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
        # Get position of previously running child, or start at 0 if none was running
        running_child = self.additional_information(blackboard, 0)

        # Iterate through the children starting from the previously running child (or first if none running)
        for child_position in range(running_child, len(self.children)):
            child = self.children[child_position]
            result = child.run(blackboard) # Execute current child
            
            # If the child fails, entire sequence fails: return failure
            if result == btl.ResultEnum.FAILED:
                return self.report_failed(blackboard, 0)
            
            # If child is running, sequence is considered running; return this child position to resume this point from the next tick
            elif result == btl.ResultEnum.RUNNING:
                return self.report_running(blackboard, child_position)
            
            # If child succeeeds, we continue in the loop to the next child
        
        # If all children succeed, the sequence succeeds; we return to 0 to reset the first child on next tick
        return self.report_succeeded(blackboard, 0)