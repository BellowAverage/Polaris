
--- 
title:  从sqlserver中导出视图然后导入另一个数据库中 
tags: []
categories: [] 

---
## 代码

因为可能存在导入是标间依赖的关系，比如A表中引用了B表但是是A表点导入的所以此时A表导入就会失败要先导入B表我这里采用了多次导入的方法失败了就放到新的子目录1中无线套娃最终导入完成

```
import java.io.*;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class ViewStructureTransfer2 {<!-- -->
    private static final String SOURCE_URL = "jdbc:sqlserver://rm-m5ebo95e1b0514649ko.sqlserver.rds.aliyuncs.com:3433;databasename=taikechuangxinZSTEST3;user=kingdee;password=123qweASD";
    private static final String TARGET_URL = "jdbc:sqlserver://47.104.197.13:1433;databaseName=AIS20230814140217;user=sa;password=btzn123@";
    String exportFile = "views.sql";
    private static final String EXPORT_PATH = "D:\\wxh\\dubbo\\exportView\\sql\\"; // 修改导出路径

    public static void main(String[] args) {<!-- -->
        // 导出视图结构到文件
        //exportViewStructure();

        // 导入视图结构到目标数据库
        importViewStructure();
    }

    private static void exportViewStructure() {<!-- -->
        Connection sourceConn = null;
        Statement sourceStmt = null;
        ResultSet resultSet = null;

        try {<!-- -->
            sourceConn = DriverManager.getConnection(SOURCE_URL);
            sourceStmt = sourceConn.createStatement();
            resultSet = sourceStmt.executeQuery("SELECT name FROM sys.objects WHERE type_desc = 'VIEW'");

            List&lt;String&gt; viewNames = new ArrayList&lt;&gt;();
            while (resultSet.next()) {<!-- -->
                viewNames.add(resultSet.getString("name"));
            }

            for (String viewName : viewNames) {<!-- -->
                ResultSet viewResultSet = sourceStmt.executeQuery("SELECT definition FROM sys.sql_modules WHERE object_id = OBJECT_ID('" + viewName + "')");
                StringBuilder viewStructure = new StringBuilder();
                while (viewResultSet.next()) {<!-- -->
                    viewStructure.append(viewResultSet.getString("definition")).append("\n");
                }
                viewResultSet.close();

                String exportFile = EXPORT_PATH + viewName + ".sql";
                FileWriter fileWriter = new FileWriter(exportFile);
                fileWriter.write(viewStructure.toString());
                fileWriter.close();

                System.out.println("Exported view structure for view: " + viewName + " to file: " + exportFile);
            }
        } catch (SQLException | IOException e) {<!-- -->
            e.printStackTrace();
        } finally {<!-- -->
            closeResultSet(resultSet);
            closeStatement(sourceStmt);
            closeConnection(sourceConn);
        }
    }

    private static void importViewStructure() {<!-- -->
        Connection targetConn = null;
        Statement targetStmt = null;
        FileInputStream fileInputStream = null;

        try {<!-- -->
            targetConn = DriverManager.getConnection(TARGET_URL);
            targetStmt = targetConn.createStatement();

            File folder = new File(EXPORT_PATH);
            File[] files = folder.listFiles((dir, name) -&gt; name.endsWith(".sql"));

            for (File file : files) {<!-- -->
                try{<!-- -->
                    fileInputStream = new FileInputStream(file);
                    byte[] buffer = new byte[(int) file.length()];
                    fileInputStream.read(buffer);
                    fileInputStream.close();

                    String script = new String(buffer);

                    targetStmt.execute(script);
                    System.out.println("Imported view structure from file: " + file.getName());
                }catch (SQLException | IOException e){<!-- -->
                    e.printStackTrace();
                    File errorFolder = new File(EXPORT_PATH + "/1");

                    // Create "1" folder if it doesn't exist
                    if (!errorFolder.exists()) {<!-- -->
                        boolean folderCreated = errorFolder.mkdir();
                        if (!folderCreated) {<!-- -->
                            System.out.println("Failed to create error folder!");
                            return;
                        }
                    }

                    // Move the exception file to the "1" folder
                    File exceptionFile = new File(EXPORT_PATH + "/" + file.getName());
                    boolean fileMoved = file.renameTo(new File(EXPORT_PATH + "/1/" + file.getName()));
                    if (!fileMoved) {<!-- -->
                        System.out.println("Failed to move exception file to the error folder!");
                    }
                }

            }
        } catch (SQLException e) {<!-- -->
            e.printStackTrace();
        } finally {<!-- -->

        }
        closeInputStream(fileInputStream);
        closeStatement(targetStmt);
        closeConnection(targetConn);
    }

    private static void closeResultSet(ResultSet resultSet) {<!-- -->
        if (resultSet != null) {<!-- -->
            try {<!-- -->
                resultSet.close();
            } catch (SQLException e) {<!-- -->
                e.printStackTrace();
            }
        }
    }

    private static void closeStatement(Statement statement) {<!-- -->
        if (statement != null) {<!-- -->
            try {<!-- -->
                statement.close();
            } catch (SQLException e) {<!-- -->
                e.printStackTrace();
            }
        }
    }

    private static void closeConnection(Connection connection) {<!-- -->
        if (connection != null) {<!-- -->
            try {<!-- -->
                connection.close();
            } catch (SQLException e) {<!-- -->
                e.printStackTrace();
            }
        }
    }

    private static void closeInputStream(FileInputStream fileInputStream) {<!-- -->
        if (fileInputStream != null) {<!-- -->
            try {<!-- -->
                fileInputStream.close();
            } catch (IOException e) {<!-- -->
                e.printStackTrace();
            }
        }
    }
}

```
