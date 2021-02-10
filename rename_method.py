# by Kami Bigdely
# Rename Method
# Reference: https://parade.com/1039985/marynliles/pick-up-lines/

def calulate_area_under_graph(graph):
    """Calculate the area under the input graph."""
    # bla bla bla.
    pass

#####################

def find_max(li):
    m = li[0]
    for value in li:
        if value > m:
            m = value
    return m


li = [5, -1, 43, 32, 87, -100]
print(find_max(li))

############################
def split_by_words(sentence):
    words = sentence[0:].split(' ')
    return words

print(split_by_words('If you were a vegetable, you’d be a ‘cute-cumber.'))
