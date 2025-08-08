import requests
import json
api = "http://localhost:3000/users"

user_data = requests.get(api)
print(user_data.json())

api1= "http://localhost:3000/users"

send_data =  {"id":"3" , "Name":"ram"}
send_data= json.dumps(send_data)
send_user = requests.post(api1,data=send_data)
print(send_user.json())


  
api2 = "http://localhost:3000/users/3"
 
put_data = {
    "id": "3",
    "Name": "siddhu",
    "branch": "42"
}
put_data=json.dumps(put_data)
put_user = requests.put(api2,data=put_data)
print(put_user)


  
api3 = "http://localhost:3000/users/3"
 
put_data = {
    
    "branch": "42"
}
put_data=json.dumps(put_data)
put_user = requests.patch(api3,data=put_data)
print(put_user)


api4 ="http://localhost:3000/products"

user_data = requests.get(api4)
print(user_data.json())

api5="http://localhost:3000/products"

send_data =  {
    "id": 16,
      "title": "Sony WH-1000XM5 Wireless Industry Leading Active Noise Cancelling Headphones, 8 Mics for Clear Calling, 30Hr Battery, 3 Min Quick Charge = 3 Hours Playback, Multi Point Connectivity, Alexa-Silver",
      "image": "https://storage.googleapis.com/fir-auth-1c3bc.appspot.com/1692941008275-headphone3.jpg",
      "price": 362,
      "description": "Industry Leading noise cancellation-two processors control 8 microphones for unprecedented noise cancellation. With Auto NC Optimizer, noise cancelling is automatically optimized based on your wearing conditions and environment.\r\nIndustry-leading call quality with our Precise Voice Pickup Technology uses four beamforming microphones and an AI-based noise reduction algorithm\r\nMagnificent Sound, engineered to perfection with the new Integrated Processor V1\r\nCrystal clear hands-free calling with 4 beamforming microphones, precise voice pickup, and advanced audio signal processing.",
      "brand": "song",
      "model": "WH1000XM5/SMIN",
      "color": "white",
      "category": "audio",
      "popular": "true",
      "discount": 21
  }


send_data= json.dumps(send_data)
send_user = requests.post(api5,data=send_data)
print(send_user.json())