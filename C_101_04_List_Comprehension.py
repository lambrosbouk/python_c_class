﻿# Επίλυση Δραστηριοτήτων του μαθήματος Προγραμματισμός Υπολογιστών
# Γ' ΕΠΑΛ
# ΤΟΜΕΑΣ ΠΛΗΡΟΦΟΡΙΚΗΣ
# worked with Python 2.7.10
# @ Tasos Chatzipapadopoulos

'''

ΚΕΦΑΛΑΙΟ 6ο ΔΙΑΧΕΙΡΙΣΗ ΑΡΧΕΙΩΝ
Δραστηριότητα 4 / σελίδα 101
Τι πιστεύετε ότι θα συμβεί, όταν θα εκτελεστούν τα παρακάτω σενάρια. Τεκμηριώστε
την άποψή σας. 
       
'''

# List Comprehension

# Δημιουργία λίστας τετραγώνων αριθμών από 1.. 10
my_list = [i**2 for i in range(1,11)]

# Άνοιγμα αρχείου για εγγραφή
f = open('output.txt', 'w')

# Γράψε τα στοιχεία της λίστας στο αρχείο
for item in my_list:
    f.write(str(item) + '\n') # δέχεται string όρισμα η write
f.close()

# Άνοιξε το αρχείο και εκτύπωσε τα περιεχόμενά του
f = open('output.txt', 'r')
print f.readline()
print f.read()
f.close()
    