import time
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

def testfun(self, params,packet):
    print("received message from aws")
    print("topic: " + packet.topic)
    print("payload: ",(packet.payload))

myMQTTClient = AWSIoTMQTTClient("kbonefontID")

myMQTTClient.configureEndpoint("a2uqhwp0fcajoi-ats.iot.us-east-2.amazonaws.com", 8883) #Provide your AWS IoT Core endpoint (Example: "abcdef12345-ats.iot.us-east-1.amazonaws.com")
myMQTTClient.configureCredentials("/home/kris/aws_pi_test/src/config/AmazonRootCA1.pem", "/home/kris/aws_pi_test/src/config/private.pem.key", "/home/kris/aws_pi_test/src/config/certificate.pem.crt") 
myMQTTClient.configureOfflinePublishQueueing(-1)
myMQTTClient.configureDrainingFrequency(2)
myMQTTClient.configureConnectDisconnectTimeout(10)
myMQTTClient.configureMQTTOperationTimeout(5)
print("initiating iot topic..")
myMQTTClient.connect()

myMQTTClient.subscribe("home/testfun", 1, testfun)