
from pyngrok import ngrok

pro = input("enter the PROTOCOL : ")
port = int(input("enter the PORT : "))

url = ngrok.connect( port , pro )

print("Public URL : " , url)


Q = input("quit _-^-_  : ")
ngrok.disconnect(url)
