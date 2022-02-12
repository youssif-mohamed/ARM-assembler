def findded(string : str, sub_string : str, start : int = 0) -> int:
    """[The function checks if a sub string is in a certain string and returns a bool]

    Args:
        string ([str]): [The string to search in.]
        sub_string ([str]): [A sub string to search with.]
        start (int, optional): [the index to start the searching process within the string]. Defaults to 0.

    Returns:
        [int]: [the return is zero if the the sub_string is not found other wise the return will be 1]
    """
    is_in_string = string.find(sub_string, start)
    if is_in_string == -1:
        return 0
    else:
        return 1
def parse(assembly_code : str)-> list:
    """[The function parse the assembly code string and converts it to a list of sub_strings]

    Args:
        assembly_code (str): [a normal assembly_code dtrong]

    Returns:
        list: [a list containg all the features of the assembly code in the form of sub_strings]
    """
    # make all charcters of the assembly_code string lower case, remove white spaces in its start and end,
    # The split the assembly_code string into a list of sub_strings
    assembly_code = assembly_code.lower().strip().split(",")

    firt_sub_string_in_assembly_code_list = assembly_code[0]
    assembly_code = firt_sub_string_in_assembly_code_list.split() + assembly_code[1:]

    for i in range(len(assembly_code)):
        assembly_code[i] = assembly_code[i].strip().strip("[]")
    return assembly_code
def assembly_to_machine_code(assembly: str)-> str:
    """[This function converts an assebly code to 32-bits machine code]

    Args:
        assembly ([str]): [string containing the assebly code]

    Returns:
        [str]: [string containing the 32-bits machine code]
    """
    
    # check if the assemby code is a data istruction 
    is_data_instruction = findded(assembly,"[")

    # take the input and pasre it to a list of strings
    assembly = parse(assembly)
    

    # extract s_bit, i_bit abd l_bit from the assembly code
    s_bit = findded(assembly[0], "s", 3)
    i_bit = int(not findded(assembly[-1], "r"))
    l_bit = int(assembly[0][0]=='b' and findded(assembly[0],'l'))
    


    # Dictionary of data processing instructions
    data_processing = {"and":"0000", "eor":"0001",
        "sub":"0010", "rsb":"0011",
        "add":"0100", "adc":"0101",
        "sbc":"0110", "rsc":"0111",
        "tst":"1000", "teq":"1001",
        "cmp":"1010", "cmn":"1011",
        "orr":"1100", "mov":"1101"
        }
    # Dictionary of memory instructions
    memory_instruction = {"ldr":"1", "str":"0"}
    
    # Dictionary of conditional excutions
    condition_dict = {"eq":"0000", "ne":"0001",
                            "cs":"0010", "hs":"0010",
                            "cc":"0011", "lo":"0011",
                            "ml":"0100", "pl":"0101",
                            "vs":"0110", "vc":"0111",
                            "hl":"1000", "ls":"1001",
                            "ge":"1010", "lt":"1011",
                            "le":"1101", "al":"1110",
                            "":"1110" #unconditional
                            }


    if (assembly[0][0] == 'b'): # checking for branch instruction and returns its machine code.
        op = '10'
        cond = assembly[0][2:] if (l_bit) else assembly[0][1:]
        return condition_dict[cond] + op + '1' + str(l_bit) + bin(int(assembly[1][1]) - 1)[2:].zfill(24)  

    elif (is_data_instruction):
        cmd = assembly[0][:3]
        cond = assembly[0][3+1:] if (s_bit) else assembly[0][3:]
        op = "01"
        base_reg = bin(int(assembly[2][1]))[2:].zfill(4)
        destination_source_reg = bin(int(assembly[1][1]))[2:].zfill(4)
        offset = bin(int(assembly[-1][1]))[2:].zfill(12)
        return (condition_dict[cond] + op + str(int(not i_bit)) + "1100" +
            memory_instruction[cmd] + base_reg + destination_source_reg + offset)

    else: # Data processing instructions

        cmd = assembly[0][:3]
        cond = assembly[0][len(cmd)+1:] if (s_bit) else assembly[0][len(cmd):]
        op = "00"
        
        destination_reg = bin(int(assembly[1][1]))[2:].zfill(4)
        second_source = bin(int(assembly[-1][1]))[2:].zfill(12) 
        if cmd != "mov":
            first_source_reg = bin(int(assembly[2][1]))[2:].zfill(4)
        else:
            first_source_reg = "0000" #mov instruction handeling
        
        return (condition_dict[cond] + op + str(i_bit) + data_processing[cmd] + str(s_bit)  + first_source_reg + destination_reg + second_source)

def assembly_to_machine_file(assembly_code_file_path: str, machine_code_file_path: str): 
    """[Reads a txt file containing multiple lines of ARM assembly code and produces a txt file containing 
    crossponding 32-bits machine code lines.]

    Args:
        assembly_code_file_path (str): [string containing the path of the assembly code txt file]
        machine_code_file_path (str): [string containing the path of the machine code txt file]
    """     
    
    assembly_file = open(assembly_code_file_path, 'r')
    machine_file = open(machine_code_file_path, 'w')

    y = assembly_file.readlines()

    for i in y:
        machine_file.write(assembly_to_machine_code(i))
        machine_file.write("\n")
        
    assembly_file.close()
    machine_file.close()

# calling the function
assembly_to_machine_file('assembly_code.txt','machine_code.txt')