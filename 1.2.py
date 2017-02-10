import random
import string
FIELD = string.digits + string.letters
def generate(n, many=1, where=None):
    def getCode(n):
        return "".join(random.sample(FIELD, n))
    gene = [getCode(n) for i in range(many)]
    return gene
def writeIn(n, many, where):
    count = 1
    for i in generate(n, many):
        with open(where, "a") as boom:
            boom.write(str(count).rjust(3)+"  "+i+"\n")
        count += 1
if __name__ == '__main__':
