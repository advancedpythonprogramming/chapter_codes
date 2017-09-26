inname, outname = "logs.txt", "logs_out.txt"

with open(inname) as infile:
    with open(outname, "w") as outfile:
        warnings = (l.replace('WARNING', '') for l in infile if 'WARNING' in l)
        for l in warnings:
            outfile.write(l)
