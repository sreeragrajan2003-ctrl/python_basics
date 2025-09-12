animal = input("Enter your favourite animal name:")
print(f"I Love {animal}!")

student = input("Enter name of the student:")
age = int(input("Enter the age of student:"))
print(f"{student} is {age} years old.")

hobby = input("what is you hobby:")
print(
    f"Hi there! I'm {student}, a {age}-year-old who loves {hobby}. Nice to meet you!")

book_name = input("Enter the name of the book:")
book_author = input("Enter author name:")
book_publications = input("Enter book publications name:")
print(f"{book_publications.upper()} publications published \"{book_name.title()}\" written by {book_author.lower()}")

movie = input("Which is your favourite movie? ")
director = input("who is director of the movie?")
print(
  f"My favourite movie is {movie.title()},which is directed by {director.title()}")


name = input("What is your name? ")
age = int(input("What is your age? "))
print(f"Hey {name.title()}! you will turn {age+5} in 5 years.")

city = input("Enter the name ofthe city: ")
weather = input("Enter the weather condition in the city: ")
print(f"The weather in {city.title()} is {weather.lower()}")
