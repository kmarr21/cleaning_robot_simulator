import bt_library as btl
from ..globals import CHARGING, BATTERY_LEVEL

class Charge(btl.Task):
    """
    Implementation of the Charge task.
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message('Charging')
        blackboard.set_in_environment(CHARGING, True)
        current_battery = blackboard.get_in_environment(BATTERY_LEVEL, 0)
        
        # As long as battery is < 100, keep charging — return RUNNING (robot will not get off charger until at 100%)
        if current_battery < 100:
            self.print_message(f'Battery at {current_battery}%, continuing to charge')
            return self.report_running(blackboard)
        else:
            # If done charging, report this and set charging flag to false; report success
            self.print_message('Battery fully charged')
            blackboard.set_in_environment(CHARGING, False)
            return self.report_succeeded(blackboard)