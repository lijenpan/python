"""Write a method which will remove any given character from a target string. 
Don't use the String.replace() method in your solution. 
If the given character is not found in the target string,
your method should raise a CharacterNotFound exception.
"""


class CharacterNotFound(Exception):
    """Exception raised for errors in the input.

    Attributes:
        value -- the character not found in the string
    """

    def __init__(self, value):
    	self.value = value

    def __str__(self):
    	return repr(self.value)


def remove_character_from_string(original_string, character_to_remove):
	if not character_to_remove in original_string:
		raise CharacterNotFound(character_to_remove)
	else:
		return original_string.translate(None, character_to_remove)

a = remove_character_from_string("ABC", 'A')
print a
remove_character_from_string("ABC", 'D')