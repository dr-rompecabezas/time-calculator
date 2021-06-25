# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main


# print("Test #1 expects 5:42 PM\n", add_time("3:30 PM", "2:12"), "\n")
# print("Test #2 expects 3:07 PM \n", add_time("11:55 AM", "3:12"), "\n")
# print("Test #3 expects 2:45 AM (next day)\n", add_time("9:15 PM", "5:30"), "\n")
# print("Test #4 expects 12:05 PM\n", add_time("11:40 AM", "0:25"), "\n")
# print("Test #5 expects 2:59 AM (next day)\n", add_time("2:59 AM", "24:00"), "\n")
# print("Test #6 expects 12:04 AM (2 days later)\n", add_time("11:59 PM", "24:05"), "\n")
# print("Test #7 expects 6:18 AM (20 days later)\n", add_time("8:16 PM", "466:02"), "\n")
# print("Test #8 expects 5:01 AM\n", add_time("5:01 AM", "0:00"), "\n")
# print("Test #9 expects 5:42 PM, Monday\n", add_time("3:30 PM", "2:12", "Monday"), "\n")
# print("Test #10 expects 2:59 AM, Sunday (next day)\n", add_time("2:59 AM", "24:00", "saturDay"), "\n")
# print("Test #11 expects 12:04 AM, Friday (2 days later)\n", add_time("11:59 PM", "24:05", "Wednesday"), "\n")
# print("Test #12 expects 6:18 AM, Monday (20 days later)\n", add_time("8:16 PM", "466:02", "tuesday"), "\n")


# Run unit tests automatically
main(module='test_module', exit=False)