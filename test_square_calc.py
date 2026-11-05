from square_calc import square

def main():
    test_square()

def test_square():
        assert square(2)==4
        assert square(3)==9 #instead of if, if not true gives assertion error
        #run with pytest
def test_zero():
    assert square(0)==0

if __name__ == "__main__":
    main()