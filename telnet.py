import socket
import rospy
from std_msgs.msg import String

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("192.168.245.63", 28097))
dataTampung = ""

while True:
    data = str(s.recv(1024),encoding='utf-8')
    # print(data)

    # cyan data
    if(data=="W"):
        dataTampung = "ChCy"
        print (data," ==> Team Cyan")
    elif(data=="K"):
        dataTampung = "KoCy"
        print (data," ==> KickOf Team Cyan")
    elif(data=="s"):
        dataTampung = "StCy"
        print (data," ==> Start Team Cyan")
    elif(data=="S"):
        dataTampung = "EnCy"
        print (data," ==> Stop Team Cyan")
    elif(data=="F"):
        dataTampung = "FrCy"
        print (data," ==> FreeCick Team Cyan")
    elif(data=="G"):
        dataTampung = "GkCy"
        print (data," ==> GoalKick Team Cyan")
    elif(data=="T"):
        dataTampung = "ThCy"
        print (data," ==> ThrowIn Team Cyan")
    elif(data=="C"):
        dataTampung = "CoCy"
        print (data," ==> CornerKick Team Cyan")
    elif(data=="P"):
        dataTampung = "PenCy"
        print (data," ==> PenaltyKick Team Cyan")
    elif(data=="N"):
        dataTampung = "DroCy"
        print (data," ==> DroppedBall Team Cyan")
    elif(data=="O"):
        dataTampung = "RepCy"
        print (data," ==> Repair Team Cyan")
    elif(data=="A"):
        dataTampung = "GolCy"
        print (data," ==> Goal Team Cyan")

    # magenta data
    if(data=="W"):
        dataTampung = "ChMg"
        print (data," ==> Team Magenta")
    elif(data=="k"):
        dataTampung = "KoMg"
        print (data," ==> KickOf Team Magenta")
    elif(data=="s"):
        dataTampung = "StMg"
        print (data," ==> Start Team Magenta")
    elif(data=="S"):
        dataTampung = "EnMg"
        print (data," ==> Stop Team Magenta")
    elif(data=="f"):
        dataTampung = "FrMg"
        print (data," ==> FreeCick Team Magenta")
    elif(data=="g"):
        dataTampung = "GkMg"
        print (data," ==> GoalKick Team Magenta")
    elif(data=="t"):
        dataTampung = "ThMg"
        print (data," ==> ThrowIn Team Magenta")
    elif(data=="c"):
        dataTampung = "CoMg"
        print (data," ==> CornerKick Team Magenta")
    elif(data=="p"):
        dataTampung = "PenMg"
        print (data," ==> PenaltyKick Team Magenta")
    elif(data=="N"):
        dataTampung = "DroMg"
        print (data," ==> DroppedBall Team Magenta")
    elif(data=="o"):
        dataTampung = "RepMg"
        print (data," ==> Repair Team Magenta")
    elif(data=="a"):
        dataTampung = "GolMg"
        print (data," ==> Goal Team Magenta")

    def talker():
        pub = rospy.Publisher('chatter', String, queue_size=10)
        rospy.init_node('talker', anonymous=True)
        rate = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():
            parsing = dataTampung
            rospy.loginfo(dataTampung)
            pub.publish(dataTampung)
            rate.sleep()

if __name__ == '__main__':
    try:
         talker()
    except expression as identifier:
        pass
