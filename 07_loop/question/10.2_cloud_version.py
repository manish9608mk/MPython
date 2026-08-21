import time

wait_time = 1
max_retries = 5
attempt = 1

# Simulate that the server becomes available on the 3rd attempt
success_on = 3

while attempt <= max_retries:

    print(f"\nAttempt {attempt}/{max_retries}")

    if attempt == success_on:
        print("✅ Connected successfully!")
        break

    print("❌ Connection failed.")
    print(f"Retrying in {wait_time} second(s)...")

    time.sleep(wait_time)

    wait_time *= 2
    attempt += 1

else:
    print("\n❌ Maximum retry limit reached.")
    print("Operation failed.")


    