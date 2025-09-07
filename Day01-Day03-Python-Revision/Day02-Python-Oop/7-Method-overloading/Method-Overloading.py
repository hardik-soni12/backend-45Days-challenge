'''
# Method Overloading: 

Method overriding is the ability of a child class to redefine a method from its parent class. 
The method in the child class has the exact same name, arguments, and return type as the one in the parent, 
but it performs a different action. 
The purpose of overriding is to change the behavior of an inherited method to fit the needs of the child class.
'''

'''
# Example: A Payment System 💳

We have a general Payment class with a process_payment() method. We can then create 
different child classes for specific payment methods, like CreditCardPayment and PayPalPayment, 
which override the process_payment() method to handle their unique processes.
'''

class Payment:
    def process_payment(self, amount):
        print(f"Processing a generic payment of ₹{amount}.")

# credit card payment
# This class overrides the process_payment method
class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing a credit card payment of ₹{amount}.")
        print("Charging the card via the secure gateway.")

# paypal payment
# This class also overrides the process_payment method
class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing a PayPal payment of ₹{amount}.")
        print("Redirecting user to PayPal for authentication.")


generic_payment = Payment()
credit_card_payment = CreditCardPayment()
paypal_payment = PayPalPayment()

print("--- Calling the generic parent method ---")
generic_payment.process_payment(10000)

print("\n--- Calling the overridden child method for Credit Card ---")
credit_card_payment.process_payment(15000)

print("\n--- Calling the overridden child method for PayPal ---")
paypal_payment.process_payment(7500)