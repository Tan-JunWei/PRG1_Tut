#Programming I

#######################
#     Mission 9.1     #
#       Sorting       #
#######################

#Background
#==========
# Tom has TWO list of places in the Western and Eastern part of Singapore.
# Define a function Sort() function with 2 parameters.
# The first parameter is to pass in a list of Strings and
# the second parameters is to pass in a Boolean flag.
# If the flag is True, the list is sorted in ascending order.
# If the flag is False, the list is sorted in descending order.
# The function returns the sorted list.

#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.
#2) You MUST use the following variables
#   - SingaporeWest
#   - SingaporeEast

SingaporeWest = [
'Western Water Catchment',
'Pioneer',
'Jurong West',
'Lim Chu Kang',
'Tuas',
'Choa Chu Kang',
'Bukit Batok',
'Western Islands Planning Area',
'Tengah',
'Jurong East',
'Clementi',
'Bukit Panjang',
'Boon Lay']

SingaporeEast = ['Changi Bay',
'Katong',
'Lorong Halus',
'Simei',
'Bedok Reservoir',
'Tanah Merah',
'East Coast',
'Pasir Ris',
'Marine Parade',
'Chai Chee',
'Bedok',
'Changi Village',
'Kembangan',
'Loyang',
'Tampines',
'Ubi',
'Siglap',
'Elias',
'Joo Chiat',
'Kaki Bukit',
'Changi East',
'Changi'
]

#START CODING FROM HERE
#======================

#Create your function here
def Sort(sg, boolean):
    if boolean:
        sorted_sg = sorted(sg,reverse=True)
    else:
        sorted_sg = sorted(sg)

    return sorted_sg




    
#Calling function
#Comment out when submitting in Coursemology
# Sort(SingaporeWest, True)

#3) For testing, print out the sorted list
#   - Comment out before submitting
print(Sort(SingaporeWest, False))
