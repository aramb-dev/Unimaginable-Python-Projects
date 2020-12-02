# Below is an example of how you would set up your entries
month_Conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
# You can use numbers as key value pairs
month_Conversions_numbers = {
    0: "January",
    1: "February",
    2: "March",
    3: "April",
    4: "May",
    5: "June",
    6: "July",
    7: "August",
    8: "September",
    9: "October",
    10: "November",
    11: "December",
}
# There are a couple of ways you could print your list.
print(month_Conversions["Nov"])
# or
print(month_Conversions.get("Mar"))
# You could create default values in the .get function
# You can pass a non-existing key value to an error message or entry
print(month_Conversions.get("Luv", "Sorry, This is not a month abbreviation"))

