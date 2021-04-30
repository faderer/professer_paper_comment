import os
import pandas as pd
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django
if django.VERSION >= (1, 7):#自动判断版本
    django.setup()

def main():
    from polls.models import Paper
    root = os.getcwd()
    teachers = os.listdir(root + '\\paper\\test3')
    for t in teachers:
        source = os.listdir(root + '\\paper\\test3\\' + t)
        for s in source:
            file_list = os.listdir(root + '\\paper\\test3\\' + t + '\\' + s)
            if len(file_list) > 0:
                df = pd.read_excel(root + '\\paper\\test3\\' + t + '\\' + s + '\\logfile_04-07-2021.xlsx')
                for row in df.itertuples():
                    if getattr(row, 'year') > 0:
                        Paper.objects.get_or_create(author=t, title=getattr(row, 'title'), subtitle=s,
                                                    citation=int(str(getattr(row, 'citation'))[6:]),
                                                    pub_date=int(getattr(row, 'year')),
                                                    filename=getattr(row, 'filename'))



if __name__ == "__main__":
    main()
    print('Done!')
