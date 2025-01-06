import psutil

procs = list(psutil.process_iter())
i = 1

for p in procs:
    print(f"{i}: Name {p.name()}")
    i += 1

idx = int(input("Enter the process number: "))
proc = procs[idx - 1]

print(f"Process ID - {proc.pid}")
print(f"Process Name - {proc.name()}")

choice = int(input("Do you want to kill this process? (1 - yes, 2 - no): "))
if choice == 1:
    proc.kill()
    print(f"Process '{proc.name()}' was killed.")