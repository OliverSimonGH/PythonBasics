import city
import sys

print(sys.argv)
print(len(sys.argv))
print("The popualtion of {} is {} and it has a size of {}.".format(sys.argv[1], sys.argv[2], sys.argv[3]))

if len(sys.argv) < 3:
    print("Nope")
    sys.exit(1)
else:
    for arg in sys.argv:
        print(arg)
