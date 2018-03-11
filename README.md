# MQTT_simple
Implementing MQTT protocal with TCP based

### Requirement:
  - Any OS with Python 3++
  - Any Shell might be worked
 
### Setup Guildline:
  - setup Broker first,call your shell and run python broker.py
  - if you would like to setup Publisher go with python client.py on another shell
  - if you would like to setup Subscriber go with python subscriber.py on another shell

### Command:

 #### Publisher
  **topic "topic name"**
  Set a new topic for that publisher eg. topic mqttTest1
  
  **publish "message"**
  Send a new message to broker in order to broadcast to subscribers 
  eg. publish bnk48 is currenly on tour.
  
  **cancel "topic name**
  Cancel the current topic your publisher is on eg. cancel mqttTest1
  
  **quit**
  Quit the client - there are no arguement following quit command. eg. quit
  _Note: to set a new topic, your current topic must be canceled and to publish to broker ,your current topic must be set_
  
 #### Subscriber
  **sub "topic name**
  Set topic,you would like to subscribe  eg. sub mqttTest1
  _Note: Currrent version can still subscribe only one topic_
