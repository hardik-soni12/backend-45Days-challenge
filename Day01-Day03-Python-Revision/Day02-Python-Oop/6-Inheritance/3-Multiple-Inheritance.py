'''
# Multiple Inheritance: 

Multiple inheritance is when a single class inherits from more than one parent class. 
This allows the child class to combine attributes and behaviors 
from all its parent classes, essentially creating a new, specialized class that is a mix of its ancestors.
'''

'''
# Multiple Inheritance Example: SmartWatch
Let's use a Smartwatch as an example. A smartwatch can be considered a combination of a Watch and a FitnessTracker. 
By using multiple inheritance, we can create a Smartwatch that gets features from both.
'''
# Parent Class 1: Watch
class Watch:
    def __init__(self, brand):
        self.brand = brand

    def set_time(self, time):
        print(f"Setting the time to {time}.")
        self.time_set = True

# Parent Class 2: FitnessTracker
class FitnessTracker:
    def __init__(self, tracker_id):
        self.tracker_id = tracker_id
        self.steps_counted = 0

    def count_steps(self, steps):
        self.steps_counted += steps
        print(f"Recorded {self.steps_counted} steps.")

# Child Class: Smartwatch
# It inherits from both Watch and FitnessTracker
class SmartWatch(Watch, FitnessTracker):
    def __init__(self, brand, tracker_id):
        Watch.__init__(self, brand)
        FitnessTracker.__init__(self, tracker_id)
        self.notification_enabled = False

    def enable_notifications(self):
        self.notifications_enabled = True
        print("Notifications enabled on the smartwatch.")


my_smartwatch = SmartWatch("FitGo", "FGT-001")

print(f"Brand: {my_smartwatch.brand}, ID: {my_smartwatch.tracker_id}")

# Use methods inherited from the Watch class
my_smartwatch.set_time("8:00 AM")

# Use methods inherited from the FitnessTracker class
my_smartwatch.count_steps(1000)

# Use the unique method of the Smartwatch class
my_smartwatch.enable_notifications()