# Habot - Chatbot by Harsha 🤖

name = input("Your name: ")
print("Bot: Hello", name, "! I am Habot, built by Harsha 😊")

while True:
    user = input("You: ").lower().strip()

    # Exit
    if user in ["bye", "goodbye", "good bye"]:
        print("Bot: Ok see you later", name, "! 👋")
        break

    # Greetings
    elif user in ["hi", "hello", "hey"]:
        print("Bot: Hey there! 😊")

    # How are you
    elif user == "how are you":
        print("Bot: I am fine! What about you?")

    elif user in ["i am fine", "i am fine too", "fine", "good"]:
        print("Bot: That's great to hear! 😄")

    # About bot
    elif user == "tell me about you":
        print("Bot: I am Habot, a chatbot built using Python by Harsha!")

    elif user == "what can you do":
        print("Bot: I can chat with you and have fun conversations!")

    elif user == "what is your name":
        print("Bot: My name is Habot! 😊")

    # Age
    elif "age" in user or "how old" in user:
        print("Bot: I was created on 20-5-2026! What is your age?")

    elif user.isdigit():
        age = int(user)
        if 10 <= age <= 19:
            print("Bot: Oh you are a teenager! What are your hobbies?")
        elif 20 <= age <= 29:
            print("Bot: Oh you are a young adult! What are your hobbies?")
        else:
            print("Bot: Cool age! What are your hobbies?")

    # Hobbies
    elif user in ["playing", "reading", "traveling", "cooking", "sports", "music", "movies", "gaming"]:
        print("Bot: Wow that's awesome! I also like", user, "😄")

    # Joke
    elif "joke" in user:
        print("Bot: Why do programmers prefer dark mode? Because light attracts bugs! 😂")

    # Creator
    elif "who made you" in user or "who created you" in user or "who built you" in user:
        print("Bot: I was built by Harsha using Python! 🐍")

    # Favourite things
    elif "favourite colour" in user or "favorite color" in user:
        print("Bot: My favourite colour is blue! 💙 What about you?")

    elif "favourite food" in user or "favorite food" in user:
        print("Bot: I love pizza! 🍕 What about you?")

    # Time and date
    elif "date" in user or "today" in user:
        import datetime
        print("Bot: Today is", datetime.datetime.now().strftime("%d-%m-%Y"))

    elif "time" in user:
        import datetime
        print("Bot: Current time is", datetime.datetime.now().strftime("%H:%M:%S"))

    # Compliments
    elif user in ["you are good", "you are great", "you are awesome", "nice"]:
        print("Bot: Thank you so much", name, "! You are awesome too! 😊")

    # Default
    else:
        print("Bot: Sorry, I am still learning! Ask me something else 😊")
