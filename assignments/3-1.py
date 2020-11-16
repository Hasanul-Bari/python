h = input("Enter Hours:")
rt = input("Enter Rate:")


try:

    h = float(h)
    rt = float(rt)
except:
    print('Error, please enter numeric input')
    quit();


if h>40:
    ans=(40.0*rt)+((h-40.0)*1.5*rt)
else:
    ans=h*rt

print(ans)
