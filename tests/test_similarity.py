# analyzer.similarity = similarity.py file
# similarity score is the function we want to test.
from analyzer.similarity import similarity_score

def test_identical_texts_score_one():

    # assert checks whether a condition is true.
    # checking for identical text produce a similarity very close to 1.0.
    # used 0.99 instead pf 1.0 because floating point calculations can produce tiny precision differences.
    assert similarity_score("python flask sql", "python flask sql") > 0.99

# it checks for unrelated texts
# similarity score should be low
def test_unrelated_texts_score_low():
    assert similarity_score("python flask sql", "cooking baking recipes") < 0.1

# if the input is empty it must explicitly returns 0.0
def  test_empty_text_scores_zero():
    assert similarity_score("","python") == 0.0