
--- 
title:  qt项目用qInstallMessageHandler函数输出log日志 
tags: []
categories: [] 

---
### 1.qInstallMessageHandler函数输出日志

非常简单，废话不多说我们直接上代码：

```
#include &lt;QApplication&gt;
#include &lt;QMutex&gt;
#include &lt;QDateTime&gt;
#include &lt;QFile&gt;
#include &lt;QTextStream&gt;

#define LOG_PATH QCoreApplication::applicationDirPath() + "/log/"

bool makeFilePath(const QString filePath)
{<!-- -->
    QDir dir(filePath);
    if(!dir.exists())
    {<!-- -->
        bool ok = dir.mkpath(filePath);
        if(ok)
        {<!-- -->
            qDebug() &lt;&lt; "Make" &lt;&lt; filePath &lt;&lt; "success";
            return true;
        }
        else
        {<!-- -->
            qDebug() &lt;&lt; "Make" &lt;&lt; filePath &lt;&lt; "fail";
            return false;
        }
    }
    return true;
}

void myLog(QtMsgType type, const QMessageLogContext &amp;context, const QString &amp;msg)
{<!-- -->
    static QMutex mutex;
    mutex.lock();

    QString text;
    switch(type)
    {<!-- -->
    case QtDebugMsg:
        text = QString("Debug");
        break;
    case QtInfoMsg:
        text = QString("Info");
        break;
    case QtWarningMsg:
        text = QString("Warning");
        break;

    case QtCriticalMsg:
        text = QString("Critical");
        break;

    case QtFatalMsg:
        text = QString("Fatal");
    }

    QString current_date_time = QDateTime::currentDateTime().toString("yyyy-MM-dd hh:mm:ss::zzz");
    QString current_date = QString("%1").arg(current_date_time);
    QString context_info = QString("%1-%2").arg(QString(context.file)).arg(context.line);
    QString message = QString("%1 - %2: %3: %4").arg(current_date).arg(text).arg(context_info).arg(msg);
    makeFilePath(LOG_PATH);
    QString timestr = LOG_PATH + QDateTime::currentDateTime().toString("yyyy-MM-dd");
    QString logName = timestr + ".log";
    QFile file(logName);
    file.open(QIODevice::WriteOnly | QIODevice::Append);
    QTextStream text_stream(&amp;file);
    text_stream &lt;&lt; message &lt;&lt; "\r\n";
    file.flush();
    file.close();
    mutex.unlock();
}

int main(int argc, char **argv)
{<!-- -->
    qInstallMessageHandler(myMessageOutput);
    QApplication app(argc, argv);
    qInfo() &lt;&lt; "hello world";
    return app.exec();
}

```

### 2.在Release模式编译下会遇到的问题

在Release模式下，编译器产生的机器码是经过优化的。这种优化会导致在生成的可执行文件中去除了调试符号信息，从而无法通过调试符号信息获取行号等信息。我们只需要做如下修改：

```
DEFINES += QT_MESSAGELOGCONTEXT //qmake编译，在.pro文件中添加
add_definitions("-DQT_MESSAGELOGCONTEXT") // 用cmake编译，在CMakeLists.txt文件中添加

```
