def reverse_string(s):
    return " ".join(reversed(s.split()))

print(reverse_string("iam a good boy"))




# in more detail 

def reverse_str(s):
    s = s.split() # split the string into list
    s.reverse()    # reverse the list
    " ".join(s)     # joins the items in the list
    return s

print(reverse_str("live young live free"))