import csv


headers = ['idx',
           'vlen',
           'vgrpdepth',
           'vgrpstride',
           'ic_hit',
           'ic_mis',
           'l2_rd_hit0',
           'l2_rd_mis0',
           'l2_wr_hit0',
           'l2_wr_mis0',
           'l2_rd_hit1',
           'l2_rd_mis1',
           'l2_wr_hit1',
           'l2_wr_mis1',
           'l2_rd_hit2',
           'l2_rd_mis2',
           'l2_wr_hit2',
           'l2_wr_mis2',
           'l2_rd_hit3',
           'l2_rd_mis3',
           'l2_wr_hit3',
           'l2_wr_mis3',
           'vp_busy_cnt',
           'vp_vfld_num',
           'vp_vfst_num',
           'vp_vcvt_num',
           'vp_vfadd_num',
           'vp_vfcmp_num',
           'vp_vfdiv_num',
           'vp_vfdot_num',
           'vp_vfmul_num',
           'vp_vfsmax_num',
           'vp_vfssum_num',
           'vp_vflogic_num',
           'vp_vfld_busy_cnt',
           'vp_vfst_busy_cnt',
           'vp_vfld_req_cnt',
           'vp_vfst_req_cnt',
           'vp_hzd_stall_cnt',
           'mtime_start',
           'mtime_end'
           ]
           
    
'''
headerstest = ['class','name','sex','height','year']
rows = [
        {'class':1,'name':'xiaoming','sex':'male','height':168,'year':23},
        {'class':1,'name':'xiaohong','sex':'female','height':162,'year':22},
        {'class':2,'name':'xiaozhang','sex':'female','height':163,'year':21},
        {'class':2,'name':'xiaoli','sex':'male','height':158,'year':21},
    ]


with open('test2.csv','w',newline='')as f:
    f_csv = csv.DictWriter(f,headerstest)
    f_csv.writeheader()
    print(type(rows[0]))
    f_csv.writerows(rows)
 
'''
notvalid = [1,2,3,9,10,11,12,13,14,31,32,33,34,54,55]
def  read_csv_row(fd):
    row_content = []
    for i in range(0,56):
        line = fd.readline()
        if not line:
            return row_content
        if i in notvalid:
#            print("%d line not valid"%i)
            continue
        row_ret = []
    #    line_split = line.split()
    #    print(type(line))
    #    print(type(line_split))
    #    print(len(line_split))
    #    for i in range(0,len(line_split)):
    #        print(i)
    #        print(line_split[i])
    #    print(line)
        val = int(line.split()[-1])
        row_content.append(val)
    return row_content
    
    
    
with open('log.txt','r') as flog:
    cnt = 0
    row_cnt = 0
    f_csv = open('output.csv','w')
    fcsv = csv.DictWriter(f_csv,headers)
    fcsv.writeheader()
    csv_rows = []
    while True:
        line = flog.readline()
        if not line:
            break
        linesplit = line.split()
        if linesplit[0] == "PERFORMANCE":
            print(linesplit[0])
            row_line = read_csv_row(flog)
            dict_line = {'idx':row_cnt}
            print(len(headers))
            print(len(row_line))
            print(dict_line)
            for j in range(0,len(row_line)):
                dict_line[headers[j]] = row_line[j]
            print(dict_line)
            csv_rows.append(dict_line)
    fcsv.writerows(csv_rows)

    flog.close
    f_csv.close
