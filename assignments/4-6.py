def computepay(h,r):
    if h>40:
        return (40.0*r)+((h-40.0)*1.5*r)
    else:
        return h*r



h = input("Enter Hours:")
rt = input("Enter Rate:")


try:
    h = float(h)
    rt = float(rt)
except:
    print('Error, please enter numeric input')
    quit();


p = computepay(h,rt)
print("Pay",p)
