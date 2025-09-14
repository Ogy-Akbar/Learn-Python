#BEGINNER PROJECT
#1 Madlibs Game

# Creating Madlibs game would involve some syntaxes like
    # input, to provide input given by the user
    # String Concatenation for the madlibs paragraph

# Few way to do the concetanation
    # print( "subscribe to " + youtuber)
    # print("subscribe to {}".format(youtuber))
    # print (f"subscribe to {youtuber})

welcome = "Welcome to MadLibs game please fill these words below!\n"
print(welcome)


food1 = input("food: ")
food2 = input("food: ")
hobby = input("hobby: ")
videogame = input("video game: ")
friend1 = input("friend's name: ")
friend2 = input("friend's name: ")
friend3 = input("friend's name: ")
friend4 = input("friend's name: ")


madlib = f"My brother's name is Ogan. His favorite food is {food1}, His most hated food is {food2} \
His hobby is {hobby} with his most loved games is {videogame}. He aLso loves to play with his friends, \
{friend1}, {friend2}, {friend3}, & {friend4}."

print(madlib)
