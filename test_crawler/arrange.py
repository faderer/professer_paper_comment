import os
import pandas as pd


def main():
    paperlist = pd.DataFrame(columns=('author', 'title', 'subtitle', 'citation', 'pub_date'))
    root = os.getcwd()
    teachers = os.listdir(root+'\\test')
    for t in teachers:
        source = os.listdir(root+'\\test\\'+t)
        for s in source:
            file_list = os.listdir(root+'\\test\\'+t+'\\'+s)
            if len(file_list) > 0:
                df = pd.read_excel(root+'\\test\\'+t+'\\'+s+'\\logfile_04-04-2021.xlsx')
                for row in df.itertuples():
                    if getattr(row, 'year') > 0:
                        paperlist = paperlist.append(
                            pd.DataFrame({'author': [t], 'title': [getattr(row, 'title')], 'subtitle': [s], 'citation': [str(getattr(row, 'citation'))[6:]], 'pub_date': [int(getattr(row, 'year'))]}),
                            ignore_index=True)
    print(paperlist)
    paperlist.to_csv('papers.txt', sep='\t', index=False, header=0)
if __name__ == "__main__":
    main()
    print('Done!')