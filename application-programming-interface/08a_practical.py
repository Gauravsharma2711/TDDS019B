import time 

def verify_student():
    print("Verifying student...")
    time.sleep(2)
    print("Student Verified\n")

def fetch_attendence():
    print("Fetching Attendance...")
    time.sleep(2)
    print("Attendance Loaded \n")

def fetch_marks():
    print("Fetching marks...")
    time.sleep(3)
    print("Marks Loaded \n")

print("========== Stundent portal ==========")

start = time.time()

verify_student()
fetch_attendence()
fetch_marks()

end = time.time()

print(f"\n Total time = {end-start:.2f} seconds")

