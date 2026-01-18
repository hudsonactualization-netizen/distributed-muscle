import os, json, time

task = os.getenv("TASK", "test")
payload = os.getenv("PAYLOAD", "")

print(f"TASK={task}")
print(f"PAYLOAD={payload}")

# Example: structured output file
result = {
    "task": task,
    "ok": True,
    "summary": f"Completed task '{task}'",
}

# Simulate work
for i in range(3):
    print(f"work_step={i+1}/3")
    time.sleep(1)

# Save JSON output (this is what you will consume on the phone)
os.makedirs("out", exist_ok=True)
with open("out/result.json", "w") as f:
    json.dump(result, f, indent=2)

print("Wrote out/result.json")
