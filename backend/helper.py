import random 
import string 
import os 
from datetime import datetime

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


def randomize_inmemory(max_size=2000000): 
    start = datetime.now()   
    report = [0,0,0,0]
    generator = RandomGenerator()
    filename = generator.generate_random_alphabet() + ".txt"
    target_file = f"output/{filename}"
    # output = open(target_file,'w')
    output = ""
    while True:
        result = generator.randomize()
        if len(output)+len(str(result['output']))<=max_size:
            report[result['type']]+=1
            output+=","+str(result['output'])
        else:
            break
    file_handler = open(target_file,'w')
    file_handler.write(output)
    file_handler.close()
    end = datetime.now()
    return {"output": target_file, "filename": filename, "size": os.path.getsize(target_file), "report": report,"eta":end-start}

def randomize_infile(max_size=2000000): 
    start = datetime.now()   
    report = [0,0,0,0]
    generator = RandomGenerator()
    filename = generator.generate_random_alphabet() + ".txt"
    target_file = f"output/{filename}"
    output = open(target_file,'w')
    while True:
        result = generator.randomize()
        if os.path.getsize(target_file)+len(str(result['output']))<=max_size:
            report[result['type']]+=1
            print(result['output'],end=",", file=output)
        else:
            break
    output.close()
    end = datetime.now()
    return {"output": target_file, "filename": filename, "size": os.path.getsize(target_file), "report": report,"eta":end-start}