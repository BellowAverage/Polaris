
--- 
title:  java使用swing制作桌面图形应用的实例教程 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解，java编程语言通过swing制作桌面图形应用的实例教程，通过一个简单的个人信息提交表单界面，让你了解swing的布局管理、窗口图标设置、编译和运行以及窗口菜单的设置。 日期：2023年8月25日 


### 实际效果

<img src="https://img-blog.csdnimg.cn/ddc4b0ce6c0741439bc2f50082015a1b.png#pic_center" alt="在这里插入图片描述"> 弹出新窗口帮助文档界面： <img src="https://img-blog.csdnimg.cn/ecd903475b4140c7a2d49d7f61da090e.png" alt="在这里插入图片描述"> 说明：设置新窗口图标和主窗口一致，也可在新窗口设置布局，同主窗口的配置方式。

### 代码实例

```
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.Desktop;
import java.net.URI;

public class MainWindow extends JFrame {<!-- -->
    public MainWindow() {<!-- -->
        setTitle("简易swing个人信息填写，多菜单界面demo实例");
        setSize(400, 300);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLayout(new BorderLayout());
        setLocation(200, 100);

        // 设置任务栏图标
        Image taskbarIcon = Toolkit.getDefaultToolkit().getImage("E:\\develop\\cursor\\java\\icon.png");
        setIconImage(taskbarIcon);


        // 创建菜单栏
        JMenuBar menuBar = new JMenuBar();
        setJMenuBar(menuBar);

        // 创建官网菜单项
        JMenuItem websiteMenuItem = new JMenuItem("官网");
        websiteMenuItem.addActionListener(new ActionListener() {<!-- -->
            @Override
            public void actionPerformed(ActionEvent e) {<!-- -->
                openWebsite();
            }
        });

        // 创建帮助菜单项
        JMenuItem helpMenuItem = new JMenuItem("帮助");
        helpMenuItem.addActionListener(new ActionListener() {<!-- -->
            @Override
            public void actionPerformed(ActionEvent e) {<!-- -->
                showHelpWindow();
            }
        });

        // 将菜单项添加到菜单栏
        JMenu menu = new JMenu("菜单");
        menuBar.add(menu);
        menu.add(websiteMenuItem);
        menu.add(helpMenuItem);

        // 创建个人信息填写表单
        JPanel formPanel = new JPanel(new GridBagLayout());
        GridBagConstraints constraints = new GridBagConstraints();
        constraints.anchor = GridBagConstraints.WEST;

        JLabel nameLabel = new JLabel("姓名：");
        JTextField nameTextField = new JTextField(20);

        JLabel genderLabel = new JLabel("性别：");
        JRadioButton maleRadioButton = new JRadioButton("男");
        JRadioButton femaleRadioButton = new JRadioButton("女");
        ButtonGroup genderButtonGroup = new ButtonGroup();
        genderButtonGroup.add(maleRadioButton);
        genderButtonGroup.add(femaleRadioButton);

        JLabel hobbyLabel = new JLabel("爱好：");
        JCheckBox javaCheckBox = new JCheckBox("Java");
        JCheckBox pythonCheckBox = new JCheckBox("Python");
        JCheckBox cSharpCheckBox = new JCheckBox("C#");

        JLabel introLabel = new JLabel("简介：");
        JTextArea introTextArea = new JTextArea(5, 20);

        JLabel dropdownLabel = new JLabel("下拉：");
        String[] dropdownOptions = {<!-- -->"不内卷", "规避竞争的最好方法是避免竞争", "养生上班才好"};
        JComboBox&lt;String&gt; dropdownComboBox = new JComboBox&lt;&gt;(dropdownOptions);

        JButton submitButton = new JButton("提交");
        submitButton.addActionListener(new ActionListener() {<!-- -->
            @Override
            public void actionPerformed(ActionEvent e) {<!-- -->
                submitForm(nameTextField.getText(), maleRadioButton.isSelected(),
                        javaCheckBox.isSelected(), pythonCheckBox.isSelected(),
                        cSharpCheckBox.isSelected(), introTextArea.getText(),
                        dropdownComboBox.getSelectedItem().toString());
            }
        });
		//设置布局
        constraints.gridx = 0;//设置x坐标
        constraints.gridy = 0;//设置y坐标
        formPanel.add(nameLabel, constraints);//添加组件

        constraints.gridx = 1;
        constraints.gridwidth = 3;//设置宽度
        formPanel.add(nameTextField, constraints);

        constraints.gridx = 0;
        constraints.gridy = 1;
        formPanel.add(genderLabel, constraints);

        constraints.gridx = 1;
        formPanel.add(maleRadioButton, constraints);

        constraints.gridx = 2;
        formPanel.add(femaleRadioButton, constraints);

        constraints.gridx = 0;
        constraints.gridy = 2;
        formPanel.add(hobbyLabel, constraints);

        constraints.gridx = 1;
        constraints.gridwidth = 1;
        formPanel.add(javaCheckBox, constraints);

        constraints.gridx = 2;
        constraints.gridwidth = 1;
        formPanel.add(pythonCheckBox, constraints);

        constraints.gridx = 3;
        constraints.gridwidth = 1;
        formPanel.add(cSharpCheckBox, constraints);

        constraints.gridx = 0;
        constraints.gridy = 3;
        formPanel.add(introLabel, constraints);

        constraints.gridx = 1;
        constraints.gridwidth = 3;
        formPanel.add(introTextArea, constraints);

        constraints.gridx = 0;
        constraints.gridy = 4;
        formPanel.add(dropdownLabel, constraints);

        constraints.gridx = 1;
        constraints.gridwidth = 3;
        formPanel.add(dropdownComboBox, constraints);

        constraints.gridx = 5;
        constraints.gridy = 6;
        constraints.gridwidth = 4;
        formPanel.add(submitButton, constraints);

        add(formPanel, BorderLayout.CENTER);

        setVisible(true);
    }
	//打开官网
    private void openWebsite() {<!-- -->
        int result = JOptionPane.showConfirmDialog(this, "点击确认即可打开www.youqiong.net", "打开官网", JOptionPane.OK_CANCEL_OPTION, JOptionPane.INFORMATION_MESSAGE);
        if (result == JOptionPane.OK_OPTION) {<!-- -->
            try {<!-- -->
                URI uri = new URI("https://www.youqiong.net");
                Desktop desktop = Desktop.getDesktop();
                if (desktop.isSupported(Desktop.Action.BROWSE)) {<!-- -->
                    desktop.browse(uri);
                }
            } catch (Exception e) {<!-- -->
                e.printStackTrace();
            }
        }
    }
	//显示新窗口
    private void showHelpWindow() {<!-- -->
        JFrame helpWindow = new JFrame();
        JScrollPane scrollPane = new JScrollPane();
        JTextPane textPane = new JTextPane();
        StringBuilder content = new StringBuilder();
        for (int i = 1; i &lt;= 200; i++) {<!-- -->
            content.append(i).append("\n");
        }
        textPane.setText(content.toString());
        scrollPane.setViewportView(textPane);
        helpWindow.add(scrollPane);
        helpWindow.setTitle("帮助窗口");
        helpWindow.setSize(400, 300);
        helpWindow.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        helpWindow.setVisible(true);
    }
	//弹出表单信息
    private void submitForm(String name, boolean isMale, boolean hasJavaHobby,
                            boolean hasPythonHobby, boolean hasCSharpHobby,
                            String intro, String selectedOption) {<!-- -->
        JOptionPane.showMessageDialog(this, "姓名：" + name + "\n"
                + "性别：" + (isMale ? "男" : "女") + "\n"
                + "爱好：" + (hasJavaHobby ? "Java " : "") + "\n"
                + "      " + (hasPythonHobby ? "Python " : "") + "\n"
                + "      " + (hasCSharpHobby ? "C#" : "") + "\n"
                + "个人简介：" + intro + "\n"
                + "下拉框选项：" + selectedOption, "个人基本信息", JOptionPane.INFORMATION_MESSAGE);
    }
	//实例化窗口
    public static void main(String[] args) {<!-- -->
        SwingUtilities.invokeLater(new Runnable() {<!-- -->
            @Override
            public void run() {<!-- -->
                new MainWindow();
            }
        });
    }
}

```

### 执行代码说明

#### 1.记得先编译，中文用utf-8

```

javac -encoding UTF-8 MainWindow.java


```

#### 2.执行命令输入如下即可

```
java MainWindow

```

end：输入后按回车即可弹出最初的窗口效果。
