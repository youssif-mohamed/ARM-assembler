
def findded(string, sub, start=0):
    y = string.find(sub,start)
    if y == -1:
        return 0
    else:
        return 1
    

# take the input then filter it
x = input('Enter an assembly code: ')
x = x.lower().strip().split(",")
x = x[0].split() + x[1:]
for i in range(0, len(x)):
    x[i] = x[i].strip()
print(x)

# extract s_bit and i_bit from the assembly code
s_bit = findded(x[0], "s", 3)
i_bit = int(not findded(x[-1], "r"))
print(f"s bit is: {s_bit} and i bit is: {i_bit}")



# Dictionary of data processing instructions
data_processing = {"and":"0000", "eor":"0001",
       "sub":"0010", "rsb":"0011",
       "add":"0100", "adc":"0101",
       "sbc":"0110", "rsc":"0111",
       "tst":"1000", "teq":"1001",
       "cmp":"1010", "cmn":"1011",
       "orr":"1100", "mov":"1101"
                                }
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
for i in data_processing:
    if i in x[0]:
        cmd = i
        cond = x[0][len(cmd)+1:] if (s_bit) else x[0][len(cmd):]
        op = "00"
        
        destination_reg = bin(int(x[1][1]))[2:].zfill(4)
        second_source = bin(int(x[-1][1]))[2:].zfill(12) 
        if cmd != "mov":
            first_source_reg = bin(int(x[2][1]))[2:].zfill(4)
        else:
            first_source_reg = "0000" #mov instruction handeling
        
        print(condition_dict[cond] + op + str(i_bit) + data_processing[cmd] + str(s_bit)  + first_source_reg + destination_reg + second_source)
        
