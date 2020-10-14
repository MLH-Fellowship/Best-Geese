from texttoquestion import TextToQuestion


q = TextToQuestion()

if __name__ == "__main__":
    
    text = "Oxygen is a chemical element with symbol O and atomic number 8. It is a member of the chalcogen group on the periodic table, a highly reactive nonmetal, and an oxidizing agent that readily forms oxides with most elements as well as with other compounds. By mass, oxygen is the third-most abundant element in the universe, after hydrogen and helium. At standard temperature and pressure, two atoms of the element bind to form dioxygen, a colorless and odorless diatomic gas with the formula O2. Diatomic oxygen gas constitutes 20.8% of the Earth's atmosphere. As compounds including oxides, the element makes up almost half of the Earth's crust."

    questions = q.generateQuestions(text, 9)    
    print(questions)
    wo_prob = q.remove_prob_and_send_to_db('questions.json')
    print(wo_prob[5])
