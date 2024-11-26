def game():
    print("Гра 'Цифри по порядку'. Для завершення введіть 'over'")
    stack = []
    
    while True:
        num = input("Введіть число: ")
        if num == 'over':
            print("Завершено")
            break
        
        num = int(num)
        
        if not stack or num > stack[-1]:
            stack.append(num)
            print(f"Поточний: {stack}")
        else:
            stack.pop()
            print(f"Послідовність неправильна, додайте інше правильне число")

game()
        

        









