story = """
There was a farmer who had a dog
And Bingo was his name o
BINGO
BINGO
BINGO
And Bingo was his name o
There was a farmer who had a dog
And {1} was his name o
(Clap)INGO
(Clap)INGO
(Clap)INGO
And Bingo was {1} name o
There was a farmer who had a {2}
And Bingo was his name o
(Clap){3}NGO
(Clap)(clap)NGO
(Clap)(clap)NGO
And Bingo was his nameo"""

noun = raw_input("Enter a noun: ")
pronoun = raw_input("Enter a pronoun: ")
adjective = raw_input("Enter an adjective: ")
verb = raw_input("Enter a verb: ")
print story.format(noun,pronoun,adjective,verb)
