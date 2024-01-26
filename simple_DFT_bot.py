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

	def check_positive_respose(self, user_input, previous):
		positive_reply = ["yes", "yeah", "sure", "absolutely", "of course"]
		DFT = ["Are you ready to learn about Density Functional Theory?", "I'm sorry, I didn't understand that. Are you interested in learning more about Density Functional Theory?"]
		if ( user_input.lower() in positive_reply )  and ( DFT[0] in previous ):
			print("Chatbot: Great! Let's start.")
			return True

		if ( user_input.lower() in positive_reply )  and ( DFT[1] in previous ):
			print("Chatbot: Great! Let's continue")
			return True
		return False

	def check_negative_response(self, user_input, previous):
		DFT = ["Are you ready to learn about Density Functional Theory?", "I'm sorry, I didn't understand that. Are you interested in learning more about Density Functional Theory?"]
		negative_reply = ["no", "nope", "nah", "nahh"]
		if  ( user_input.lower() in negative_reply ) and ( i in previous for i in DFT ):
			print("I am sorry but I am only trained to talk about DFT. Goodbye!")
			return True
		return False

	def chat_with_bot(self, chatbot):
		previous_response = ""
		while True:

			user_input = self.get_user_input()
			if self.exit_bot( user_input ):
				break

			if self.check_negative_response(user_input, previous_response):
				break

			if self.check_positive_respose(user_input, previous_response):
				continue

			response = chatbot.respond(user_input)

			if response:
				print("Chatbot:", response)

			previous_response = response

	def run_the_chat(self):
		self.print_text()
		instance = self.create_bot()
		self.chat_with_bot(instance)

if __name__ == "__main__":
	patterns = [
		('Hi|hello|hey', ["Hi there! Are you ready to learn about Density Functional Theory?","Hello! Are you ready to learn about Density Functional Theory?","Hey! Are you ready to learn about Density Functional Theory?"]),
		('What is DFT|Tell me about DFT|what is it about?|what is dft dealing with?', ["Density Functional Theory (DFT) is a quantum mechanical modeling method used in physics and chemistry to study the electronic structure of atoms and molecules. It is formulated to obtain ground state properties of various systems."]),
		('Applications of DFT|what are the applications of dft?|tell me more about it|dft applications', ["DFT is applied in predicting material properties, studying chemical reactions, understanding electronic structure, and modeling the behavior of atoms and molecules."]),
		('Who developed DFT|who made it|who developed dft? who developed it?|developer?|developer?|Who develop it?|who deveole dft?', ["DFT was developed by Walter Kohn and Pierre Hohenberg in 1964, for which they were awarded the Nobel Prize in Chemistry in 1998."]),
		('How does DFT work|explain DFT working principle|working of DFT', ["DFT approximates the many-body quantum problem into a non-interacting electron problem, using the electron density. However, predicting exact band gaps of semiconductors and insulators can be challenging due to certain theoretical limitations."]),
		('Limitations of DFT|cons of using DFT|drawbacks of DFT', ["DFT, despite being powerful, faces challenges in predicting exact band gaps of semiconductors and insulators. The Hohenberg-Kohn theorem states the external potential is uniquely determined by the ground-state charge density, but practical functionals struggle with excited-state properties. The fundamental band gap for a system is given by differences in ground-state total energies of systems with deviating numbers of electrons. While DFT can calculate ground-state total energies, the Kohn-Sham band structure may not represent the fundamental gap of the interacting-electron system accurately."]),
		('Pseudopotentials in DFT|What are pseudopotentials?', ["Pseudopotentials are used in DFT to replace core electrons, making calculations more efficient. They help reduce computational cost while maintaining accuracy in electronic structure calculations."]),
		('VASP|Vienna Ab initio Simulation Package', ["VASP is a widely used software package for accurate ab initio quantum-mechanical calculations, commonly employed for electronic structure calculations using DFT."]),
		('Quantum ESPRESSO', ["Quantum ESPRESSO is an open-source software suite for ab initio quantum-mechanical calculations, used for electronic structure calculations based on DFT."]),
		('Nuclei stability in DFT|Stability of atomic nuclei', ["DFT can predict the stability of atomic nuclei by calculating binding energies and studying nuclear structure, providing insights into their properties under different conditions."]),
		('quit|exit', ["Goodbye! If you have more questions in the future, feel free to ask.", "Farewell! If you ever want to learn more about DFT, don't hesitate to return."]),
		('thanks|thank you|thank you very much|appreciate your help', ["You are very welcome"]),
		('', ["I'm sorry, I didn't understand that. Are you interested in learning more about Density Functional Theory?"])
	]



	'''
	patterns = [
        ('Hi|hello|hey', ["Hi there! Are you ready to learn about Density Functional Theory?",
                         "Hello! Are you ready to learn about Density Functional Theory?",
                         "Hey! Are you ready to learn about Density Functional Theory?"]),
        ('What is DFT|Tell me about DFT|what is it about?|what is dft dealing with?', ["Density Functional Theory (DFT) is a quantum mechanical modeling method used in physics and chemistry to study the electronic structure of atoms and molecules. It is an approach for calculating the electronic properties of matter, such as energy and charge distribution. DFT is widely used in material science and condensed matter physics for predicting and understanding the properties of materials."]),
        ('Applications of DFT|what are the applications of dft?|tell me more about it|dft applications', ["DFT is applied in various fields, including predicting material properties, studying chemical reactions, and understanding electronic structure. In material science, DFT is used to analyze and design new materials with specific properties. DFT is also employed in the study of biomolecules and their interactions."]),
        ('Who developed DFT|who made it|who developed dft? who developed it?|developer?|developer?|Who develop it?|who deveole dft?', ["DFT was developed by Walter Kohn and Pierre Hohenberg in 1964, for which they were awarded the Nobel Prize in Chemistry in 1998. Walter Kohn and Pierre Hohenberg laid the foundation for DFT in their seminal paper published in 1964."]),
        ('quit|exit', ["Goodbye! If you have more questions in the future, feel free to ask.", "Farewell! If you ever want to learn more about DFT, don't hesitate to return."]),
		('thanks|thank you|thank you very much|appreciate your help', ["You are very welcome"]),
        ('', ["I'm sorry, I didn't understand that. Are you interested in learning more about Density Functional Theory?"])

    ]
	'''
	dft_bot = DFTChatBot(patterns)
	dft_bot.run_the_chat()

