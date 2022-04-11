import pickle


def unpickle():
    filename = "dogs"

    infile = open(filename,'rb')
    new_dict = pickle.load(infile)
    infile.close()

    print(new_dict)


if __name__ == "__main__":
    unpickle()
