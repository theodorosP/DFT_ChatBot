import nltk
from nltk.chat.util import Chat, reflections


class DFTChatBot:
    def __init__(self, patterns):
        self.patterns = patterns

    def print_text(self):
        print("Hello! I am a Density Functional Theory (DFT) chatbot.")
        print("If you want to quit, please type 'quit' or 'exit.'")

    def create_bot(self):
        chatbot = Chat(self.patterns, reflections)
        return chatbot

    def get_user_input(self):
        return input("You: ")

    def exit_bot(self, user_input):
        if user_input.lower() == "quit" or user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            return True
        return False

    def check_positive_response(self, user_input, previous):
        positive_reply = ["yes", "yeah", "yeahh", "yeahhh" "sure", "absolutely", "of course"]
        DFT = ["Are you ready to learn about Density Functional Theory?",
               "I'm sorry, I didn't understand that. Are you interested in learning more about Density Functional Theory?"]
        if (user_input.lower() in positive_reply) and (DFT[0] in previous or DFT[1] in previous):
            print("Chatbot: Great! Let's start.")
            return True

        return False

    def check_negative_response(self, user_input, previous):
        DFT = ["Are you ready to learn about Density Functional Theory?",
               "I'm sorry, I didn't understand that. Are you interested in learning more about Density Functional Theory?"]
        negative_reply = ["no", "nope", "nah", "nahh"]
        if (user_input.lower() in negative_reply) and any(i in previous for i in DFT):
            print("I am sorry but I am only trained to talk about DFT. Goodbye!")
            return True
        return False

    def chat_with_bot(self, chatbot):
        previous_response = ""
        while True:
            user_input = self.get_user_input()
            if self.exit_bot(user_input):
                break

            if self.check_negative_response(user_input, previous_response):
                break

            if self.check_positive_response(user_input, previous_response):
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
        ('Hi|hello|hey', ["Hi there! Are you ready to learn about Density Functional Theory?",
                          "Hello! Are you ready to learn about Density Functional Theory?",
                          "Hey! Are you ready to learn about Density Functional Theory?"]),
        ('What is DFT|Tell me about DFT|what is it about?|what is dft dealing with?|what is it?|what is this?',
         ["Density Functional Theory (DFT) is a quantum mechanical modeling method used in physics and chemistry to study the electronic structure of atoms and molecules. It is formulated to obtain ground state properties of various systems."]),
        ('Applications of DFT|what are the applications of dft?|tell me more about it|dft applications|its applications|applications|tell me more about DFT|tell me more|tell me more about it|tell me more aboyt DFT|more|tell more',
         ["DFT is applied in predicting material properties, studying chemical reactions, understanding electronic structure, and modeling the behavior of atoms and molecules."]),
        ('Who developed DFT?|who made it?|who developed dft? who developped it?|developer?|developer?|Who develop it?|who deveole dft?|who developped it?',
         ["DFT was developed by Walter Kohn and Pierre Hohenberg in 1964, for which they were awarded the Nobel Prize in Chemistry in 1998."]),
        ('How does DFT work|explain DFT working principle|working of DFT|How DFT works?',
         ["DFT approximates the many-body quantum problem into a non-interacting electron problem, using the electron density. However, predicting exact band gaps of semiconductors and insulators can be challenging due to certain theoretical limitations."]),
        ('advantages|pros|advantages of DFT|pros of DFT|DFT pros|pros',
         ["Density Functional Theory (DFT) stands out as a highly advantageous computational method in quantum chemistry and condensed matter physics. Its notable efficiency stems from its focus on electron density rather than wave functions, rendering it computationally more feasible compared to other many-body methods. This efficiency allows for the study of large and intricate systems, making DFT particularly valuable in materials science and biological applications. DFT excels in predicting ground-state properties, offering accurate insights into total energy, electronic density, and structural parameters. Its versatility extends across various materials, encompassing metals, insulators, semiconductors, and molecules. The method's foundation in quantum mechanics provides a rigorous framework for understanding electronic structure and properties. DFT's incorporation of exchange-correlation effects enables a reasonably accurate treatment of electron-electron interactions without the need for explicit many-body wave functions. With its predictive power, DFT guides experimental investigations, aiding in the design of new materials and unraveling chemical reactivity and bonding in molecules."]),
        ('Limitations of DFT|cons of using DFT|drawbacks of DFT|limitations?|cons?|limitations of dft?',
         ["DFT, despite being powerful, faces challenges in predicting exact band gaps of semiconductors and insulators. The Hohenberg-Kohn theorem states the external potential is uniquely determined by the ground-state charge density, but practical functionals struggle with excited-state properties. The fundamental band gap for a system is given by differences in ground-state total energies of systems with deviating numbers of electrons. While DFT can calculate ground-state total energies, the Kohn-Sham band structure may not represent the fundamental gap of the interacting-electron system accurately."]),
        ('Pseudopotentials in DFT|What are pseudopotentials?',
         ["Pseudopotentials are used in DFT to replace core electrons, making calculations more efficient. They help reduce computational cost while maintaining accuracy in electronic structure calculations."]),
        ('Do you know any DFT software?|Do you know DFT software?|DFT Software|What are some popular software tools used for DFT calculations?|Software|Simulation software?',
         ["Some widely used software tools for DFT calculations include VASP (Vienna Ab initio Simulation Package), Quantum ESPRESSO."]),
        ('Hybrid Functionals|functionals|what are the hybrid functionals?',
         ["Hybrid functionals combine a fraction of exact exchange with the exchange-correlation functionals used in standard DFT calculations. They are often employed to improve the accuracy of predictions for electronic properties."]),
        ('Do you know about VASP?|VASP|Vienna Ab initio Simulation Package',
         ["VASP is a widely used software package for accurate ab initio quantum-mechanical calculations, commonly employed for electronic structure calculations using DFT."]),
        ('Quantum ESPRESSO',
         ["Do you know about quantum espresso?|Quantum ESPRESSO is an open-source software suite for ab initio quantum-mechanical calculations, used for electronic structure calculations based on DFT."]),
        ('Nuclei stability in DFT|Stability of atomic nuclei',
         ["DFT can predict the stability of atomic nuclei by calculating binding energies and studying nuclear structure, providing insights into their properties under different conditions."]),
        ('can you describe DFT algorithm?|DFT algorithm|algorithm|algo?|What is the algorith of DFT?|What is DFT algorithm?|Tell me about DFT algorithm|Tell me about its algorithm',
         ["In the grid-based implementation of the Kohn-Sham approach within Density Functional Theory (DFT), the algorithm operates on a discretized representation of three-dimensional space. Initially, the space is subdivided into a grid of points (riri​), where each point corresponds to a specific position in space. The electron density (ρ(ri)ρ(ri​)) is then initialized based on an initial guess at each grid point. Subsequently, the Kohn-Sham equations are discretized on the grid, resulting in a set of linear equations of the form HKSψi(rj)=ϵiψi(rj)HKS​ψi​(rj​)=ϵi​ψi​(rj​), where ψi(rj)ψi​(rj​) represents the value of the Kohn-Sham orbital at grid point rjrj​. The solution to these equations provides the Kohn-Sham orbitals throughout the grid. The electron density is then updated using these orbitals, and the process iterates until self-consistency is achieved. This grid-based approach enables a numerical solution to the Kohn-Sham equations, offering a practical means to approximate the electronic structure of the system. Implementation in Python involves managing the grid points, solving the discretized equations, and updating the electron density on the grid iteratively.\n I apologize for not writing the indices correctly, but I am still learning to do so"]),
        ('what will you be doing in the future?|Future Plans?',
         ["I will be trained to design simulations for any system you ask me about in computational material science."]),
        #('Do you have data from Simulations?|semiconductor results|semi conductor results|semi-conductor results|',
         #[" Up to about 1.33ML, the chemical potential stays below that of bulk Pb and 2 Pb layers, meaning the wetting layer is more favorable even as Pb coverage rises slightly beyond the bulk Pb(111) density of 1.30ML. Above 1.33ML, the chemical potential sharply rises above that of the other two states, and since the chemical potential of bulk Pb is the lower of the two, Pb begins forming islands rather than assembling a second layer. This explains the compression of the wetting layer and the sudden, explosive nucleation of Pb islands."]),
        ('quit|exit', ["Goodbye! If you have more questions in the future, feel free to ask.",
                       "Farewell! If you ever want to learn more about DFT, don't hesitate to return."]),
        ('thanks|thank you|thank you very much|appreciate your help', ["You are very welcome"]),
        ('', ["I'm sorry, I didn't understand that. Are you interested in learning more about Density Functional Theory?"])
    ]

    dft_bot = DFTChatBot(patterns)
    dft_bot.run_the_chat()
