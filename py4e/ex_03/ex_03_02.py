sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, please enter numeric")
    quit()
print(fh,fr)
if fh > 40:
    print("Overtime")
    reg = fh * fr
    otp = (fh - 40) * (fr * 0.5)
    #print(reg, otp)
    xp = reg + otp
else:
    print("Regular")
    xp = fh * fr
print("Pay: ",xp)
