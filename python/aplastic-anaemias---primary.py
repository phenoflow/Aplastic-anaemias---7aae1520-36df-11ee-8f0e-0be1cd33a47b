# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"D200400","system":"readv2"},{"code":"D201100","system":"readv2"},{"code":"D201200","system":"readv2"},{"code":"D201311","system":"readv2"},{"code":"D204.00","system":"readv2"},{"code":"D20z.00","system":"readv2"},{"code":"102848.0","system":"med"},{"code":"107828.0","system":"med"},{"code":"109273.0","system":"med"},{"code":"15422.0","system":"med"},{"code":"15658.0","system":"med"},{"code":"16108.0","system":"med"},{"code":"21723.0","system":"med"},{"code":"30994.0","system":"med"},{"code":"31275.0","system":"med"},{"code":"31491.0","system":"med"},{"code":"31774.0","system":"med"},{"code":"32715.0","system":"med"},{"code":"32900.0","system":"med"},{"code":"34754.0","system":"med"},{"code":"34953.0","system":"med"},{"code":"37320.0","system":"med"},{"code":"40244.0","system":"med"},{"code":"41142.0","system":"med"},{"code":"43166.0","system":"med"},{"code":"43825.0","system":"med"},{"code":"44913.0","system":"med"},{"code":"47438.0","system":"med"},{"code":"47620.0","system":"med"},{"code":"57114.0","system":"med"},{"code":"57859.0","system":"med"},{"code":"5823.0","system":"med"},{"code":"61326.0","system":"med"},{"code":"61462.0","system":"med"},{"code":"64625.0","system":"med"},{"code":"65351.0","system":"med"},{"code":"65502.0","system":"med"},{"code":"66239.0","system":"med"},{"code":"68087.0","system":"med"},{"code":"69027.0","system":"med"},{"code":"69061.0","system":"med"},{"code":"69269.0","system":"med"},{"code":"69379.0","system":"med"},{"code":"70128.0","system":"med"},{"code":"71965.0","system":"med"},{"code":"72104.0","system":"med"},{"code":"7225.0","system":"med"},{"code":"72252.0","system":"med"},{"code":"938.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('aplastic-anaemias-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["aplastic-anaemias---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["aplastic-anaemias---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["aplastic-anaemias---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
