class Course:
    def __init__(self, name, duration, link):
        self.name = name
        self.duration = duration
        self.link = link

    def __repr__(self):
        return f"{self.name} [{self.duration}], ({self.link})"

courses=[
    Course("Introduccion a linux", 15, "intro linux link"),
    Course("Personalizacion de linux", 3, "customize linux Personalizacion"),
    Course("introuccion al hacking", 53, "intro hacling link")
]

def list_courses():
    for course in courses:
        print(course)

def search_course(name):
    for course in courses:
        if course.name == name:
            return course
        else:
            return f"\n[!] Not valid course name"
