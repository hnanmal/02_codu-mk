input_id = input("아이디를 입력해주세요.\n")
members = ['pjmk007', 'carpamea', 'sharku']

### 1st try
# for member in members:
#     if member == input_id:
#         print('Hello!, ' + member)

#     else:
#         print('Who are you?')


### 2nd try
# for member in members:
#     if member == input_id:
#         print('Hello!, ' + member)
#         import sys
#         sys.exit()

#     else:
#         print('Who are you?')

for member in members:
    if member == input_id:
        print('Hello!, ' + member)
        import sys
        sys.exit()

print('Who are you?')