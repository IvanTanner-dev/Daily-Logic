Given a full name as a string, return their intials i.e get_initials("Tommy Millwood") should return "T.M." & get_initials("Dorothy Vera Clump Haverstock Norris") should return "D.V.C.H.N."

I found this challenge quite straight forward but need to remind myself of the methods to split a string apart and then how to join the result back together.

Lightbulb Moment: The whole function can be coded as a single line:

def get_initials(name):
return "".join([word[0] + "." for word in name.split()])

I need to practise List Comprehensions!
