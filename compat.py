line_count = 1
#Pop the most compatible option off and create line 1 {"Line 1": medication}
def initialize_list(sorted_compat_total, final_lines):
    global line_count
    for key, _ in sorted_compat_total.items():
        medications_in_line = [key]
        final_lines[f"Line {line_count}"] = medications_in_line
        line_count += 1
        sorted_compat_total.pop(key)
        break
        

def add_next_medication_to_line(sorted_compat_total, final_lines, chart):
    global line_count
    for first_med, _ in sorted_compat_total.items():
        for line_key, meds_list in final_lines.items():
            all_tests_pass = True  # Reset flag for each line check
            for med in meds_list:
                if not is_compat(med, first_med, chart):       
                    all_tests_pass = False
                    break
            
            if all_tests_pass:
                add_medication_to_line(line_key, first_med, final_lines)
                sorted_compat_total.pop(first_med)  # Remove the added medication
                break

        if all_tests_pass:
            break

    if not all_tests_pass:
        final_lines[f"Line {line_count}"] = [first_med]
        sorted_compat_total.pop(first_med)  # Remove the added medication
        line_count += 1


def is_compat(primary_medication, secondary_medication, chart):
 
    if chart[primary_medication][secondary_medication] == "C":
        return True
    elif chart[primary_medication][secondary_medication] == "self":
        return True
    else:
        return False
    
def add_line(compat_total, line_count, final_lines):
    drug, _ = compat_total[0]
    final_lines[f"line {line_count}"] = [drug]
    line_count = line_count + 1
    compat_total.pop(0)

#Add the medication to a specific line number
def add_medication_to_line(line_number, medication, final_lines):
    final_lines[line_number].append(medication)


def main():

    #sample input that will be obtained from interface
    chart = {
        "dobutamine":{
            "dobutamine":"self",
            "dopamine":"C",
            "epinephrine":"C",
            "fentanyl":"C",
            "lasix":"x",
            "norepinephrine":"C",
            "phenylephrine":"C",
            "precedex":"x",
            "propofol":"x",
            "versed":"x"
            },
        "dopamine":{
            "dobutamine":"C",
            "dopamine":"self",
            "epinephrine":"C",
            "fentanyl":"C",
            "lasix":"x",
            "norepinephrine":"C",
            "phenylephrine":"C",
            "precedex":"x",
            "propofol":"x",
            "versed":"C"
            },
        "epinephrine":{
            "dobutamine":"C",
            "dopamine":"C",
            "epinephrine":"self",
            "fentanyl":"C",
            "lasix":"C",
            "norepinephrine":"C",
            "phenylephrine":"C",
            "precedex":"C",
            "propofol":"x",
            "versed":"C"
            },
        "fentanyl":{
            "dobutamine":"C",
            "dopamine":"C",
            "epinephrine":"C",
            "fentanyl":"self",
            "lasix":"C",
            "norepinephrine":"C",
            "phenylephrine":"C",
            "precedex":"C",
            "propofol":"C",
            "versed":"C"
            },
        "lasix":{
            "dobutamine":"x",
            "dopamine":"x",
            "epinephrine":"C",
            "fentanyl":"C",
            "lasix":"self",
            "norepinephrine":"x",
            "phenylephrine":"x",
            "precedex":"C",
            "propofol":"C",
            "versed":"x"
            },
        "norepinephrine":{
            "dobutamine":"C",
            "dopamine":"C",
            "epinephrine":"C",
            "fentanyl":"C",
            "lasix":"x",
            "norepinephrine":"self",
            "phenylephrine":"C",
            "precedex":"C",
            "propofol":"C",
            "versed":"C"
            },
        "phenylephrine":{
            "dobutamine":"C",
            "dopamine":"C",
            "epinephrine":"C",
            "fentanyl":"C",
            "lasix":"x",
            "norepinephrine":"C",
            "phenylephrine":"self",
            "precedex":"C",
            "propofol":"x",
            "versed":"C"
            },
        "precedex":{
            "dobutamine":"C",
            "dopamine":"C",
            "epinephrine":"C",
            "fentanyl":"C",
            "lasix":"C",
            "norepinephrine":"C",
            "phenylephrine":"C",
            "precedex":"self",
            "propofol":"C",
            "versed":"C"
            },
        "propofol":{
            "dobutamine":"x",
            "dopamine":"x",
            "epinephrine":"x",
            "fentanyl":"C",
            "lasix":"C",
            "norepinephrine":"C",
            "phenylephrine":"x",
            "precedex":"C",
            "propofol":"self",
            "versed":"C"
            },
        "versed":{
            "dobutamine":"x",
            "dopamine":"C",
            "epinephrine":"C",
            "fentanyl":"C",
            "lasix":"x",
            "norepinephrine":"C",
            "phenylephrine":"C",
            "precedex":"C",
            "propofol":"C",
            "versed":"self"
            },
    }
    #sample drug list that will be obtained from interface
    drugs = ["dobutamine","dopamine","epinephrine","fentanyl","lasix","norepinephrine","phenylephrine","precedex","propofol","versed"]

    #initialize the holding items/global variables
    compat_total = {}
    lines = {}
    final_lines = {}
    line_count = 1
    


    #Create the dictionary for each medication and how many compatible medications there are in the list {medication: number of compats}
    for med in drugs:
        counter = 0
        drug_data = chart[med]  # Get the data for the current drug
        for drug, value in drug_data.items():
            if value == "C":
                counter += 1
        compat_total[med] = counter



    #Order medications by most compatibilities to least
    sorted_compat_total = dict(sorted(compat_total.items(), key=lambda x:x[1], reverse = True))

    # Add the first line to dictionary
    initialize_list(sorted_compat_total, final_lines)


    # Check next line against the dictionary, if all compatible add, if not, check next line, if no lines, add line
    for i in range(len(drugs)-1):
        add_next_medication_to_line(sorted_compat_total, final_lines, chart)

    print(final_lines)

if __name__ == "__main__":
    main()
