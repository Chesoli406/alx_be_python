def main():
    print("\nDAILY TASK REMINDER")
    print("===================")
    
    # Get user input with validation
    task = input("\nEnter your task: ")
    
    while True:
        priority = input("Priority (high/medium/low): ").lower()
        if priority in ('high', 'medium', 'low'):
            break
        print("Invalid input. Please enter high, medium, or low.")
    
    while True:
        time_bound = input("Is it time-bound? (yes/no): ").lower()
        if time_bound in ('yes', 'no'):
            break
        print("Please answer with yes or no.")
    
    # Generate reminder using match-case
    match priority:
        case "high":
            message = f"'{task}' is a high priority task"
            if time_bound == "yes":
                message += " that requires immediate attention today!"
            else:
                message += " that should be your top focus."
        
        case "medium":
            message = f"'{task}' is a medium priority task"
            if time_bound == "yes":
                message += " that should be completed soon."
            else:
                message += " to address when possible."
        
        case "low":
            message = f"'{task}' is a low priority task"
            if time_bound == "yes":
                message += " with a time constraint - schedule it."
            else:
                message += ". Consider completing it when you have free time."
    
    # Print the final reminder
    print("\n" + ("REMINDER: " if priority == "high" else "Note: ") + message)
    print("\nTask reminder set successfully!")

if __name__ == "__main__":
    main()