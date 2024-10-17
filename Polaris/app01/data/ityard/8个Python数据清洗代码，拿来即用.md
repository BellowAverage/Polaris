
--- 
title:  8个Python数据清洗代码，拿来即用 
tags: []
categories: [] 

---
作者：Admond Lee

机器之心编译

不管你承不承认，数据清洗着实不是一件简单的任务，大多数情况下这项工作是十分耗时而乏味的，但它又是十分重要的。

如果你经历过数据清洗的过程，你就会明白我的意思。而这正是撰写这篇文章的目的——让读者更轻松地进行数据清洗工作。

事实上，我在不久前意识到，在进行数据清洗时，有一些数据具有相似的模式。也正是从那时起，我开始整理并编译了一些数据清洗代码（见下文），我认为这些代码也适用于其它的常见场景。

由于这些常见的场景涉及到不同类型的数据集，因此本文更加侧重于展示和解释这些代码可以用于完成哪些工作，以便读者更加方便地使用它们。

**我的数据清洗小工具箱**

在下面的代码片段中，数据清洗代码被封装在了一些函数中，代码的目的十分直观。你可以直接使用这些代码，无需将它们嵌入到需要进行少量参数修改的函数中。

**1. 删除多列数据**

```
def drop_multiple_col(col_names_list, df): 
    '''
    AIM    -&gt; Drop multiple columns based on their column names 

    INPUT  -&gt; List of column names, df

    OUTPUT -&gt; updated df with dropped columns 
    ------
    '''
    df.drop(col_names_list, axis=1, inplace=True)
    return df
```

有时，并不是所有列的数据都对我们的数据分析工作有用。因此，「df.drop」可以方便地删掉你选定的列。

**2. 转换 Dtypes**

```
def change_dtypes(col_int, col_float, df): 
    '''
    AIM    -&gt; Changing dtypes to save memory

    INPUT  -&gt; List of column names (int, float), df

    OUTPUT -&gt; updated df with smaller memory  
    ------
    '''
    df[col_int] = df[col_int].astype('int32')
    df[col_float] = df[col_float].astype('float32')
```

当我们面对更大的数据集时，我们需要对「dtypes」进行转换，从而节省内存。如果你有兴趣学习如何使用「Pandas」来处理大数据，我强烈推荐你阅读「Why and How to Use Pandas with Large Data」这篇文章（https://towardsdatascience.com/why-and-how-to-use-pandas-with-large-data-9594dda2ea4c）。

**3. 将分类变量转换为数值变量**

```
def convert_cat2num(df):
    # Convert categorical variable to numerical variable
    num_encode = {'col_1' : {'YES':1, 'NO':0},
                  'col_2'  : {'WON':1, 'LOSE':0, 'DRAW':0}}  
    df.replace(num_encode, inplace=True)  
```

有一些机器学习模型要求变量是以数值形式存在的。这时，我们就需要将分类变量转换成数值变量然后再将它们作为模型的输入。对于数据可视化任务来说，我建议大家保留分类变量，从而让可视化结果有更明确的解释，便于理解。

**4. 检查缺失的数据**

```
def check_missing_data(df):
    # check for any missing data in the df (display in descending order)
    return df.isnull().sum().sort_values(ascending=False)
```

如果你想要检查每一列中有多少缺失的数据，这可能是最快的方法。这种方法可以让你更清楚地知道哪些列有更多的缺失数据，帮助你决定接下来在数据清洗和数据分析工作中应该采取怎样的行动。

**5. 删除列中的字符串**

```
def remove_col_str(df):
    # remove a portion of string in a dataframe column - col_1
    df['col_1'].replace('\n', '', regex=True, inplace=True)

    # remove all the characters after &amp;# (including &amp;#) for column - col_1
    df['col_1'].replace(' &amp;#.*', '', regex=True, inplace=True)
```

有时你可能会看到一行新的字符，或在字符串列中看到一些奇怪的符号。你可以很容易地使用 df['col_1'].replace 来处理该问题，其中「col_1」是数据帧 df 中的一列。

**6. 删除列中的空格**

```
def remove_col_white_space(df):
    # remove white space at the beginning of string 
    df[col] = df[col].str.lstrip()
```

当数据十分混乱时，很多意想不到的情况都会发生。在字符串的开头有一些空格是很常见的。因此，当你想要删除列中字符串开头的空格时，这种方法很实用。

**7. 将两列字符串数据（在一定条件下）拼接起来**

```
def concat_col_str_condition(df):
    # concat 2 columns with strings if the last 3 letters of the first column are 'pil'
    mask = df['col_1'].str.endswith('pil', na=False)
    col_new = df[mask]['col_1'] + df[mask]['col_2']
    col_new.replace('pil', ' ', regex=True, inplace=True)  # replace the 'pil' with emtpy space
```

当你希望在一定条件下将两列字符串数据组合在一起时，这种方法很有用。例如，你希望当第一列以某些特定的字母结尾时，将第一列和第二列数据拼接在一起。根据你的需要，还可以在拼接工作完成后将结尾的字母删除掉。

**8. 转换时间戳（从字符串类型转换为日期「DateTime」格式）**

```
def convert_str_datetime(df): 
    '''
    AIM    -&gt; Convert datetime(String) to datetime(format we want)

    INPUT  -&gt; df

    OUTPUT -&gt; updated df with new datetime format 
    ------
    '''
    df.insert(loc=2, column='timestamp', value=pd.to_datetime(df.transdate, format='%Y-%m-%d %H:%M:%S.%f'))
```

在处理时间序列数据时，你可能会遇到字符串格式的时间戳列。这意味着我们可能不得不将字符串格式的数据转换为根据我们的需求指定的日期「datetime」格式，以便使用这些数据进行有意义的分析和展示。**<em><em><em><img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9LbVhQS0ExOWdXOFpmcGljZDQwRXJpYkd1YUZpY0RCQ1JINklPdTFSbmM0VDNXM0oxd0UwajZrUTZHb3JSU2dpY2liMGZtTnJqM3l6bG9rdXAyamlhOVowWVZlQS82NDA?x-oss-process=image/format,png">**</em></em></em>

**原文链接：https://towardsdatascience.com/the-simple-yet-practical-data-cleaning-codes-ad27c4ce0a38**

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb2RBYW9nMXVLMFp1V3VYMnZ5SG9TWnpaUVdoaWNpYm51REpYeGhtU1pxQ3k3Mk5lZDRmWVNoTkNKTkZ3MVIzQm9pY0dyemRFVGEwMGhZUS82NDA?x-oss-process=image/format,png">
