#
import sys
sys.path.append(r'C:\Users\83936\Desktop\2019 MCM\CA')#保存CA和CADrawer的地址
import CA
import CADrawer


def CAplot(rule,n,initiate):
    ca = CA.CA(rule, n)
    if initiate == "single":
        ca.start_single()
    else:
        ca.start_random()
    ca.loop(n-1)
    drawer = CADrawer.PyplotDrawer()
    drawer.draw(ca)


CAplot(50,10,"random")
