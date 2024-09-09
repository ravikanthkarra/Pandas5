import pandas as pd


def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(employee)
    df['max_salary'] = df.groupby('departmentId')['salary'].transform('max')
    # print(df)
    df = df[(df['salary'] == df['max_salary'])]
    df2 = df.merge(department, left_on='departmentId', right_on='id', how='inner', suffixes=('_emple', '_dept'))
    df2 = df2[['name_dept', 'name_emple', 'salary']]
    return df2.rename(columns={'name_dept': 'Department', 'name_emple': 'Employee', 'salary': 'Salary'})
