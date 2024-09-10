paragraph = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Omnis adipisci commodi assumenda optio placeat accusamus expedita eligendi porro aperiam consequuntur quod vero iusto, eaque ipsam harum aliquid distinctio possimus deserunt? is there or in the ia is there the is"
word1 = input("Which Word You want to repklace: ")
word2 = input("wjhich word you want to replaced by : ")
paragraph = paragraph.replace(word1,word2)
replaced_paragraph = ''.join(paragraph)
print(replaced_paragraph)
'''
Lorem ipsum dolor sit amet, consectetur adipisicing (*lite*). Omnis adipisci commodi assumenda optio placeat accusamus expedita eligendi porro aperiam consequuntur quod vero iusto, eaque ipsam harum aliquid distinctio possimus deserunt? is there or in the ia is there the is
'''