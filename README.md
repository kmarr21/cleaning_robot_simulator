# Behavior Tree Assignment
[Completed for Master's coursework]

## Introduction

This project implements a behavior tree for a vacuum cleaning robot simulator. It operates as a simple reflex agent. 

## How to Run

1. Ensure you have Python 3 installed on your system.
2. Download this directory.
3. Navigate to the project directory in your terminal.
4. Run the following command:
   ```
   python main.py
   ```

## Dependencies

- Python 3
- No external libraries required beyond the python standard library
  - Uses `time` module for simulation pacing
  - Uses `random` module for simulating environmental factors

## File Structure

- `main.py`: The main simulation script
- `bt_library/`: Contains the core behavior tree implementation
- `bt/`: Contains specific implementations for the vacuum robot
  - `tasks/`: Individual task implementations
  - `conditions/`: Condition node implementations
  - `decorators/`: Decorator node implementations
  - `composites/`: Composite node implementations (sequence, selection, priority)
  - `globals.py`: Global variables and constants
  - `robot_behavior.py`: Defines the overall behavior tree structure

## Assumptions and Design Decisions

### Battery Management
- Battery decreases by 1% each cycle (second) when not charging
- Battery increases by 5% each cycle when charging (assumed that like most electronics, the robot charges faster than it loses charge)
- (This allows for approximately 100 seconds of operation and 20 seconds of charging)

### Default Environment Values
- Battery Less Than 30: Defaults to 0 if not set
- Spot Cleaning: Defaults to False
- General Cleaning: Defaults to False
- Dusty Spot: Defaults to False
- Users can modify these defaults at the start of the simulation (prompted via main)

### Simulation Cycle
- Each cycle represents 1 second of real-time
- The simulation runs in blocks of 10 cycles
- Users are prompted to continue after each block of 10 cycles (can select y/n)

### Cleaning Modes (if in automatic mode)
- General Cleaning is toggled to True every 50 cycles if currently False
- Spot Cleaning is toggled to True every 100 cycles if currently False

### Clean Floor Task
- Has a low probability (< 10%) of randomly failing to simulate completing the cleaning task

### Dusty Spot Detection
- 20% chance of detecting a dusty spot in each cycle (this is true for both interactive and automatic modes)

## User Interaction

- Users can choose between Automatic and Interactive modes
- In Interactive mode, users can issue cleaning commands every 10 cycles (see "Cleaning Modes" above for what happens in automatic mode)
- Users can always modify initial conditions at the start of the simulation (regardless of mode)

## Behavior Tree Structure

The behavior tree is structured with the following main components:
1. Battery check and charging sequence
2. Cleaning operations (Spot and General cleaning)
3. Do Nothing fallback

For detailed structure, refer to the `robot_behavior.py` file.

## Notes

- In Interactive mode, unavailable cleaning options (due to ongoing tasks) are not displayed