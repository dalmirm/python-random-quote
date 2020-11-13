def main():
  

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  for indQuote in quotes:
    print(indQuote)

if __name__== "__main__":
  main()
