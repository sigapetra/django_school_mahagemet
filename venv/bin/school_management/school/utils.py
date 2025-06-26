import requests
from .models import Teacher, Class

def fetch_dummy_teachers():
    # Fetching fake teacher data from dummyjson API
    response = requests.get("https://dummyjson.com/users?limit=5")  # You can adjust the API endpoint and limit
    if response.status_code == 200:
        data = response.json()
        teachers_data = data.get('users', [])
        
        if teachers_data:
            for teacher_data in teachers_data:
                try:
                    # Assuming the dummyjson 'users' array contains firstName and lastName fields
                    teacher_name = f"{teacher_data.get('firstName', '')} {teacher_data.get('lastName', '')}"
                    
                    # Fetching or creating the first class (ensure at least one class exists)
                    assigned_class = Class.objects.first()  # You may want to change the logic here

                    if assigned_class:  # Ensure that a class is available
                        teacher = Teacher.objects.create(
                            name=teacher_name,
                            class_assigned=assigned_class
                        )
                        print(f"Teacher {teacher_name} added to class {assigned_class.name}")
                    else:
                        print("No class available to assign.")
                except Exception as e:
                    print(f"Error creating teacher: {e}")
            return True
        else:
            print("No teachers data found.")
    else:
        print(f"Error fetching data: {response.status_code}")
    return False
