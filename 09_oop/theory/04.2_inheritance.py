# ==========================================
# Example 1: Without Inheritance
# ==========================================
#
# A basic OTT subscription.
# Every subscription has:
# - subscription id
# - plan
# - total payment
#
# The object can subscribe or unsubscribe.
print()

class OTTSubscription:

    # Parent Constructor
    def __init__(self, subscription_id, plan, total_payment):

        # Instance Variables
        self.id = subscription_id
        self.plan = plan
        self.total_payment = total_payment

    # Instance Method
    def subscribe(self):
        print(f"Subscriber with {self.id} id subscribed to {self.plan} plan")

    # Instance Method
    def un_subscribe(self):
        print(f"Subscriber with {self.id} id unsubscribed from {self.plan} plan")


# Create a normal OTT subscription.
netflix = OTTSubscription(4567, "Monthly", 100)

# Access instance variable.
print(netflix.plan)

# Call instance method.
netflix.subscribe()



print()

# ==========================================
# Example 2: Inheritance
# ==========================================
#
# PremiumSubscription inherits everything
# from OTTSubscription.
#
# It automatically gets:
# - id
# - plan
# - total_payment
# - subscribe()
# - un_subscribe()
#
# It also adds one new feature:
# - max_screens

class OTTSubscription:

    # Parent Constructor
    def __init__(self, subscription_id, plan, total_payment):

        self.id = subscription_id
        self.plan = plan
        self.total_payment = total_payment

    def subscribe(self):
        print(f"Subscriber with {self.id} id subscribed to {self.plan} plan")

    def un_subscribe(self):
        print(f"Subscriber with {self.id} id unsubscribed from {self.plan} plan")


# Child Class
class PremiumSubscription(OTTSubscription):

    # Child Constructor
    def __init__(self, subscription_id, plan, total_payment, screens):

        # Call the Parent Constructor.
        super().__init__(subscription_id, plan, total_payment)

        # Child-specific instance variable.
        self.max_screens = screens

    # Child-specific method.
    def set_max_screens(self, screens):

        self.max_screens = screens

        print(f"Maximum screens set to {self.max_screens} in Premium plan.")


# Create a Premium Subscription object.
netflix = PremiumSubscription(
    123456,
    "Monthly",
    200,
    1
)

# Inherited method.
netflix.subscribe()

# Child method.
netflix.set_max_screens(4)

my_ott = OTTSubscription('12121', 'quater', 500)
print(my_ott.plan)

'''
                     OTTSubscription
                    (Parent Class)
                  /                \
                 /                  \
                / inherits           \
               ▼                      ▼

PremiumSubscription             OTTSubscription Object
      Object                         (my_ott)
      (netflix)

id = 123456                     id = 12121
plan = Monthly                  plan = quarter
payment = 200                   payment = 500
max_screens = 4                 (No max_screens)
'''



'''
=========================================
Inheritance
=========================================

Inheritance allows one class
(child class) to reuse the properties
and methods of another class (parent class).

Parent Class
↓
General features

Child Class
↓
Inherits everything from the parent
and can add new features.

Syntax

class Child(Parent):
    pass

=========================================

Computer Thinking

PremiumSubscription Object
        │
        ▼
Call Parent Constructor
        │
        ▼
Initialize:
id
plan
total_payment
        │
        ▼
Initialize:
max_screens
        │
        ▼
Object Ready

=========================================

Relationship

OTTSubscription
        ▲
        │
        │ inherits
        │
PremiumSubscription

PremiumSubscription IS-A OTTSubscription

=========================================

Interview Questions

Q. What is Inheritance?

Ans:
Inheritance is an OOP concept in which
a child class acquires the properties
and methods of a parent class.

-----------------------------------------

Q. Why use Inheritance?

Ans:
To reuse existing code,
reduce duplication,
and make programs easier to maintain.

-----------------------------------------

Q. What does super() do?

Ans:
super() is used to call the parent class's
constructor or methods from the child class.

=========================================

One-line Revision

Inheritance
        ↓
Code Reusability
        ↓
Parent Class
        ↓
Child Class
        ↓
super()
        ↓
Reuse Parent Features

=========================================
'''