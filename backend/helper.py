import random 
import string 
import os 

class Randomizer:
    ALPHABET = 0
    REALNUMBER = 1
    INTEGER = 2 
    ALPHANUMERIC = 3


class RandomGenerator():
    def randomize(self,length=None):
        selector = random.randint(1,4)
        generator = [
            self.generate_random_alphabet,
            self.generate_random_float,
            self.generate_random_int,
            self.generate_random_alphanumeric
        ]
        randomizer= random.choice(generator)
        return {'type': generator.index(randomizer), "output": randomizer()}

    def generate_random_alphabet(self):
        length = random.randint(5,25)
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    def generate_random_alphanumeric(self):
        length = random.randint(5,25)
        letters = string.ascii_lowercase + string.digits
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    def generate_random_float(self):
        return random.uniform(0,999999)

    def generate_random_int(self):
        return random.randint(0,999999)


def generate_random(max_size=2000000):    
    report = [0,0,0,0]
    generator = RandomGenerator()
    filename = generator.generate_random_alphabet() + ".txt"
    target_file = f"output/{filename}"
    output = open(target_file,'w')
    while True:
        result = generator.randomize()
        if os.path.getsize(target_file)+len(str(result))<=max_size:
            report[result['type']]+=1
            print(result['output'], file=output, end=",")
        else:
            break
    return {"output": target_file, "filename": filename, "size": os.path.getsize(target_file), "report": report}