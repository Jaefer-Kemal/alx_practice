def check_vote(age):
    result = "You can't vote"
    if age>18:
        def update_result(age):
            nonlocal result
            result = f"You are eligible to vote because you are above 18"
        update_result(age)
        
    return result
            
print(check_vote(int(input("Let's see if you are eligible to vote\n What is your Age: "))))