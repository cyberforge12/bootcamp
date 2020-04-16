class Evaluator:
    def __init__(self):
        pass

    def zip_evaluate(coefs, words):
        if len(words) == len(coefs):
            len_w = [len(i) for i in words]
            return sum([i * j for i, j in zip(len_w, coefs)])
        else:
            return -1

    def enumerate_evaluate(coefs, words):
        if len(words) == len(coefs):
            return sum([len(j) * coefs[i] for i, j in enumerate(words)])
        else:
            return -1

