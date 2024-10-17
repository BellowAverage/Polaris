
--- 
title:  在当前bash(sh)中执行脚本和注册函数 
tags: []
categories: [] 

---
在研究时，我们使用了source指令而没有使用sh或者bash来执行脚本，就是因为source指令可以让脚本在当前bash(sh)中执行；而sh或者bash则会新启动一个bash来执行。 <img src="https://img-blog.csdnimg.cn/direct/da8d1358f9094b1fb2662b6437cdb33f.png" alt="在这里插入图片描述"> 我们可以通过下面这个脚本做测试

```
# test.sh
# 用一个数组保存进程ID和进程名
processInfo=()

# 查找父进程的进程号
findParentID() {<!-- -->
    if [ $1 = $2 ]; then
        # 如果父进程号等于目标进程号，说明已经找到了父进程
        # 打印所有进程信息
        echo "processInfo: ${processInfo[@]}"
        return
    else
        # 获取当前进程的父进程号
        parentID=$(ps -o ppid= $1)
        # 获取父进程的名字
        parentName=$(ps -o comm= $parentID)

        # 将父进程号和父进程名保存到数组中
        processInfo+=($parentID $parentName)

        findParentID $parentID $2
    fi
}

currentName=$(ps -o comm= $$)
processInfo+=($$ $currentName)
findParentID $$ $1

```

## bash

```
bash test.sh $$

```

>  
 processInfo: 45322 bash 40883 bash 


当前bash的进程ID是40883，新启动的bash的进程ID是45322。

## source

```
source test.sh $$

```

>  
 processInfo: 40883 bash 


可以见得没有启动新的bash程序。 source还可以让自动注册脚本中的函数。 比如上面指令让脚本中的findParentID方法可以直接被使用。

```
findParentID $$ $$

```

>  
 processInfo: 40883 bash 


相似的应用在Python虚拟环境中也有体现。 比如我们启动一个虚拟环境，使用下面的命令

```
source .env/bin/activate

```

<img src="https://img-blog.csdnimg.cn/direct/cd6c5fd72d8e4abe85ef7c90ce979b51.png" alt="在这里插入图片描述"> 而退出虚拟环境的方法deactivate则注册在.env/bin/activate文件中

```
# This file must be used with "source bin/activate" *from bash*
# you cannot run it directly

deactivate () {<!-- -->
    # reset old environment variables
    if [ -n "${_OLD_VIRTUAL_PATH:-}" ] ; then
        PATH="${_OLD_VIRTUAL_PATH:-}"
        export PATH
        unset _OLD_VIRTUAL_PATH
    fi
    if [ -n "${_OLD_VIRTUAL_PYTHONHOME:-}" ] ; then
        PYTHONHOME="${_OLD_VIRTUAL_PYTHONHOME:-}"
        export PYTHONHOME
        unset _OLD_VIRTUAL_PYTHONHOME
    fi

    # This should detect bash and zsh, which have a hash command that must
    # be called to get it to forget past commands.  Without forgetting
    # past commands the $PATH changes we made may not be respected
    if [ -n "${<!-- -->BASH:-}" -o -n "${ZSH_VERSION:-}" ] ; then
        hash -r 2&gt; /dev/null
    fi

    if [ -n "${_OLD_VIRTUAL_PS1:-}" ] ; then
        PS1="${_OLD_VIRTUAL_PS1:-}"
        export PS1
        unset _OLD_VIRTUAL_PS1
    fi

    unset VIRTUAL_ENV
    unset VIRTUAL_ENV_PROMPT
    if [ ! "${1:-}" = "nondestructive" ] ; then
    # Self destruct!
        unset -f deactivate
    fi
}

# unset irrelevant variables
deactivate nondestructive

VIRTUAL_ENV="/home/fangliang/numpy-example/.env"
export VIRTUAL_ENV

_OLD_VIRTUAL_PATH="$PATH"
PATH="$VIRTUAL_ENV/bin:$PATH"
export PATH

# unset PYTHONHOME if set
# this will fail if PYTHONHOME is set to the empty string (which is bad anyway)
# could use `if (set -u; : $PYTHONHOME) ;` in bash
if [ -n "${PYTHONHOME:-}" ] ; then
    _OLD_VIRTUAL_PYTHONHOME="${PYTHONHOME:-}"
    unset PYTHONHOME
fi

if [ -z "${VIRTUAL_ENV_DISABLE_PROMPT:-}" ] ; then
    _OLD_VIRTUAL_PS1="${<!-- -->PS1:-}"
    PS1="(.env) ${<!-- -->PS1:-}"
    export PS1
    VIRTUAL_ENV_PROMPT="(.env) "
    export VIRTUAL_ENV_PROMPT
fi

# This should detect bash and zsh, which have a hash command that must
# be called to get it to forget past commands.  Without forgetting
# past commands the $PATH changes we made may not be respected
if [ -n "${<!-- -->BASH:-}" -o -n "${ZSH_VERSION:-}" ] ; then
    hash -r 2&gt; /dev/null
fi

```

如果我们使用bash来执行，则因为虚拟环境会在新启动的bash中存在，并会快速退出。回到我们原来的bash中时，已经不是虚拟环境了。相应的deactivate方法也没注册到环境中。 <img src="https://img-blog.csdnimg.cn/direct/54a2eda23a6d49378adba30e85a1d08d.png" alt="在这里插入图片描述"> 所以如果我们希望脚本对当前bash有所影响，就要使用source去执行脚本；如果不希望影响当前bash，则可以使用bash或者sh去执行。 需要注意的是，bash并不等价于sh。sh（Bourne Shell）是1978年由史蒂夫·伯恩编写的shell；bash（Bourne-Again Shell）是1987年由布莱恩·福克斯为GNU计划编写的Unix shell。主要目标是与POSIX标准保持一致，同时兼顾对sh的兼容，是各种Linux发行版标准配置的Shell。比如上面test.sh使用bash可以正确执行，而sh执行就会报错。
