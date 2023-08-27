s = "12:01:00AM"

def timeConversion(s):
    # Write your code here
    if s[-2:] == "AM" and s[:2] == "12":
        military_am = int(s[:2]) - 12
        return ("{:02d}{}".format(military_am, s[2:-2]))
    elif s[-2:] == "AM":
        return s[:-2]
    elif s[-2:] == "PM" and s[:2] == "12":
        return s[:-2]
    else:
        military_pm = int(s[:2]) + 12
        return ("{:02d}{}".format(military_pm, s[2:-2]))

print(timeConversion(s))
