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
		response_variable = ""
		while True:
			user_input = self.get_user_input()
			if self.exit_bot( user_input ):
				break

			response = chatbot.respond(user_input)
			if response:
				print("Chatbot:", response)
			if user_input == "no" and "Are you ready to learn about Density Functional Theory?" in response_variable:
				print("I am sorry but I am only trained to talk about DFT. Goodbye!")
				break

			response_variable = response


if __name__ == "__main__":
	patterns = [
		(r'Hi|hello|hey', ["Hi there! Are you ready to learn about Density Functional Theory?",
							"Hello! Are you ready to learn about Density Functional Theory?",
							"Hey! Are you ready to learn about Density Functional Theory?"])
	]

	dft_bot = DFTChatBot(patterns)
	dft_bot.print_text()

	chatbot_instance = dft_bot.create_bot()
	dft_bot.chat_with_bot(chatbot_instance)
