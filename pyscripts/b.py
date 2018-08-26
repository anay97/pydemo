import autocomplete

# load pickled python Counter objects representing our predictive models
# I use Peter Norvigs big.txt (http://norvig.com/big.txt) to create the predictive models
autocomplete.load()

# imagine writing "the b"
results = autocomplete.completeSearch('Sony',5)
for r in results:
	print(r)