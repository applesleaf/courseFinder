# Course Information Program

This Python program allows you to enter a course number and displays the corresponding room number, instructor, and meeting time. It utilizes dictionaries to store course information and a function to display the data based on user input.

## Description

### Dictionaries
Three dictionaries are created to store course information for room numbers, instructors, and meeting times.

- **Room Numbers**: Maps course numbers to their respective room numbers.
- **Instructors**: Maps course numbers to the names of the instructors.
- **Meeting Times**: Maps course numbers to the times when the courses meet.

### Function
`display_course_info(course_number)` is defined to display the course information based on the user input. It retrieves the room number, instructor, and meeting time from the dictionaries and prints them out.

### Main Program
The user is prompted to enter a course number, which is then used to fetch and display the corresponding course information. The main execution flow starts with this prompt.

### Input Handling
The `input()` function is used to get the course number from the user, which is then converted to uppercase to ensure the input matches the dictionary keys. This helps avoid errors due to case sensitivity.

## Usage
You can run this program, and it will prompt you to enter a course number, then display the relevant information. If an invalid course number is entered, it will notify the user.

```python
# Dictionaries containing course information
course_rooms = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

course_instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

course_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}

# Function to display course information
def display_course_info(course_number):
    room = course_rooms.get(course_number)
    instructor = course_instructors.get(course_number)
    time = course_times.get(course_number)
    
    if room and instructor and time:
        print(f"Course Number: {course_number}")
        print(f"Room Number: {room}")
        print(f"Instructor: {instructor}")
        print(f"Meeting Time: {time}")
    else:
        print("Invalid course number. Please try again.")

# Main program
def main():
    course_number = input("Enter a course number (e.g., CSC101): ").strip().upper()
    display_course_info(course_number)

if __name__ == "__main__":
    main()
