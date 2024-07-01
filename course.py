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
