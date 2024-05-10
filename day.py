import random

class FiniteStateMachine:
    def __init__(self):
        self.current_state = None
        self.random_events = [
            "meet old friend",
            "call from mom",
            "rain"
        ]

    def run(self):
        mental_health = 100
        hunger = 30

        hour = 0
        while hour <= 24:
            if 0 <= hour < 7 or 23 <= hour:
                if hour == 23:
                    print("I had hard day today. Time to sleep.\n")
                else:
                    print("zZZzzZZZ\n")
                mental_health = 100
                self.current_state = "Sleep"
            elif hour == 7:
                print("It's time to wake up :)\n")
                hunger = 0
                mental_health -= 10
                self.current_state = "Morning routine"
            elif hour == 8:
                print("I'm hungry. I need to eat something for breakfast.\n")
                self.current_state = "Eat"
                hunger = 100
            elif hour % 5 == 0:
                random_event = random.choice(self.random_events)
                if random_event == "meet old friend":
                    if self.current_state == "Study":
                        print("""I met my old friend in library while studying!
I'm really glad to talk with her.
                              """)
                    elif self.current_state == "Walk":
                        print("""A chance meeting with an old friend is the
best thing that could happen today!
                              """)
                    else:
                        print("Wow! I want to spend some time to talk with my old friend!\n")
                    hunger -= 10
                    mental_health += 10
                    self.current_state = "Relax"
                if random_event == "call from mom":
                    print("Oh, my mom is calling! I'm really glad to hear her.\n")
                    hunger -= 10
                    mental_health += 10
                    self.current_state = "Relax"
                if random_event == "rain":
                    print("Oh no, It's raining outside :(\n")
                    hunger -= 10
                    mental_health -= 20
            elif hour == 13:
                print("I was a little hungry. It's time to have lunch.\n")
                hunger = 100
                self.current_state = "Eat"
            elif mental_health < 40:
                print("I feel so bad. I need a little rest.\n")
                mental_health += 50
                hunger -= 10
                self.current_state = "Relax"
            elif hour == 14:
                print("A little walk will help me study better.\n")
                hunger -= 10
                mental_health += 10
                self.current_state = "Walk"
            elif hour == 18:
                print("I was a little hungry. It's time to have dinner.\n")
                hunger = 100
                self.current_state = "Eat"
            else:
                if self.current_state == "Study":
                    print("Still studying...")
                else:
                    print("I have some time to study and prepare to exams.\n")
                mental_health -= 10
                hunger -= 10
                self.current_state = "Study"

            print(f"{hour}:00 {self.current_state}")
            print(f"Mental health: {mental_health}, Hunger: {hunger}\n\n")
            hour += 1

if __name__ == "__main__":
    day = FiniteStateMachine()
    day.run()
