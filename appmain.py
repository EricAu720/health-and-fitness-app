

class HealthFitnessApp:
    def __init__(self):
        # Initialize data storage
        self.steps = 0
        self.calories_burned = 0
        self.meals = []  # List of tuples: (meal_name, calories)
        self.total_calories_consumed = 0
        self.gym_videos = []  # List of tuples: (title, duration, url)

    def track_activity(self, steps):
        """Simulate tracking steps and calculate calories burned."""
        self.steps += steps
        # Simple formula: 1 step burns 0.05 calories (approximation)
        calories = steps * 0.05
        self.calories_burned += calories
        print(f"Activity tracked: {steps} steps, {calories:.1f} calories burned.")

    def track_nutrition(self, meal_name, calories):
        """Simulate logging a meal and its calories."""
        self.meals.append((meal_name, calories))
        self.total_calories_consumed += calories
        print(f"Meal logged: {meal_name}, {calories} calories.")

    def add_gym_video(self, title, duration, url):
        """Simulate adding a tutorial gym video by storing its metadata."""
        self.gym_videos.append((title, duration, url))
        print(f"Gym video added: {title}, Duration: {duration} mins, URL: {url}")

    def show_gym_videos(self):
        """Display the list of tutorial gym videos."""
        if not self.gym_videos:
            print("No gym videos available.")
            return
        print("\n--- Tutorial Gym Videos ---")
        for title, duration, url in self.gym_videos:
            print(f"Title: {title}, Duration: {duration} mins, URL: {url}")

    def show_progress(self):
        """Display total steps, calories burned, and calories consumed."""
        print("\n--- Progress Summary ---")
        print(f"Total Steps: {self.steps}")
        print(f"Total Calories Burned: {self.calories_burned:.1f}")
        print(f"Total Calories Consumed: {self.total_calories_consumed}")
        print("Meals Logged:")
        for meal_name, calories in self.meals:
            print(f"  - {meal_name}: {calories} calories")
        # Net calorie balance
        net_calories = self.total_calories_consumed - self.calories_burned
        print(f"Net Calorie Balance: {net_calories:.1f} (Consumed - Burned)")

def main():
    app = HealthFitnessApp()
    print("Welcome to the Health and Fitness Tracking App Simulation!")

    while True:
        print("\nOptions:")
        print("1. Track Activity (Steps)")
        print("2. Track Nutrition (Meal)")
        print("3. Add Tutorial Gym Video")
        print("4. Show Gym Videos")
        print("5. Show Progress")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            try:
                steps = int(input("Enter number of steps: "))
                if steps < 0:
                    print("Steps cannot be negative!")
                    continue
                app.track_activity(steps)
            except ValueError:
                print("Please enter a valid number of steps.")

        elif choice == "2":
            meal_name = input("Enter meal name: ")
            try:
                calories = int(input("Enter calories for this meal: "))
                if calories < 0:
                    print("Calories cannot be negative!")
                    continue
                app.track_nutrition(meal_name, calories)
            except ValueError:
                print("Please enter a valid number of calories.")

        elif choice == "3":
            title = input("Enter video title: ")
            try:
                duration = int(input("Enter video duration (in minutes): "))
                if duration <= 0:
                    print("Duration must be positive!")
                    continue
            except ValueError:
                print("Please enter a valid duration.")
                continue
            url = input("Enter video URL (e.g., YouTube link): ")
            app.add_gym_video(title, duration, url)

        elif choice == "4":
            app.show_gym_videos()

        elif choice == "5":
            app.show_progress()

        elif choice == "6":
            print("Exiting the app. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-6.")

if __name__ == "__main__":
    main()