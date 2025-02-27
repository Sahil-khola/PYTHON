p1 = 'make lot of money'
p2 = "click this"
p3 = "buy now"

message = input("Enter your comment: ")

if( p1 in message or p2 in message or p3 in message):
    print("this comment are spam")

else:
    print("this comment is not a span") 