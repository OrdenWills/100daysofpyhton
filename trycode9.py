friends_invited=['john', 'emma', 'rich', 'presh', 'steph', 'oreva']
message=(f"""dear {friends_invited[1]} you are invited to the get togther guess, whichpeople are coming? 
\n\t{friends_invited[0]}, \n\t{friends_invited[2]},\n\t{friends_invited[3]},\n\t{friends_invited[4]},\n\t{friends_invited[5]}.""")
print(message)
wont_come=friends_invited[0]
print(friends_invited)
friends_invited.remove(wont_come)
print(f"mr {wont_come} can't make it ")
