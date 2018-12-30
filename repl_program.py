# create_hash function was taken from https://bitbucket.org/damienjadeduff/hashing_example/raw/master/hash_password.py

from hashlib import sha256

def create_hash(password):
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()

password = create_hash("yildiz4you")
print(password)


comment_list = []
comment_item = ''
while True:
    comment_item = input("Enter your comment (type -1 to quit) : ")
    if comment_item != '-1':
        user_password = create_hash(input("Enter your password : "))
        if(user_password == password):
            comment_list.append(comment_item)
            print("Previously entered comments : ")
            for i in range(len(comment_list)):
                print(str(i+1)+". "+ comment_list[i])
        else:
            print("I a sorry I can’t let you do that.")
    else:
        break



