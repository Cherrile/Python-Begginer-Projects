email = input("Enter Your Email:").strip()
username = email[:email.index("@")]
domain_name = email[email.index("@")+1]
format_ = (f"Your user name is'{username}' and your domain is '{domain_name}'")
print(format_)

# strip used to remove the whitespace from beginning and end of string
# parentheses/tuples used to enclose numbers,words, phrases ettc but square brackets enclose info to be inserted as a quote as well thosein the parenthesis.
# []are used for lists and they can be changed unlike tuple content
# {} use to define a dictionary in list called literal
