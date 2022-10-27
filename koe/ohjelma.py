
#puuttuvat funktiot
def bytes_to_megabytes(bytes):
    return bytes/(1024*1024)

bytes = 748723979
megabytes =  bytes_to_megabytes(bytes)
print(f"{bytes:d} B = {megabytes:.2f} Mb")

#toinen tehtävä

#def double(numbers):
    #doubled = []
    #for a in numbers:
       # doubled.append(2*a)
    #return doubled


#numbers = [12, 5, 21, 4, 8, 0, 11]
#doubled = double(numbers)
#print("Alkuperäiset luvut / Original numbers: " + str(numbers))
#print("Tuplatut luvut: / Doubled numbers: " + str(doubled))