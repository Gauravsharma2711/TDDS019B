import asyncio
import time


async def verify_student():
    print("Verifying student...")
    await asyncio.sleep(2)
    print("Student Verified\n")

async def fetch_attendance():
    print("Fetching Attendance...")
    await asyncio.sleep(2)
    print("Attendance Loaded \n")

async def fetch_marks():
    print("Fetching marks...")
    await asyncio.sleep(3)
    print("Marks Loaded \n")

async def main():
    print("========== Student portal ==========")
    start = time.time()
    
    await asyncio.gather(
        verify_student(),
        fetch_attendance(),
        fetch_marks()
    )
    
    end = time.time()
    print(f"Total time = {end-start:.2f} seconds")


asyncio.run(main())
