# Vaccume cleaner world - simple reflex agent

#Initial environment
A = input("Enter status of the room A (CLEAN/DIRTY): ").upper()
B = input("Enter the status of the room B (CLEAN/DIRTY): ").upper()

# initial position of the vaccume cleaner
location = input("Enter the initial position of the vaccume cleaner (A/B): ").upper()

# Maximum 4 actions
for i in range (4):

    if location == "A":
        if A == "DIRTY":
            print("Cleaning Room A")
            A = "CLEAN"

        else:
            print("Moving to Room B")
            location = "B"

    elif location == "B":
        if B == "DIRTY":
            print("Cleaning Room B")
            B = "CLEAN"

        else:
            print("Moving to Room A")
            location = "A"

    if A == "CLEAN" and B == "CLEAN":
        break

# Final result
print("\nFinal status: ")
print("Room A: ", A)
print("Room B: ", B)

'''How is this a rational agent?
The goal is to clean both rooms.
- If the room is dirty, cleaning it is the correct action.
- If the room is clean, moving to the other room helps check its condition.
- It stops when both rooms are clean.
Therefore, it takes actions that help achieve its goal.

7. Viva questions and answers
These are the questions I want you to prepare first.

Q1. What is an AI agent?
An AI agent is a system that observes its environment and performs actions to achieve a goal.

Q2. What is a Simple Reflex Agent?
It is an agent that selects actions based only on the current percept.

Q3. What is Vacuum Cleaner World?
It is a simple AI environment consisting of rooms that can be clean or dirty and a vacuum cleaner that cleans them.

Q4. What is a percept?
A percept is the information received by an agent from its environment.

Q5. What is the goal of this program?
To clean all the dirty rooms.

Q6. Why do we use a while loop?
To repeat the cleaning process until both rooms become clean.

Q7. What is a rational agent?
An agent that chooses actions that help achieve its desired goal.

Q8. What are the possible actions of the vacuum cleaner?
- Clean
- Move Left
- Move Right

Q9. What is the environment in this experiment?
The two-room environment consisting of Room A and Room B.

Q10. What is the difference between a Simple Reflex Agent and a Model-Based Agent?
A Simple Reflex Agent uses only the current percept, whereas a Model-Based Agent also maintains information about the environment's internal state.

Q11. What is the stopping condition in this program?
The program stops when both Room A and Room B are CLEAN.

Q12. Which Python concepts are used in this program?
Variables, input(), if-else conditions, while loop and print().'''


    
