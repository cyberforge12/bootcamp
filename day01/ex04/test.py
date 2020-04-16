from eval import Evaluator

words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coeffs = [1.0, 2.0, 1.0, 4.0, 0.5]
print(Evaluator.zip_evaluate(coeffs, words))
print(Evaluator.enumerate_evaluate(coeffs, words))
