in_file = open('sensorData.json', 'r')
out_file = open('sensorData-fixed.json', 'w')

depth = 0
for in_line in in_file:
    out_line = ''
    for char in in_line:
        out_line += char
        if char == '{':
            depth += 1
        elif char =='}':
            depth += -1
            if depth == 0:
                out_line += ','
                
    out_file.write(out_line)

in_file.close()
out_file.close()
