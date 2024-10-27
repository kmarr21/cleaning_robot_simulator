#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# version 3.0.0 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

import bt_library as btl
import random
import time

from bt.robot_behavior import robot_behavior
from bt.globals import BATTERY_LEVEL, GENERAL_CLEANING, SPOT_CLEANING, DUSTY_SPOT_SENSOR, HOME_PATH, CHARGING

# Battery constraints
CHARGE_RATE = 5
DISCHARGE_RATE = 1

# Print ASCII art of robot — for fun! :) 
def print_robot():
    print("""
     [¯]
    (|>|)
    /===\\
   //| |\\\\
  // o=o \\\\
 //  |_|  \\\\
<_________>
    """)

# Print introduction into terminal, to make sure user is aware of how program works
def print_intro():
    print("\n" + "="*80)
    print_robot()
    print("Welcome to the Vacuum Cleaning Robot Simulator!")
    print("="*80)
    print("\nThis program simulates a vacuum cleaning robot with the following features:")
    print("- Battery management (charge rate: 5%/cycle, discharge rate: 1%/cycle)")
    print("- General cleaning mode")
    print("- Spot cleaning mode")
    print("- Dusty spot detection")
    print("- Automatic charging when battery is low")
    print("\nAssumptions:")
    print("- Each cycle represents 1 second of real-time")
    print("- The simulation runs in blocks of 10 cycles")
    print("- Dusty spots are randomly detected with a 20% chance each cycle")
    print("\nStarting conditions:")
    print("- Battery Level: 29%")
    print("- Spot Cleaning: False")
    print("- General Cleaning: True")
    print("- Dusty Spot Sensor: False")
    print("- Charging: False")
    print("\nYou will have the option to modify these starting conditions.")
    print("\nYou can choose between two modes:")
    print("1. Automatic: The robot operates autonomously with periodic cleaning commands")
    print("2. Interactive: You can input cleaning commands every 10 cycles")
    print("\n" + "="*80)

# Allow user to choose either "automatic" mode, where user input is simulated, or "interactive" mode, where they can provide robot input
def get_user_mode():
    while True:
        mode = input("\nChoose a mode (1 for Automatic, 2 for Interactive): ")
        if mode in ['1', '2']:
            return int(mode)
        print("Invalid input. Please enter 1 or 2.")

# Prompt user to see if they want to change the initial starting conditions; otherwise, assume default
def set_initial_conditions():
    conditions = {
        BATTERY_LEVEL: 29,
        SPOT_CLEANING: False,
        GENERAL_CLEANING: True,
        DUSTY_SPOT_SENSOR: False,
        CHARGING: False
    }
    
    while True:
        print("\nCurrent conditions:")
        for key, value in conditions.items():
            print(f"- {key}: {value}")
        
        change = input("\nWould you like to change any condition? (y/n): ").lower()
        if change != 'y':
            break
        
        condition = input("Which condition would you like to change? ").upper()
        if condition not in conditions:
            print("Invalid condition. Please try again.")
            continue
        
        if condition == BATTERY_LEVEL:
            new_value = int(input("Enter new battery level (0-100): "))
            if 0 <= new_value <= 100:
                conditions[BATTERY_LEVEL] = new_value
            else:
                print("Invalid battery level. It must be between 0 and 100.")
        else:
            new_value = input("Enter new value (True/False): ").lower() == 'true'
            conditions[condition] = new_value
    
    return conditions

# Run BT simulation
def run_simulation(mode, initial_conditions):
    current_blackboard = btl.Blackboard()

    # Set up initial conditions
    for key, value in initial_conditions.items():
        current_blackboard.set_in_environment(key, value)

    cycle_count = 0
    done = False

    while not done:
        for _ in range(10):  # Run 10 cycles at a time
            cycle_count += 1
            print(f"\n--- Cycle {cycle_count} ---")

            # Step 1: Change the environment (same for both modes)
            #  Change the battery level (charging or depleting)
            current_battery = current_blackboard.get_in_environment(BATTERY_LEVEL, 0) # get current battery level
            is_charging = current_blackboard.get_in_environment(CHARGING, False) # check if charging
            
            if is_charging:
                # If is charging, add charge (until the total charge reaches 100)
                current_battery = min(100, current_battery + CHARGE_RATE)
            else:
                # If not charging (i.e., on charging port), decrease in battery
                current_battery = max(0, current_battery - DISCHARGE_RATE)
            
            current_blackboard.set_in_environment(BATTERY_LEVEL, current_battery) # set new battery level

            #  Simulate the response of the dusty spot sensor
            current_blackboard.set_in_environment(DUSTY_SPOT_SENSOR, random.random() < 0.2)  # 20% chance of dusty spot

            #  Simulate user input commands
            # Option 1: Automatic mode (simulation of user commands without actual interaction)
            if mode == 1:
                # Every 50 cycles, turn on general cleaning if not already on
                if cycle_count % 50 == 0 and not current_blackboard.get_in_environment(GENERAL_CLEANING, False):
                    print("Auto Command: Start General Cleaning")
                    current_blackboard.set_in_environment(GENERAL_CLEANING, True)
                # Every 100 cycles, turn on spot cleaning if not already on
                if cycle_count % 100 == 0 and not current_blackboard.get_in_environment(SPOT_CLEANING, False):
                    print("Auto Command: Start Spot Cleaning")
                    current_blackboard.set_in_environment(SPOT_CLEANING, True)

            # Print current state
            print(f"Battery: {current_battery}%, Charging: {is_charging}")
            print(f"Spot Cleaning: {current_blackboard.get_in_environment(SPOT_CLEANING, False)}")
            print(f"General Cleaning: {current_blackboard.get_in_environment(GENERAL_CLEANING, False)}")
            print(f"Dusty Spot: {current_blackboard.get_in_environment(DUSTY_SPOT_SENSOR, False)}")

            # Evaluate behavior tree
            print('BEFORE -------------------------------------------------------------------------')
            btl.print_states(current_blackboard)
            print('================================================================================')

            result = robot_behavior.evaluate(current_blackboard)

            print('AFTER --------------------------------------------------------------------------')
            btl.print_states(current_blackboard)
            print('================================================================================')
            
        # Option 2: Interactive mode (outside of loop, since can only be done every 10 cycles)
        if mode == 2:
            print("\nCleaning commands:")
            print("Note: Options for General or Spot Cleaning will not appear if already requested and pending.")
            general_cleaning = current_blackboard.get_in_environment(GENERAL_CLEANING, False)
            spot_cleaning = current_blackboard.get_in_environment(SPOT_CLEANING, False)
                
            # See which commands you can add
            # (e.g., if a user already requested GENERAL_CLEANING, they must wait until it is false to request again)
            available_commands = []
            if not general_cleaning:
                print("1: Start General Cleaning")
                available_commands.append('1')
            if not spot_cleaning:
                print("2: Start Spot Cleaning")
                available_commands.append('2')
            print("3: No new command")
            available_commands.append('3')
                
            while True:
                command = input(f"Enter your command ({'/'.join(available_commands)}): ")
                if command == '1' and not general_cleaning:
                    current_blackboard.set_in_environment(GENERAL_CLEANING, True)
                    print("General Cleaning initiated.")
                    break
                elif command == '2' and not spot_cleaning:
                    current_blackboard.set_in_environment(SPOT_CLEANING, True)
                    print("Spot Cleaning initiated.")
                    break
                elif command == '3':
                    print("No new command issued.")
                    break
                else:
                    print("Invalid command or cleaning already in progress. Please try again.")

        # User input after every 10 cycles
        user_input = input("Continue simulation for 10 more cycles? (y/n): ")
        if user_input.lower() != 'y':
            done = True

    print("Simulation completed.")

# Main execution
print_intro()
initial_conditions = set_initial_conditions()
mode = get_user_mode()
run_simulation(mode, initial_conditions)