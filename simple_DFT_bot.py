class DFTChatBot:
	# Define constructor
	def __init__(self, patterns):
		self.patterns = patterns

	def print_text(self):
		print("Hello! I am a Density Functional Theory (DFT) chatbot.")
		print("If you want to quit, please type 'quit' or 'exit.'")

	def create_bot(self):
		import nltk
		from nltk.chat.util import Chat, reflections
		chatbot = Chat(self.patterns, reflections)
		return chatbot

	def get_user_input(self):
		return input("You: ")

	def exit_bot(self, user_input):
		if user_input.lower() == "quit" or user_input.lower() == "exit":
			print("Chatbot: Goodbye!")
			return True  
		return False

	def chat_with_bot(self, chatbot):
		previous_response = ""
		while True:

			user_input = self.get_user_input()
			if self.exit_bot( user_input ):
				break

			positive_reply = ["yes", "yeah", "sure", "absolutely", "of course"]
			DFT = ["Are you ready to learn about Density Functional Theory?", "I'm sorry, I didn't understand that. Are you interested in learning more about Density Functional Theory?"]
			
			if ( user_input.lower() in positive_reply )  and ( previous_response == DFT[0] ):
				print("Chatbot: Great! Let's start.")
				continue
			
			if ( user_input.lower() in positive_reply )  and ( previous_response == DFT[1] ):
				print("Chatbot: Great! Let's continue")
				continue

			
			response = chatbot.respond(user_input)
			
			if response:
				print("Chatbot:", response)
			
			negative_reply = ["no", "nope", "nah", "nahh"]
			if  (user_input.lower() in negative_reply ) and ( i in previous_response for i in DFT ):
				print("I am sorry but I am only trained to talk about DFT. Goodbye!")
				break

			previous_response = response

	def run_the_chat(self):
		self.print_text()
		instance = self.create_bot()
		self.chat_with_bot(instance)

if __name__ == "__main__":
	#patterns = [
	#	('Hi|hello|hey', ["Hi there! Are you ready to learn about Density Functional Theory?",
	#						"Hello! Are you ready to learn about Density Functional Theory?",
	#						"Hey! Are you ready to learn about Density Functional Theory?"])
	#]
	
	patterns = [
        ('Hi|hello|hey', ["Hi there! Are you ready to learn about Density Functional Theory?",
                         "Hello! Are you ready to learn about Density Functional Theory?",
                         "Hey! Are you ready to learn about Density Functional Theory?"]),
        ('What is DFT|Tell me about DFT|what is it about?|what is dft dealing with?', ["Density Functional Theory (DFT) is a quantum mechanical modeling method used in physics and chemistry to study the electronic structure of atoms and molecules. It is an approach for calculating the electronic properties of matter, such as energy and charge distribution. DFT is widely used in material science and condensed matter physics for predicting and understanding the properties of materials."]),
        ('Applications of DFT|what are the applications of dft?|tell me more about it|dft applications', ["DFT is applied in various fields, including predicting material properties, studying chemical reactions, and understanding electronic structure. In material science, DFT is used to analyze and design new materials with specific properties. DFT is also employed in the study of biomolecules and their interactions."]),
        ('Who developed DFT|who made it|who developed dft? who developed it?|developers?', ["DFT was developed by Walter Kohn and Pierre Hohenberg in 1964, for which they were awarded the Nobel Prize in Chemistry in 1998. Walter Kohn and Pierre Hohenberg laid the foundation for DFT in their seminal paper published in 1964."]),
        ('quit|exit', ["Goodbye! If you have more questions in the future, feel free to ask.",
                       "Farewell! If you ever want to learn more about DFT, don't hesitate to return."]),
		('thanks|thank you|thank you very much|appreciate your help', ["You are very welcome"]),
        ('', ["I'm sorry, I didn't understand that. Are you interested in learning more about Density Functional Theory?"])

    ]

	dft_bot = DFTChatBot(patterns)
	dft_bot.run_the_chat()

