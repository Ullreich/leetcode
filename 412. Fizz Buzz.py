def fizzbuzz(n : int) -> list[str]:
    #return ["FizzBuzz" if i%3==0 and i%5==0 else "Fizz" if i%3==0 else "Buzz" if i%5==0 else str(i) for i in range(1, n+1)]

    # shorter
    #return ["Fizz"*(i % 3 == 0)+"Buzz"*(i % 5 == 0) if (i % 3*i % 5 == 0) else str(i) for i in range(1, n + 1)]

    # shorter
    [print("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) + str(i) * (i % 3 * i % 5 != 0)) for i in range(1, 101)]
    #[print(str(i) * (i % 3 * i % 5 == 0)) for i in range(1, 101)]
fizzbuzz(15)"]