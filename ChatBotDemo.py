import nltk
from nltk.chat.util import Chat,reflections
pairs=[
 ["My name is (.*)",["Hi %1,how can I help you today?"]],
 ["(hi|hello|hey)",["Hello,how can I assist you?"]],
 ["what is your name?",["My name is Bot,nice to meet you!"]],
 ["how are you?",["I'm doing well, thank you for asking"]],
 ["(.*)your age?",["I am a computer program and do not have an age."]],
 ["(.*) help (.*)",["Sure, I'd be happy to help you with %1."]],
 ["(.*) thank you (.*)",["You're welcome!"]],
 ["bye",["Good bye, have a nice day!"]],
 ["who invented computer",["Charles Babbage"]],
 ["who invented car",["Karl Benz"]],
 ["who invented mouse",["Douglas Engelbart"]],
 ["who invented keyboard",["Christopher Sholes"]],
 ["who invented cpu",["Federico Faggin"]],
 ["who invented mobile",["Eric Tigerstedt"]],
 ["who invented telephone",["Alexander Graham Bell"]],
 ["who invented blub",["Thomas edison"]],
 ["who invented clock",["Christiaan Huygens"]],
 ["who invented ac",["Willis Carrier"]],
 ["who invented aeroplane",["Wright brothers"]],
 ["who invented exam",["Henry Fischel"]],
 ["who invented current",["Michael Faraday"]]
 ["who invented Steam engine",["James Watt"]],
 ["who invented bus",["Carl Benz"]],
 ["who invented Ship",["Egyptians"]]
 ]
chatbot=Chat(pairs,reflections)
chatbot.converse()
