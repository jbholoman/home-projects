import csv

input_file = 'Stella_08192024165217.csv'
keywords= ['sales', 'service', 'director of','vbho','green team','finance','nissan','state','warranty','vbni','general','administrative','transportation','honda','appointment','huho','accounting','title','parts','call center','blue','red','loaner','vbcdj','gsm','internet','vbch','Acura','vbac','dealership','receptionist','vbma','car','admin','echo','da','shop','ecto','used','vbto','bdc','empty','conference','lunch']  # List of keywords to filter out
stores_prefixes = [83, 69, 65, 57, 55, 52, 51, 54, 13]
all_data = []
prefix_count = 0



for i in stores_prefixes:
    with open(input_file, mode='r', newline='') as infile: 
        
        reader = csv.reader(infile, delimiter=',', quotechar='|')
        dealer_data = []
        count = 1
        
        for row in reader:
            if count >= 9: 
                second_column = row[1].strip().lower() # Defining second column 
                if not any(keyword in second_column for keyword in keywords): # Checking for keywords in column
                    if row and row[1].strip(): # Deleting row where the second column is empty
                        if row[7].isnumeric(): # Checking column 8 for numbers
                            if int(row[7][:2]) == stores_prefixes[prefix_count]: # comparing the first two numbers in row 7 with our inputs in our variable "stores_prefixes"
                        
                                agent_data = []
                                agent_data.append(row[1])
                                agent_data.append(row[3])
                                agent_data.append(row[5])
                                agent_data.append(row[6])
                                agent_data.append(row[7])
                                dealer_data.append(agent_data)

            count += 1

        all_data.append(dealer_data)
        prefix_count += 1


count = 0


for i in all_data:

    with open(str(stores_prefixes[count])+'_directory.csv', mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['First Name','Last Name','Role','Department','Extension/User ID'])
        writer.writerows(i)

    count += 1