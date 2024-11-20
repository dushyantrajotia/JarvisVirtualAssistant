# Importing necessary libraries
import tkinter as tk  # for creating GUI
from tkinter import scrolledtext
import speech_recognition as sr  # For speech recognition
import pyttsx3  # For text-to-speech conversion
import datetime  # For handling date and time functions
import webbrowser  # For opening web pages
import os  # For interacting with the operating system
import random
import sys  # For redirecting output
import ctypes
import subprocess

def is_debugger_present():
    """Check if the application is being debugged on Windows."""
    # Uses Windows API to detect debugger presence
    return ctypes.windll.kernel32.IsDebuggerPresent() != 0

def check_debugging_processes():
    """Look for common debugging or reverse engineering tools."""
    debug_processes = ['ollydbg', 'x64dbg', 'ida', 'wireshark', 'processhacker']
    try:
        # Get the list of running processes
        process_list = subprocess.check_output("tasklist").decode('utf-8').lower()
        for process in debug_processes:
            if process in process_list:
                print(f"Debugging tool detected: {process}")
                return True
    except Exception as e:
        print(f"Error checking processes: {e}")
    return False

def prevent_debugging():
    """Prevent execution if debugging tools or debuggers are detected."""
    if is_debugger_present():
        print("Debugger detected! Exiting...")
        sys.exit(1)

    if check_debugging_processes():
        print("Reverse engineering tool detected! Exiting...")
        sys.exit(1)

# Call this function at the beginning of your script
prevent_debugging()

print("No debuggers found, application running securely.")

#END OF DEBUGGING AND CRACKERS CHECK

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set up the GUI window
root = tk.Tk()
root.title("Jarvis - Virtual Assistant")
root.geometry("500x500")  # Set the requested window size
root.configure(bg="#333333")  # Set background color
root.resizable(False, False)  # Make the window size fixed

# Create a scrolled text box to display dialogues and logs
text_box = scrolledtext.ScrolledText(root, width=45, height=15, wrap=tk.WORD, state="disabled", bg="#f0f0f0")
text_box.pack(pady=10)

def print_to_gui(text):
    """Prints text to the GUI text box."""
    text_box.config(state="normal")
    text_box.insert(tk.END, text + "\n")
    text_box.yview(tk.END)
    text_box.config(state="disabled")

# Redirecting all print statements to the GUI text box
class StdoutRedirector:
    def write(self, text):
        print_to_gui(text)
    def flush(self):
        pass

sys.stdout = StdoutRedirector()

def speak(audio):
    """Converts text to speech and displays it in the GUI."""
    print_to_gui("Jarvis: " + audio)
    engine.say(audio)
    engine.runAndWait()

def greet_user():
    """Greets the user based on the current time of day."""
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Jarvis, your virtual assistant. How can I help you today?")

def take_command():
    """Listens for a command from the user and returns it as text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print_to_gui("Listening...")
        text_box.update_idletasks()  # Force GUI update to show "Listening..."
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print_to_gui("Recognizing...")
        text_box.update_idletasks()  # Force GUI update to show "Recognizing..."
        query = recognizer.recognize_google(audio, language='en-in')
        print_to_gui(f"User said: {query}\n")
    except Exception as e:
        print_to_gui("Sorry, I didn't catch that. Please say that again.")
        return "None"
    return query.lower()

def open_application(command):
    """Opens a specific application on the PC based on the user's command."""
    if 'open notepad' in command:
        speak("Opening Notepad")
        os.system("notepad")
    elif 'open command prompt' in command or 'open cmd' in command:
        speak("Opening Command Prompt")
        os.system("start cmd")
    elif 'open settings' in command:
        speak("Opening Settings")
        os.system("start ms-settings:")
    elif 'open microsoft store' in command or 'open store' in command:
        speak("Opening Microsoft Store")
        os.system("start ms-windows-store:")
    elif 'open calculator' in command:
        speak("Opening Calculator")
        os.system("calc")
    elif 'open paint' in command:
        speak("Opening Paint")
        os.system("mspaint")
    elif 'open file explorer' in command or 'open explorer' in command:
        speak("Opening File Explorer")
        os.system("explorer")
    elif 'open task manager' in command:
        speak("Opening Task Manager")
        os.system("taskmgr")
    else:
        speak("Sorry, I don't recognize that application command.")

def open_website(command):
    """Opens a website based on user's command."""
    if 'open youtube' in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif 'open instagram' in command:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")
    elif 'open whatsapp' in command:
        speak("Opening Whatsapp")
        webbrowser.open("https://www.whatsapp.com")
    elif 'open discord' in command:
        speak("Opening Discord")
        webbrowser.open("https://www.discord.com")
    elif 'open facebook' in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")
    elif 'open telegram' in command:
        speak("Opening Telegram")
        webbrowser.open("https://web.telegram.org")
    elif 'open amazon' in command:
        speak("Opening Amazon")
        webbrowser.open("https://www.amazon.com")
    elif 'open flipkart' in command:
        speak("Opening Flipkart")
        webbrowser.open("https://www.flipkart.com")
    elif 'open netflix' in command:
        speak("Opening Netflix")
        webbrowser.open("https://www.netflix.com")
    elif 'open amazon prime' in command:
        speak("Opening Amazon Prime")
        webbrowser.open("https://www.primevideo.com")
    elif 'open spotify' in command:
        speak("Opening Spotify")
        webbrowser.open("https://www.spotify.com")
    elif 'open steam' in command:
        speak("Opening Steam")
        webbrowser.open("https://store.steampowered.com")
    elif 'open google classroom' in command:
        speak("Opening Google Classroom")
        webbrowser.open("https://classroom.google.com")
    elif 'open google mail' in command or 'open gmail' in command:
        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com")
    elif 'open chatgpt' in command:
        speak("Opening ChatGPT")
        webbrowser.open("https://chat.openai.com")
    else:
        speak("Sorry, I don't recognize that website command.")

def play_music():
    """Plays a random music file from a specified directory."""
    music_dir = 'C:\\Users\\Hp\\Music'
    songs = os.listdir(music_dir)
    if songs:
        song = random.choice(songs)
        os.startfile(os.path.join(music_dir, song))
        speak("Playing music")
    else:
        speak("No music files found in the directory.")

def get_time():
    """Tells the current time in hours and minutes."""
    time_now = datetime.datetime.now().strftime("%H:%M")
    speak(f"The time is {time_now}")

def main():
    """Main function to process user commands in a non-blocking way."""
    query = take_command()

    if query != "None":
        if any(kw in query for kw in [
            'open youtube', 'open google', 'open stack overflow', 'open instagram',
            'open discord', 'open facebook', 'open amazon', 'open flipkart', 'open whatsapp',
            'open spotify', 'open steam', 'open google classroom', 'open google mail', 
            
            'open gmail', 'open telegram', 'open netflix', 'open amazon prime', 'open chatgpt']):
            open_website(query)
        elif any(kw in query for kw in [
            'open notepad', 'open command prompt', 'open cmd', 'open settings',
            'open microsoft store', 'open store', 'open calculator', 'open paint', 
            'open file explorer', 'open explorer', 'open task manager']):
            open_application(query)
        elif 'play music' in query:
            play_music()
        elif 'the time' in query:
            get_time()
        elif any(kw in query for kw in ['exit', 'quit', 'see you', 'bye']):
            speak("Goodbye!")
            root.quit()
            return

    # Call main() again after a short delay to keep checking for commands
    root.after(1000, main)  # Run `main()` every 1 second

def start_assistant():
    """Starts the assistant, greets the user, and initializes the command loop."""
    greet_user()
    root.after(1000, main)  # Start the main command loop after greeting

# Create a button to start the assistant
start_button = tk.Button(root, text="Start Assistant", command=start_assistant, bg="#4CAF50", fg="white", width=15, height=2)
start_button.pack(pady=(50, 5))

# Create an exit button to close the GUI
exit_button = tk.Button(root, text="Exit", command=root.quit, bg="#f44336", fg="white", width=15, height=2)
exit_button.pack(pady=(5, 20))

# Start the GUI loop
root.mainloop()
