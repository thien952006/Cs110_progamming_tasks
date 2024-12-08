# Author   : Xuan Thien Bui
# Email    : xuanthienbui@umass.edu
# Spire ID : 34750117
import csv
def read_csv(fname):
    try:
        with open(fname, 'r') as f:
            contents=list(csv.reader(f))
            if(contents==[]):
                return None
            else:
                lst=[]
                for i in range(len(contents)):
                    dict={'name': 'x', 'section': 'y', 'average': 't', 'scores': 'z'}
                    dict['name']=contents[i][0]
                    dict['section']=contents[i][1]
                    new_content=[float(number) for number in contents[i][2:]]
                    dict['scores']=new_content
                    dict['average']=round(sum(new_content)/(len(new_content)),3)
                    lst.append(dict)
                return lst
    except Exception:
        print(f"Error occurred when opening {fname} to read")
        return None
def write_csv(fname,student_data):
    try:
        with open(fname, 'a') as f:
            for i in range(len(student_data)):
                f.write(student_data[i]['name']+',')
                f.write(student_data[i]['section']+',')
                f.write(','.join(str(number) for number in student_data[i]['scores'])+'\n')
    except Exception:
        print(f"Error occurred when opening {fname} to write")
        return None
def filter_section(student_data,section_name):
    res=[]
    for dict in student_data:
        if(dict['section']==section_name):
            res.append(dict)
    return res
def filter_average(student_data,min_inc,max_exc):
    res=[dict for dict in student_data if dict['average']>=min_inc and dict['average']<max_exc]
    return res
def split_section(fname):
    if(read_csv(fname)==None):
        return None
    else:
        content=read_csv(fname)
        data=set()
        data={dict['section'] for dict in content}
        for x in data:
            y=filter_section(content, x)
            write_csv(f"{fname.split('.')[0]}_section_{x}.csv",y)
def get_assignment_stats(student_data):
    return_list=[]
    nums=[dict['average'] for dict in student_data]
    def get_stats(x):
        mean=sum(x)/len(x)
        minimum=min(x)
        maximum=max(x)
        range=maximum-minimum
        std_dev = (sum([(n - mean)**2 for n in x]) / len(x)) ** (1/2)
        return [mean,minimum,maximum,range,std_dev]
    res=get_stats(nums)
    return_list.append({'mean':res[0],'std_dev':res[4],'min':res[1],'max':res[2],'range':res[3]})
    for i in range(0,10):
        lst=[dict['scores'][i] for dict in student_data]
        ans=get_stats(lst)
        return_list.append({'mean':ans[0],'std_dev':ans[4],'min':ans[1],'max':ans[2],'range':ans[3]})
    return return_list


            