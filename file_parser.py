import csv


def log_parse(input_file,output_file):

        with open(output_file,'w') as out_file:
                with open(input_file,'r') as in_file:

                        search="[1]"
                        csv_schema=["Date","Host","Process","Message"]
                        writer= csv.DictWriter(out_file,fieldnames=csv_schema)
                        writer.writeheader()
                        for line in in_file:

                                log_line={}
                                if(search in line):
                                        log_line["Date"]=' '.join(line.split(" ")[0:3])
                                        log_line["Host"]=line.split(" ")[3]
                                        log_line["Process"]=line.split(" ")[4].rstrip(":")
                                        log_line["Message"]=" ".join(line.split(" ")[5:]).rstrip("\n")

                                        writer.writerow(log_line)
                                else:
                                        continue
                                print log_line






        return 0


if __name__ == "__main__":
        log_parse("syslog","out_sys.csv")
