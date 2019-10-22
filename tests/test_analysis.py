import analysis

def test_average():
    avg = analysis.average_inflammations(0)
    assert(avg == 5.45)

def test_max(): #checks if we get some answers we're expecting, i.e. the max inflammation for certain patients
    assert(analysis.max_inflammations(12) == 17)

def test_acute_patient(): #checks that the acute patient (46) indeed has an average above other patients
    assert(analysis.average_inflammations(46) > analysis.average_inflammations(5))
    assert(analysis.average_inflammations(46) > analysis.average_inflammations(10))
    assert(analysis.average_inflammations(46) > analysis.average_inflammations(15))